from .models import User, UserProfile, PasswordResetOTP
from rest_framework import fields, serializers
from django.contrib.auth.hashers import make_password
from django.contrib.auth.password_validation import validate_password


# user profile


class UserProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserProfile
        fields = [
            "id",
            "user",
            "first_name",
            "last_name",
            "bio",
            "location",
            "birth_date",
            "contact_number",
            "profile_image",
        ]

        read_only_fields = ["user"]


class SignupSerializer(serializers.ModelSerializer):

    profile = UserProfileSerializer()

    class Meta:
        model = User

        # #  only for email and password
        # fields = ["id", "email", "password"]

        # for adding user profile fields during signup
        fields = ["id", "email", "password", "profile"]
        extra_kwargs = {"password": {"write_only": True}}

    def validate_password(self, value):
        try:
            validate_password(value)
        except serializers.ValidationError as e:
            raise serializers.ValidationError(e.messages)
        return value

    def create(self, validated_data):

        password = make_password(validated_data["password"])
        user = User.objects.create(email=validated_data["email"], password=password)

        # #  only for email and password
        # UserProfile.objects.create(user=user)

        # for adding user profile fields during signup
        profile_data = validated_data.pop("profile", [])

        UserProfile.objects.create(user=user, **profile_data)

        return user


# chenge password
class ChangePasswordSerializer(serializers.Serializer):
    old_password = fields.CharField(required=True)
    new_password = fields.CharField(required=True)

    def validate_new_password(self, value):
        try:
            validate_password(value)
        except serializers.ValidationError as e:
            raise serializers.ValidationError(e.messages)
        return value


# forgot password serializer


class ForgotPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField()

    def validate_email(self, value):
        try:
            user = User.objects.get(email=value)
            if not user.is_active:
                raise serializers.ValidationError("This account is not active.")
        except User.DoesNotExist:
            raise serializers.ValidationError("No user found with this email address.")
        return value


class VerifyOTPSerializer(serializers.Serializer):
    email = serializers.EmailField()
    otp_code = serializers.CharField(max_length=6, min_length=6)

    def validate(self, data):
        email = data.get("email")
        otp_code = data.get("otp_code")

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            raise serializers.ValidationError("Invalid email address.")

        try:
            otp = PasswordResetOTP.objects.filter(
                user=user, otp_code=otp_code, is_used=False
            ).latest("created_at")

            if not otp.is_valid():
                raise serializers.ValidationError("OTP has expired or is invalid.")

            data["otp_instance"] = otp
            data["user"] = user

        except PasswordResetOTP.DoesNotExist:
            raise serializers.ValidationError("Invalid OTP code.")

        return data


class ResetPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField()
    otp_code = serializers.CharField(max_length=6, min_length=6)
    new_password = serializers.CharField(
        write_only=True, style={"input_type": "password"}
    )
    confirm_password = serializers.CharField(
        write_only=True, style={"input_type": "password"}
    )

    def validate_new_password(self, value):
        validate_password(value)
        return value

    def validate(self, data):
        if data["new_password"] != data["confirm_password"]:
            raise serializers.ValidationError(
                {"confirm_password": "Password fields didn't match."}
            )

        email = data.get("email")
        otp_code = data.get("otp_code")

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            raise serializers.ValidationError("Invalid email address.")

        try:
            otp = PasswordResetOTP.objects.filter(
                user=user, otp_code=otp_code, is_used=False
            ).latest("created_at")

            if not otp.is_valid():
                raise serializers.ValidationError("OTP has expired or is invalid.")

            data["otp_instance"] = otp
            data["user"] = user

        except PasswordResetOTP.DoesNotExist:
            raise serializers.ValidationError("Invalid OTP code.")

        return data
