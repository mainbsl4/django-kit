from rest_framework import serializers
from .models import GeneralSetting, SocialMedia, PrivacyPolicy


class GeneralSettingSerializer(serializers.ModelSerializer):

    class Meta:
        model = GeneralSetting
        fields = [
            "id",
            "industry_name",
            "site_title",
            "description",
            "logo",
            "favicon",
            "address",
            "phone",
            "email",
        ]


class SocialMediaSerializer(serializers.ModelSerializer):

    class Meta:

        model = SocialMedia

        fields = [
            "id",
            "platform_name",
            "profile_url",
            "icon",
            "created_at",
            "updated_at",
        ]


# privacy policy serializer
class PrivacyPolicySerializer(serializers.ModelSerializer):

    class Meta:
        model = PrivacyPolicy
        fields = [
            "id",
            "content",
            "is_active",
            "created_at",
            "updated_at",
        ]
