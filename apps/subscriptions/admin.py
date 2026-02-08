from django.contrib import admin
from .models import Plan, Feature
from unfold.admin import ModelAdmin, TabularInline

# Register your models here.


@admin.register(Feature)
class FeatureAdmin(ModelAdmin):
    list_display = ("name", "code", "is_active", "created_at")
    list_filter = ("is_active", "created_at")
    search_fields = ("name", "code", "description")
    prepopulated_fields = {"code": ("name",)}
    ordering = ("name",)


class FeatureInline(TabularInline):
    model = Plan.features.through
    extra = 1
    verbose_name = "Feature"
    verbose_name_plural = "Included Features"


@admin.register(Plan)
class PlanAdmin(ModelAdmin):
    list_display = (
        "name",
        "price",
        "billing_period",
        "trial_period_days",
        "is_active",
        "is_popular",
        "display_order",
    )
    list_filter = (
        "billing_period",
        "is_active",
        "is_popular",
        "created_at",
    )
    search_fields = ("name", "slug", "description")
    prepopulated_fields = {"slug": ("name",)}
    ordering = ("display_order", "price")

    # Exclude 'features' from main form since we're using an inline
    exclude = ("features",)
    inlines = [FeatureInline]

    fieldsets = (
        (
            None,
            {
                "fields": (
                    "name",
                    "slug",
                    "description",
                    "is_active",
                    "is_popular",
                    "display_order",
                )
            },
        ),
        ("Pricing", {"fields": ("price", "billing_period")}),
        ("Trial", {"fields": ("trial_period_days",), "classes": ("collapse",)}),
        # Uncomment below if you re-enable quota fields later
        # ("Limits & Quotas", {
        #     "fields": ("max_users", "storage_limit_gb"),
        #     "classes": ("collapse",)
        # }),
    )
