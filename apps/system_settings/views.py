from django.shortcuts import render
from rest_framework import generics, filters
from .models import GeneralSetting, SocialMedia, PrivacyPolicy
from .serializers import (
    GeneralSettingSerializer,
    SocialMediaSerializer,
    PrivacyPolicySerializer,
)
from rest_framework.permissions import AllowAny
from rest_framework import status
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.


class GeneralSettingList(generics.ListCreateAPIView):
    permission_classes = [AllowAny]

    queryset = GeneralSetting.objects.all()
    serializer_class = GeneralSettingSerializer

    def get(self, request, *args, **kwargs):

        response_data = {
            "success": True,
            "status": status.HTTP_200_OK,
            "message": "General Settings retrieved successfully",
            "data": self.list(request, *args, **kwargs).data,
        }
        return Response(response_data, status=status.HTTP_200_OK)


# social media views
class SocialMediaList(generics.ListCreateAPIView):
    permission_classes = [AllowAny]
    queryset = SocialMedia.objects.all()
    serializer_class = SocialMediaSerializer
    filter_backends = [
        DjangoFilterBackend,
        filters.OrderingFilter,
        filters.SearchFilter,
    ]
    filterset_fields = ["platform_name"]
    search_fields = ["platform_name"]
    ordering_fields = ["created_at", "platform_name"]
    ordering = ["platform_name"]

    def get(self, request, *args, **kwargs):

        response_data = {
            "success": True,
            "status": status.HTTP_200_OK,
            "message": "Social Media links retrieved successfully",
            "data": self.list(request, *args, **kwargs).data,
        }
        return Response(response_data, status=status.HTTP_200_OK)


# privacy policy views
def get_privacy_policy(request):

    try:
        privacy_policy = PrivacyPolicy.objects.get(is_active=True)

        context = {"privacy_policy": privacy_policy}
        return render(request, "privacy_policy.html", context)
    except PrivacyPolicy.DoesNotExist:
        context = {"error": "Privacy Policy not found."}
        return render(request, "privacy_policy.html", context)
