from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from .utils.managers import UserManager

# forgot password
from datetime import timedelta
import random
import string


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_("email address"), unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email

    @property
    def username(self):
        return self.email


# Profile


class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    bio = models.TextField(blank=True)
    location = models.CharField(max_length=100, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    contact_number = models.CharField(max_length=15, blank=True)
    profile_image = models.ImageField(
        upload_to="profile_images/", blank=True, null=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Profile of {self.user.email}"


# Forgot Password Token Model


class PasswordResetOTP(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="password_reset_otps"
    )
    otp_code = models.CharField(max_length=6)
    created_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField()
    is_used = models.BooleanField(default=False)

    # # Security Features
    # attempt_count = models.IntegerField(default=0)
    # max_attempts = 3

    class Meta:
        ordering = ["-created_at"]
        indexes = [
            models.Index(fields=["user", "otp_code", "is_used"]),
        ]

    def __str__(self):
        return f"OTP for {self.user.email} - {self.otp_code}"

    @classmethod
    def generate_otp(cls, user):
        """Generate a 6-digit OTP code"""
        otp_code = "".join(random.choices(string.digits, k=6))
        expires_at = timezone.now() + timedelta(minutes=10)  # OTP valid for 10 minutes

        return cls.objects.create(user=user, otp_code=otp_code, expires_at=expires_at)

    def is_valid(self):
        """Check if OTP is still valid"""
        return not self.is_used and timezone.now() < self.expires_at

    def mark_as_used(self):
        """Mark OTP as used"""
        self.is_used = True
        self.save()

    # # Security Features
    # def increment_attempts(self):
    #     self.attempt_count += 1
    #     self.save()
    #     return self.attempt_count

    # def is_locked(self):
    #     return self.attempt_count >= self.max_attempts
