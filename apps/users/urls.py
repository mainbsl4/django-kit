from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)
from .views import (
    SignupList,
    UserProfileList,
    UserProfileDetail,
    UserDetail,
    SignoutView,
    ChangePassword,
    ForgotPasswordView,
    VerifyOTPView,
    ResetPasswordView,
)


urlpatterns = [
    path("signup/", SignupList.as_view(), name="signup"),
    path("signin/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("profile/", UserProfileList.as_view(), name="user_profile_list"),
    path("profile/<int:pk>/", UserProfileDetail.as_view(), name="user_profile_detail"),
    path("user/<int:pk>/", UserDetail.as_view(), name="user_detail"),
    path("signout/", SignoutView.as_view(), name="signout"),
    path(
        # "user/<int:pk>/change-password/",
        "user/change-password/<int:pk>/",
        ChangePassword.as_view(),
        name="change_password",
    ),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("token/verify/", TokenVerifyView.as_view(), name="token_verify"),
    # forgot password
    path("forgot-password/", ForgotPasswordView.as_view(), name="forgot-password"),
    path("verify-otp/", VerifyOTPView.as_view(), name="verify-otp"),
    path("reset-password/", ResetPasswordView.as_view(), name="reset-password"),
]
