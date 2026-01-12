# Subscription Plans Seeding

This document details the subscription plans and features created by the `seed_subscriptions` command.

## Command Usage

```bash
# Seed subscription plans and features
python manage.py seed_subscriptions

# Include subscriptions when seeding all data
python manage.py seed_all

# Seed everything except subscriptions
python manage.py seed_all --skip-subscriptions
```

## Subscription Plans

The seeding creates 6 pre-configured subscription plans:

### 1. Free Plan
- **Price:** $0/month
- **Trial:** None
- **Display Order:** 1
- **Features:**
  - Basic Support
  - Data Export

### 2. Starter Plan
- **Price:** $9.99/month
- **Trial:** 14 days
- **Display Order:** 2
- **Description:** Great for individuals and small projects
- **Features:**
  - Basic Support
  - API Access
  - Team Collaboration
  - Data Export

### 3. Professional Plan ⭐ (Most Popular)
- **Price:** $29.99/month
- **Trial:** 30 days
- **Display Order:** 3
- **Description:** Most popular for growing businesses
- **Features:**
  - Priority Support
  - API Access
  - Advanced Analytics
  - Custom Branding
  - Team Collaboration
  - Unlimited Projects
  - Data Export
  - Webhooks

### 4. Business Plan
- **Price:** $79.99/month
- **Trial:** 30 days
- **Display Order:** 4
- **Description:** Advanced features for teams
- **Features:**
  - Priority Support
  - Phone Support
  - API Access
  - Advanced Analytics
  - Custom Branding
  - Team Collaboration
  - Unlimited Projects
  - Advanced Security
  - Data Export
  - Webhooks
  - Custom Integrations

### 5. Enterprise Plan
- **Price:** $299.99/month
- **Trial:** 30 days
- **Display Order:** 5
- **Description:** Custom solutions for large organizations
- **Features:** All features including:
  - Priority Support
  - Phone Support
  - API Access
  - Advanced Analytics
  - Custom Branding
  - Team Collaboration
  - Unlimited Projects
  - Advanced Security
  - Data Export
  - Webhooks
  - Custom Integrations
  - Dedicated Account Manager
  - SLA Guarantee
  - Onboarding Training

### 6. Professional Annual Plan
- **Price:** $287.90/year (Save 20%)
- **Trial:** 30 days
- **Display Order:** 6
- **Description:** Professional plan with annual billing
- **Features:** Same as Professional Plan

## Features List

The seeding creates 15 features that can be assigned to plans:

| Feature | Code | Description |
|---------|------|-------------|
| Basic Support | `basic-support` | Email support during business hours |
| Priority Support | `priority-support` | 24/7 priority email and chat support |
| Phone Support | `phone-support` | Direct phone line to support team |
| API Access | `api-access` | Full REST API access |
| Advanced Analytics | `advanced-analytics` | Detailed reports and insights |
| Custom Branding | `custom-branding` | Add your own logo and colors |
| Team Collaboration | `team-collaboration` | Share and collaborate with team members |
| Unlimited Projects | `unlimited-projects` | Create unlimited number of projects |
| Advanced Security | `advanced-security` | Two-factor authentication and SSO |
| Data Export | `data-export` | Export your data anytime |
| Webhooks | `webhooks` | Integrate with external services |
| Custom Integrations | `custom-integrations` | Build custom integrations |
| Dedicated Account Manager | `account-manager` | Personal account manager |
| SLA Guarantee | `sla-guarantee` | 99.9% uptime guarantee |
| Onboarding Training | `onboarding-training` | Personalized onboarding sessions |

## Database Models

### Feature Model
```python
- name: CharField (max 100, unique)
- code: SlugField (max 50, unique)
- description: TextField
- is_active: BooleanField
- created_at: DateTimeField
- updated_at: DateTimeField
```

### Plan Model
```python
- name: CharField (max 100)
- slug: SlugField (max 100, unique)
- description: TextField
- price: DecimalField
- billing_period: CharField (DAILY/WEEKLY/MONTHLY/QUARTERLY/YEARLY/LIFETIME)
- trial_period_days: PositiveIntegerField
- features: ManyToManyField (Feature)
- is_active: BooleanField
- is_popular: BooleanField
- display_order: PositiveIntegerField
- created_at: DateTimeField
- updated_at: DateTimeField
```

## Idempotency

The seed command is **idempotent**:
- Safe to run multiple times
- Won't create duplicates
- Shows warnings for existing records
- Uses `get_or_create()` for safe seeding

## Customization

To customize plans, edit the `seed_subscriptions.py` file:
```
apps/subscriptions/management/commands/seed_subscriptions.py
```

You can modify:
- Plan names, prices, and descriptions
- Feature lists and descriptions
- Trial periods
- Display order
- Add/remove plans or features
