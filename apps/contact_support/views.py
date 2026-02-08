from django.shortcuts import render
from rest_framework import generics
from .models import ContactUs
from .serializers import ContactUsSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

# Create your views here.


# contact us message views
class ContactUsList(generics.ListCreateAPIView):
    permission_classes = [AllowAny]
    queryset = ContactUs.objects.all()
    serializer_class = ContactUsSerializer

    def post(self, request, *args, **kwargs):

        response_data = {
            "success": True,
            "status": status.HTTP_201_CREATED,
            "message": "Contact Us message created successfully",
            "data": self.create(request, *args, **kwargs).data,
        }
        return Response(response_data, status=status.HTTP_201_CREATED)
