from django.contrib import admin
from .models import ContactUs
from unfold.admin import ModelAdmin

# Register your models here.


@admin.register(ContactUs)
class ContactUsAdmin(ModelAdmin):
    list_display = ("first_name", "last_name", "email", "is_read", "created_at")
    list_filter = ("is_read", "created_at")
    search_fields = ("first_name", "last_name", "email", "message")
    readonly_fields = ("created_at", "updated_at")
    ordering = ("-created_at",)

    fieldsets = (
        ("Sender Info", {"fields": ("first_name", "last_name", "email")}),
        ("Message", {"fields": ("message",)}),
        ("Status", {"fields": ("is_read",)}),
        (
            "Timestamps",
            {
                "fields": ("created_at", "updated_at"),
                "classes": ("collapse",),  # Optional: collapses this section by default
            },
        ),
    )
