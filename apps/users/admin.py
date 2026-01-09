from django.contrib import admin
from .models import User, UserProfile, PasswordResetOTP
from unfold.admin import ModelAdmin

# Register your models here.


@admin.register(User)
class UserAdmin(ModelAdmin):
    list_display = ("email", "is_staff", "is_active", "date_joined")
    search_fields = ("email",)
    ordering = ("email",)


@admin.register(UserProfile)
class UserProfileAdmin(ModelAdmin):
    list_display = ("user", "first_name", "last_name", "location", "contact_number")
    search_fields = ("user__email", "first_name", "last_name", "location")
    ordering = ("user__email",)


@admin.register(PasswordResetOTP)
class PasswordResetOTPAdmin(ModelAdmin):
    list_display = ["user", "otp_code", "created_at", "expires_at", "is_used"]
    list_filter = ["is_used", "created_at"]
    search_fields = ["user__email", "otp_code"]
    readonly_fields = ["created_at"]

    def has_add_permission(self, request):
        return False
