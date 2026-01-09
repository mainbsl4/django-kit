from .models import Page, PageSection
from .serializers import PageSerializer, PageSectionSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from django.db.models import Q, Prefetch


class PageList(APIView):

    permission_classes = [AllowAny]

    def get(self, request, format=None):

        params = request.GET

        page_type = params.get("page_type", None)
        section_type = params.get("section_type", None)
        if page_type:
            if section_type:
                pages = Page.objects.prefetch_related(
                    Prefetch(
                        "sections",
                        queryset=PageSection.objects.filter(section_type=section_type)
                        .order_by("order")
                        .prefetch_related("feature_items"),
                    )
                ).filter(Q(page_type=page_type))
            else:
                pages = Page.objects.prefetch_related(
                    Prefetch(
                        "sections",
                        queryset=PageSection.objects.all()
                        .order_by("order")
                        .prefetch_related("feature_items"),
                    )
                ).filter(Q(page_type=page_type))
        else:
            pages = Page.objects.prefetch_related(
                Prefetch(
                    "sections",
                    queryset=PageSection.objects.all()
                    .order_by("order")
                    .prefetch_related("feature_items"),
                )
            ).all()
        serializer = PageSerializer(pages, many=True)

        response_data = {
            "success": True,
            "status": status.HTTP_200_OK,
            "message": "Pages retrieved successfully",
            "data": serializer.data,
        }
        return Response(response_data)
