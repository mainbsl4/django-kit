from django.shortcuts import render
from .models import Plan, Feature
from .serializers import PlanSerializer, FeatureSerializer
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import renderers
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework import status

# Create your views here.


class PlanViewSet(viewsets.ModelViewSet):

    permission_classes = [permissions.AllowAny]

    queryset = Plan.objects.all()
    serializer_class = PlanSerializer
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]
    filterset_fields = ["name", "slug", "billing_period"]
    search_fields = ["name", "description"]
    ordering_fields = ["price", "billing_period", "trial_period_days"]

    def list(self, request):
        queryset = self.filter_queryset(self.queryset)
        # serializers = PlanSerializer(queryset, many=True)
        serializers = self.serializer_class(
            queryset, many=True, context={"request": request}
        )

        response_data = {
            "success": True,
            "status": status.HTTP_200_OK,
            "message": "List of subscription plans",
            "data": serializers.data,
        }

        return Response(response_data)
