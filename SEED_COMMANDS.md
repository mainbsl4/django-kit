# Database Seeding Guide

This guide explains how to seed your database with test data.

## Quick Start

### Seed Everything (Recommended)
```bash
python manage.py seed_all
```

This command runs all seeding commands at once:
- ✅ Users & Profiles
- ✅ System Settings & Social Media
- ✅ Subscription Plans & Features

---

## Individual Seed Commands

If you want to seed specific data only:

### 1. Seed Users
```bash
python manage.py seed_users
```

**Creates:**
- 1 Superuser: `admin@admin.com` / `12345678`
- 5 Test Users (password: `password123`)
  - john.doe@example.com
  - jane.smith@example.com
  - bob.wilson@example.com
  - alice.johnson@example.com
  - charlie.brown@example.com

### 2. Seed System Settings
```bash
python manage.py seed_system_settings
```

**Creates:**
- General settings (site title, description, contact info)
- 15 social media platform links

### 3. Seed Subscriptions
```bash
python manage.py seed_subscriptions
```

**Creates:**
- 15 Features (API Access, Priority Support, Custom Branding, etc.)
- 6 Subscription Plans:
  - **Free** - $0/month (Basic features)
  - **Starter** - $9.99/month (14-day trial)
  - **Professional** - $29.99/month (Most popular, 30-day trial)
  - **Business** - $79.99/month (Advanced features)
  - **Enterprise** - $299.99/month (Full access)
  - **Professional Annual** - $287.90/year (Save 20%)

---

## Advanced Options

### Skip Specific Seeds
```bash
# Seed everything except users
python manage.py seed_all --skip-users

# Seed everything except system settings
python manage.py seed_all --skip-settings

# Seed everything except subscriptions
python manage.py seed_all --skip-subscriptions

# Combine multiple skips
python manage.py seed_all --skip-users --skip-settings
```

### Get Help
```bash
python manage.py seed_all --help
```

---

## Typical Workflow

```bash
# 1. Activate virtual environment
source venv/bin/activate

# 2. Run migrations (first time only)
python manage.py migrate

# 3. Seed all data
python manage.py seed_all

# 4. Start server
python manage.py runserver
```

---

## Notes

- ⚠️ Seed commands are **idempotent** - they won't create duplicates
- ⚠️ If data already exists, you'll see a warning but no error
- ⚠️ Safe to run multiple times

---

## Troubleshooting

**Issue:** Command not found
```bash
# Make sure you're in the project directory
cd /path/to/django_kit

# Activate virtual environment
source venv/bin/activate
```

**Issue:** Import errors
```bash
# Install dependencies first
pip install -r requirements.txt
```

**Issue:** Database errors
```bash
# Run migrations first
python manage.py migrate
```
