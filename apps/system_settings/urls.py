from django.urls import path
from .views import GeneralSettingList

urlpatterns = [
    path(
        "general-settings/", GeneralSettingList.as_view(), name="general-setting-list"
    ),
]
