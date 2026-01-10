from django.contrib import admin
from unfold.admin import ModelAdmin
from django.utils.html import format_html
from .models import GeneralSetting, SocialMedia, PrivacyPolicy

# Register your models here.


@admin.register(GeneralSetting)
class GeneralSettingAdmin(ModelAdmin):
    list_display = (
        "industry_name",
        "site_title",
        "email",
        "phone",
        "logo_preview",
        "favicon_preview",
    )

    search_fields = ("industry_name", "site_title", "email", "phone")

    readonly_fields = ("logo_preview", "favicon_preview")

    fieldsets = (
        (
            "Basic Information",
            {
                "fields": (
                    "industry_name",
                    "site_title",
                    "description",
                )
            },
        ),
        (
            "Branding",
            {
                "fields": (
                    "logo",
                    "logo_preview",
                    "favicon",
                    "favicon_preview",
                )
            },
        ),
        (
            "Contact Information",
            {
                "fields": (
                    "address",
                    "phone",
                    "email",
                )
            },
        ),
    )

    def logo_preview(self, obj):
        if obj.logo:
            return format_html('<img src="{}" style="height:60px;" />', obj.logo.url)
        return "No Logo"

    logo_preview.short_description = "Logo Preview"

    def favicon_preview(self, obj):
        if obj.favicon:
            return format_html('<img src="{}" style="height:32px;" />', obj.favicon.url)
        return "No Favicon"

    favicon_preview.short_description = "Favicon Preview"

    def has_add_permission(self, request):
        """
        Allow only ONE GeneralSetting instance
        """
        if GeneralSetting.objects.exists():
            return False
        return True


# social media admin
@admin.register(SocialMedia)
class SocialMediaAdmin(ModelAdmin):
    list_display = ("platform_name", "profile_url", "icon_preview", "created_at")
    search_fields = ("platform_name", "profile_url")
    readonly_fields = ("icon_preview", "created_at", "updated_at")

    def icon_preview(self, obj):
        if obj.icon:
            return format_html('<img src="{}" style="height:32px;" />', obj.icon.url)
        return "No Icon"

    icon_preview.short_description = "Icon Preview"
    ordering = ("platform_name",)
    list_per_page = 20


# privacy policy admin
@admin.register(PrivacyPolicy)
class PrivacyPolicyAdmin(ModelAdmin):
    list_display = ("is_active", "created_at", "updated_at")
    list_filter = ("is_active", "created_at", "updated_at")
    readonly_fields = ("created_at", "updated_at")

    def has_add_permission(self, request):
        """
        Allow only ONE active PrivacyPolicy instance
        """
        if PrivacyPolicy.objects.filter(is_active=True).exists():
            return False
        return True
