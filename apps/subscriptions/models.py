from django.db import models
from django.core.validators import MinValueValidator
from decimal import Decimal


# Create your models here.
class Feature(models.Model):
    """Individual features that can be included in plans"""

    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    code = models.SlugField(
        max_length=50, unique=True, help_text="Unique identifier for feature"
    )
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Plan(models.Model):

    BILLING_PERIOD_CHOICES = [
        ("DAILY", ("Daily")),
        ("WEEKLY", ("Weekly")),
        ("MONTHLY", ("Monthly")),
        ("QUARTERLY", ("Quarterly")),
        ("YEARLY", ("Yearly")),
        ("LIFETIME", ("Lifetime")),
    ]

    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField(blank=True)

    # Pricing
    price = models.DecimalField(
        max_digits=10, decimal_places=2, validators=[MinValueValidator(Decimal("0.00"))]
    )
    billing_period = models.CharField(
        max_length=20, choices=BILLING_PERIOD_CHOICES, default="MONTHLY"
    )

    # Trial settings
    trial_period_days = models.PositiveIntegerField(
        default=0, help_text="Number of days for free trial (0 for no trial)"
    )

    # Plan features
    features = models.ManyToManyField(Feature, related_name="plans")

    # # Limits and quotas
    # max_users = models.PositiveIntegerField(
    #     null=True, blank=True, help_text="Maximum number of users (null for unlimited)"
    # )
    # storage_limit_gb = models.PositiveIntegerField(
    #     null=True, blank=True, help_text="Storage limit in GB (null for unlimited)"
    # )

    # Plan settings
    is_active = models.BooleanField(default=True)
    is_popular = models.BooleanField(
        default=False, help_text="Highlight this plan as popular"
    )
    display_order = models.PositiveIntegerField(
        default=0, help_text="Order to display plans"
    )

    # Metadata
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # class Meta:
    #     ordering = ["display_order", "price"]
    #     verbose_name = "Plan"
    #     verbose_name_plural = "Plans"

    def __str__(self):
        return f"{self.name} - {self.get_billing_period_display()}"

    # @property
    # def monthly_price(self):
    #     """Convert price to monthly equivalent for comparison"""
    #     multipliers = {
    #         "DAILY": 30,
    #         "WEEKLY": 4.33,
    #         "MONTHLY": 1,
    #         "QUARTERLY": 1 / 3,
    #         "YEARLY": 1 / 12,
    #         "LIFETIME": 0,
    #     }
    #     return self.price * Decimal(str(multipliers.get(self.billing_period, 1)))
