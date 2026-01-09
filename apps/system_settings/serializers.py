from rest_framework import serializers
from .models import GeneralSetting


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
