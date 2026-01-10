from django.db import models
from ckeditor.fields import RichTextField


# Create your models here.
class GeneralSetting(models.Model):

    industry_name = models.CharField(max_length=255)
    site_title = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    logo = models.ImageField(upload_to="system_settings/general_settings/logos/")
    favicon = models.ImageField(upload_to="system_settings/general_settings/favicons/")
    address = models.TextField(null=True, blank=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)

    def __str__(self):
        return self.industry_name


class SocialMedia(models.Model):
    platform_name = models.CharField(max_length=100)
    profile_url = models.URLField()
    icon = models.ImageField(upload_to="system_settings/social_icons/")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.platform_name


# privacy policy


class PrivacyPolicy(models.Model):
    content = RichTextField()
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Privacy Policy - {'Active' if self.is_active else 'Inactive'}"
