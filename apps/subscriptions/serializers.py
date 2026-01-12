from rest_framework import serializers
from .models import Feature, Plan


class FeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feature
        fields = [
            "id",
            "name",
            "description",
            "code",
            "is_active",
            "created_at",
            "updated_at",
        ]


class PlanSerializer(serializers.ModelSerializer):
    features = FeatureSerializer(many=True, read_only=True)

    class Meta:
        model = Plan
        fields = [
            "id",
            "name",
            "slug",
            "description",
            "price",
            "billing_period",
            "trial_period_days",
            "features",
            "is_active",
            "is_popular",
            "created_at",
            "updated_at",
        ]
