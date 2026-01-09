from django.urls import path
from .views import PageList

urlpatterns = [
    path("pages/", PageList.as_view(), name="page-list"),
]
