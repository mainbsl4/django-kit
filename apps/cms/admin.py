from django.contrib import admin
from .models import Page, PageSection, FeatureItem
from unfold.admin import ModelAdmin, TabularInline, StackedInline


class FeatureItemInline(TabularInline):
    model = FeatureItem
    extra = 1
    fields = ("order", "title", "description", "icon")
    ordering = ("order",)


class PageSectionInline(StackedInline):
    model = PageSection
    extra = 1
    fields = (
        "section_type",
        "order",
        "title",
        "subtitle",
        "content",
        "image",
        "background_image",
        "button_text",
        "button_link",
    )
    ordering = ("order",)
    show_change_link = True


# ---------- Model Admins ----------


@admin.register(Page)
class PageAdmin(ModelAdmin):
    list_display = ("page_type", "created_at", "updated_at")
    list_filter = ("page_type", "created_at")
    search_fields = ("page_type", "page_type")
    # prepopulated_fields = {"slug": ("page_type",)}
    inlines = [PageSectionInline]
    ordering = ("-created_at",)


@admin.register(PageSection)
class PageSectionAdmin(ModelAdmin):
    list_display = (
        "page",
        "section_type",
        "order",
        "title",
        "created_at",
    )
    list_filter = ("section_type", "page")
    search_fields = ("title", "subtitle", "content")
    ordering = ("page", "order")
    inlines = [FeatureItemInline]


@admin.register(FeatureItem)
class FeatureItemAdmin(ModelAdmin):
    list_display = ("section", "order", "title")
    search_fields = ("title", "description")
    ordering = ("section", "order")
