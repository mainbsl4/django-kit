from django.urls import path
from .views import GeneralSettingList, SocialMediaList

urlpatterns = [
    path(
        "general-settings/", GeneralSettingList.as_view(), name="general-setting-list"
    ),
    path("social-media/", SocialMediaList.as_view(), name="social-media-list"),
]
