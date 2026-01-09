from django.shortcuts import render
from rest_framework import generics
from .models import GeneralSetting
from .serializers import GeneralSettingSerializer
from rest_framework.permissions import AllowAny
from rest_framework import status
from rest_framework.response import Response

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
