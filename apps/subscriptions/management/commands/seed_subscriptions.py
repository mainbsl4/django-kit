from django.core.management.base import BaseCommand
from django.db import transaction
from apps.subscriptions.models import Feature, Plan
from decimal import Decimal


class Command(BaseCommand):
    help = 'Seed database with subscription plans and features'

    def handle(self, *args, **options):
        self.stdout.write('Seeding subscription plans and features...')
        
        with transaction.atomic():
            # Create Features
            features_data = [
                {
                    'name': 'Basic Support',
                    'code': 'basic-support',
                    'description': 'Email support during business hours'
                },
                {
                    'name': 'Priority Support',
                    'code': 'priority-support',
                    'description': '24/7 priority email and chat support'
                },
                {
                    'name': 'Phone Support',
                    'code': 'phone-support',
                    'description': 'Direct phone line to support team'
                },
                {
                    'name': 'API Access',
                    'code': 'api-access',
                    'description': 'Full REST API access'
                },
                {
                    'name': 'Advanced Analytics',
                    'code': 'advanced-analytics',
                    'description': 'Detailed reports and insights'
                },
                {
                    'name': 'Custom Branding',
                    'code': 'custom-branding',
                    'description': 'Add your own logo and colors'
                },
                {
                    'name': 'Team Collaboration',
                    'code': 'team-collaboration',
                    'description': 'Share and collaborate with team members'
                },
                {
                    'name': 'Unlimited Projects',
                    'code': 'unlimited-projects',
                    'description': 'Create unlimited number of projects'
                },
                {
                    'name': 'Advanced Security',
                    'code': 'advanced-security',
                    'description': 'Two-factor authentication and SSO'
                },
                {
                    'name': 'Data Export',
                    'code': 'data-export',
                    'description': 'Export your data anytime'
                },
                {
                    'name': 'Webhooks',
                    'code': 'webhooks',
                    'description': 'Integrate with external services'
                },
                {
                    'name': 'Custom Integrations',
                    'code': 'custom-integrations',
                    'description': 'Build custom integrations'
                },
                {
                    'name': 'Dedicated Account Manager',
                    'code': 'account-manager',
                    'description': 'Personal account manager'
                },
                {
                    'name': 'SLA Guarantee',
                    'code': 'sla-guarantee',
                    'description': '99.9% uptime guarantee'
                },
                {
                    'name': 'Onboarding Training',
                    'code': 'onboarding-training',
                    'description': 'Personalized onboarding sessions'
                },
            ]

            created_features = {}
            feature_count = 0
            
            for feature_data in features_data:
                feature, created = Feature.objects.get_or_create(
                    code=feature_data['code'],
                    defaults={
                        'name': feature_data['name'],
                        'description': feature_data['description'],
                        'is_active': True
                    }
                )
                created_features[feature_data['code']] = feature
                if created:
                    feature_count += 1
                    self.stdout.write(self.style.SUCCESS(f'✓ Created feature: {feature_data["name"]}'))
                else:
                    self.stdout.write(self.style.WARNING(f'⚠ Feature {feature_data["name"]} already exists'))

            # Create Plans
            plans_data = [
                {
                    'name': 'Free',
                    'slug': 'free',
                    'description': 'Perfect for trying out the platform',
                    'price': Decimal('0.00'),
                    'billing_period': 'MONTHLY',
                    'trial_period_days': 0,
                    'is_popular': False,
                    'display_order': 1,
                    'features': ['basic-support', 'data-export']
                },
                {
                    'name': 'Starter',
                    'slug': 'starter',
                    'description': 'Great for individuals and small projects',
                    'price': Decimal('9.99'),
                    'billing_period': 'MONTHLY',
                    'trial_period_days': 14,
                    'is_popular': False,
                    'display_order': 2,
                    'features': [
                        'basic-support',
                        'api-access',
                        'team-collaboration',
                        'data-export'
                    ]
                },
                {
                    'name': 'Professional',
                    'slug': 'professional',
                    'description': 'Most popular for growing businesses',
                    'price': Decimal('29.99'),
                    'billing_period': 'MONTHLY',
                    'trial_period_days': 30,
                    'is_popular': True,
                    'display_order': 3,
                    'features': [
                        'priority-support',
                        'api-access',
                        'advanced-analytics',
                        'custom-branding',
                        'team-collaboration',
                        'unlimited-projects',
                        'data-export',
                        'webhooks'
                    ]
                },
                {
                    'name': 'Business',
                    'slug': 'business',
                    'description': 'Advanced features for teams',
                    'price': Decimal('79.99'),
                    'billing_period': 'MONTHLY',
                    'trial_period_days': 30,
                    'is_popular': False,
                    'display_order': 4,
                    'features': [
                        'priority-support',
                        'phone-support',
                        'api-access',
                        'advanced-analytics',
                        'custom-branding',
                        'team-collaboration',
                        'unlimited-projects',
                        'advanced-security',
                        'data-export',
                        'webhooks',
                        'custom-integrations'
                    ]
                },
                {
                    'name': 'Enterprise',
                    'slug': 'enterprise',
                    'description': 'Custom solutions for large organizations',
                    'price': Decimal('299.99'),
                    'billing_period': 'MONTHLY',
                    'trial_period_days': 30,
                    'is_popular': False,
                    'display_order': 5,
                    'features': [
                        'priority-support',
                        'phone-support',
                        'api-access',
                        'advanced-analytics',
                        'custom-branding',
                        'team-collaboration',
                        'unlimited-projects',
                        'advanced-security',
                        'data-export',
                        'webhooks',
                        'custom-integrations',
                        'account-manager',
                        'sla-guarantee',
                        'onboarding-training'
                    ]
                },
                {
                    'name': 'Professional Annual',
                    'slug': 'professional-annual',
                    'description': 'Professional plan with annual billing (save 20%)',
                    'price': Decimal('287.90'),
                    'billing_period': 'YEARLY',
                    'trial_period_days': 30,
                    'is_popular': False,
                    'display_order': 6,
                    'features': [
                        'priority-support',
                        'api-access',
                        'advanced-analytics',
                        'custom-branding',
                        'team-collaboration',
                        'unlimited-projects',
                        'data-export',
                        'webhooks'
                    ]
                },
            ]

            plan_count = 0
            for plan_data in plans_data:
                feature_codes = plan_data.pop('features')
                
                plan, created = Plan.objects.get_or_create(
                    slug=plan_data['slug'],
                    defaults=plan_data
                )
                
                if created:
                    # Add features to the plan
                    for feature_code in feature_codes:
                        if feature_code in created_features:
                            plan.features.add(created_features[feature_code])
                    
                    plan_count += 1
                    self.stdout.write(self.style.SUCCESS(
                        f'✓ Created plan: {plan_data["name"]} - ${plan_data["price"]}/{plan_data["billing_period"]}'
                    ))
                else:
                    self.stdout.write(self.style.WARNING(f'⚠ Plan {plan_data["name"]} already exists'))

        self.stdout.write(self.style.SUCCESS(f'\n✅ Seeding completed!'))
        self.stdout.write(self.style.SUCCESS(f'   Created {feature_count} new features'))
        self.stdout.write(self.style.SUCCESS(f'   Created {plan_count} new plans'))
        
        # Display summary
        self.stdout.write('\n📋 Available Plans:')
        for plan in Plan.objects.all().order_by('display_order'):
            self.stdout.write(f'   • {plan.name}: ${plan.price}/{plan.get_billing_period_display()}')
