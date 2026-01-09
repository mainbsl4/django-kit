from django.shortcuts import render
from rest_framework import generics
from .models import GeneralSetting
from .serializers import GeneralSettingSerializer

# Create your views here.


class GeneralSettingList(generics.ListCreateAPIView):
    queryset = GeneralSetting.objects.all()
    serializer_class = GeneralSettingSerializer
