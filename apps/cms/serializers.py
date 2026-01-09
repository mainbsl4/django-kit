from rest_framework import serializers
from .models import Page, PageSection, FeatureItem


def remove_empty_fields(data):
    """
    Remove keys where value is None, empty string, or empty list/dict
    """
    if isinstance(data, dict):
        return {
            k: remove_empty_fields(v)
            for k, v in data.items()
            if v not in (None, "", [], {})
        }
    elif isinstance(data, list):
        return [
            remove_empty_fields(item) for item in data if item not in (None, "", {}, [])
        ]
    return data


class FeatureItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeatureItem
        fields = [
            "id",
            "order",
            "title",
            "description",
            "icon",
        ]

    # def to_representation(self, instance):
    #     data = super().to_representation(instance)
    #     return remove_empty_fields(data)


class PageSectionSerializer(serializers.ModelSerializer):
    feature_items = FeatureItemSerializer(many=True, read_only=True)

    class Meta:
        model = PageSection
        fields = [
            "id",
            "section_type",
            "order",
            "title",
            "subtitle",
            "content",
            "image",
            "background_image",
            "button_text",
            "button_link",
            "feature_items",
        ]

    # def to_representation(self, instance):
    #     data = super().to_representation(instance)
    #     return remove_empty_fields(data)


class PageSerializer(serializers.ModelSerializer):
    sections = PageSectionSerializer(many=True, read_only=True)

    class Meta:
        model = Page
        fields = [
            "id",
            "page_type",
            # "title",
            # "slug",
            "created_at",
            "updated_at",
            "sections",
        ]
