from django.db import models


class Page(models.Model):

    class PageTypes(models.TextChoices):
        LANDING = "landing", "Landing Page"
        ABOUT = "about", "About Us"
        SERVICES = "services", "Services"
        CONTACT = "contact", "Contact Us"
        BLOG = "blog", "Blog"

    page_type = models.CharField(max_length=100, choices=PageTypes.choices, unique=True)
    # title = models.CharField(max_length=200)
    # slug = models.SlugField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.get_page_type_display()}"


class PageSection(models.Model):

    class SectionTypes(models.TextChoices):
        HERO = "hero", "Hero Section"
        TEXT_BLOCK = "text_block", "Text Block"
        IMAGE_TEXT = "image_text", "Image + Text"
        CTA = "cta", "Call to Action"
        FEATURE_LIST = "feature_list", "Feature List"

    page = models.ForeignKey(Page, on_delete=models.CASCADE, related_name="sections")
    section_type = models.CharField(max_length=20, choices=SectionTypes.choices)
    order = models.PositiveIntegerField(default=0)
    title = models.CharField(max_length=300, blank=True, null=True)
    subtitle = models.CharField(max_length=500, blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to="page_sections/", blank=True, null=True)
    background_image = models.ImageField(
        upload_to="page_sections/backgrounds/", blank=True, null=True
    )
    button_text = models.CharField(max_length=100, blank=True, null=True)
    button_link = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return f"{self.page.get_page_type_display()} - {self.get_section_type_display()} (Order: {self.order})"


class FeatureItem(models.Model):
    section = models.ForeignKey(
        PageSection, on_delete=models.CASCADE, related_name="feature_items"
    )
    order = models.PositiveIntegerField(default=0)
    title = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    icon = models.ImageField(upload_to="feature_items/icons/", blank=True, null=True)

    def __str__(self):
        return f"{self.section.page.title} - {self.title}"
