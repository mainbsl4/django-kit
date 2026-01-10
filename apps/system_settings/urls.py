from django.urls import path
from .views import GeneralSettingList, SocialMediaList, get_privacy_policy

urlpatterns = [
    path(
        "general-settings/", GeneralSettingList.as_view(), name="general-setting-list"
    ),
    path("social-media/", SocialMediaList.as_view(), name="social-media-list"),
    path("privacy-policy/", get_privacy_policy, name="privacy-policy"),
]
