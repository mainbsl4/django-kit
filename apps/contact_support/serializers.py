from rest_framework import serializers
from .models import ContactUs


class ContactUsSerializer(serializers.ModelSerializer):

    class Meta:

        model = ContactUs

        fields = [
            "id",
            "first_name",
            "last_name",
            "email",
            "message",
            # "is_read",
            "created_at",
            "updated_at",
        ]
