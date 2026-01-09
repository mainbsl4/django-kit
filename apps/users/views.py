from .models import User, UserProfile, PasswordResetOTP
from .serializers import (
    SignupSerializer,
    UserProfileSerializer,
    ChangePasswordSerializer,
    ForgotPasswordSerializer,
    VerifyOTPSerializer,
    ResetPasswordSerializer,
)
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics

from rest_framework.permissions import AllowAny, IsAuthenticated
from .utils.send_email import send_otp_email
from rest_framework_simplejwt.tokens import RefreshToken


class SignupList(APIView):
    permission_classes = [AllowAny]

    def post(self, request, format=None):
        serializer = SignupSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            response_data = {
                "success": True,
                "status": status.HTTP_201_CREATED,
                "message": "User created successfully",
                "data": serializer.data,
            }
            return Response(response_data, status=status.HTTP_201_CREATED)

        response_error = {
            "success": False,
            "status": status.HTTP_400_BAD_REQUEST,
            "message": "User creation failed",
            "errors": serializer.errors,
        }
        return Response(response_error, status=status.HTTP_400_BAD_REQUEST)


# user profile
class UserProfileList(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        userProfile = UserProfile.objects.filter(user=request.user)
        serializer = UserProfileSerializer(userProfile, many=True)

        response_data = {
            "success": True,
            "status": status.HTTP_200_OK,
            "message": "User profile fetched successfully",
            "data": serializer.data,
        }
        return Response(response_data)


class UserProfileDetail(APIView):

    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return UserProfile.objects.get(pk=pk, user=self.request.user)
        except UserProfile.DoesNotExist:
            raise Http404

    def put(self, request, pk, format=None):
        userProfile = self.get_object(pk)
        serializer = UserProfileSerializer(userProfile, data=request.data)
        if serializer.is_valid():
            serializer.save()

            response_data = {
                "success": True,
                "status": status.HTTP_200_OK,
                "message": "User profile updated successfully",
                "data": serializer.data,
            }
            return Response(response_data)

        response_error = {
            "success": False,
            "status": status.HTTP_400_BAD_REQUEST,
            "message": "User profile update failed",
            "errors": serializer.errors,
        }

        return Response(response_error, status=status.HTTP_400_BAD_REQUEST)


# delete user
class UserDetail(APIView):

    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk, email=self.request.user.email)
        except User.DoesNotExist:
            raise Http404

    def delete(self, request, pk, format=None):
        user = self.get_object(pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# Sign out user
class SignoutView(APIView):

    permission_classes = (IsAuthenticated,)

    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()

            response_data = {
                "success": True,
                "status": status.HTTP_205_RESET_CONTENT,
                "message": "User logged out successfully",
            }

            return Response(response_data, status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:

            response_error = {
                "success": False,
                "status": status.HTTP_400_BAD_REQUEST,
                "message": "Logout failed",
                "errors": str(e),
            }
            return Response(response_error, status=status.HTTP_400_BAD_REQUEST)


# chenge password
class ChangePassword(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ChangePasswordSerializer

    def put(self, request, pk):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        old_password = serializer.validated_data["old_password"]
        new_password = serializer.validated_data["new_password"]

        try:
            obj = User.objects.get(pk=pk)
        except User.DoesNotExist:
            return Response({"error": "User not found"}, status=404)

        if not obj.check_password(old_password):
            return Response({"error": "Old password does not match"}, status=400)

        obj.set_password(new_password)
        obj.save()

        response_data = {
            "success": True,
            "status": status.HTTP_200_OK,
            "message": "Password changed successfully",
        }
        return Response(response_data, status=status.HTTP_200_OK)


# forgot password


class ForgotPasswordView(APIView):
    """
    Request password reset OTP
    """

    permission_classes = [AllowAny]
    serializer_class = ForgotPasswordSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data["email"]
            user = User.objects.get(email=email)

            # Generate OTP
            otp = PasswordResetOTP.generate_otp(user)

            # Send email
            try:
                send_otp_email(user, otp.otp_code)
                return Response(
                    {
                        "message": "OTP has been sent to your email address.",
                        "email": email,
                    },
                    status=status.HTTP_200_OK,
                )
            except Exception as e:
                print(e)

                return Response(
                    {"error": f"Failed to send email.  Please try again later."},
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class VerifyOTPView(APIView):
    """
    Verify OTP code without resetting password
    """

    permission_classes = [AllowAny]
    serializer_class = VerifyOTPSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            return Response(
                {
                    "message": "OTP verified successfully.  You can now reset your password.",
                    "email": serializer.validated_data["email"],
                },
                status=status.HTTP_200_OK,
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ResetPasswordView(APIView):
    """
    Reset password using OTP
    """

    permission_classes = [AllowAny]
    serializer_class = ResetPasswordSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data["user"]
            otp = serializer.validated_data["otp_instance"]
            new_password = serializer.validated_data["new_password"]

            # Set new password
            user.set_password(new_password)
            user.save()

            # Mark OTP as used
            otp.mark_as_used()

            # Optionally:  Invalidate all other OTPs for this user
            PasswordResetOTP.objects.filter(user=user, is_used=False).exclude(
                id=otp.id
            ).update(is_used=True)

            return Response(
                {
                    "message": "Password has been reset successfully.  You can now login with your new password."
                },
                status=status.HTTP_200_OK,
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
