from django.contrib import admin
from unfold.admin import ModelAdmin
from django.utils.html import format_html
from .models import GeneralSetting

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
