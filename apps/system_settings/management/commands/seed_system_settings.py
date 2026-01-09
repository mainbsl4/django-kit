from django.core.management.base import BaseCommand
from django.db import transaction
from apps.system_settings.models import GeneralSetting, SocialMedia


class Command(BaseCommand):
    help = 'Seed database with system settings and social media links'

    def handle(self, *args, **options):
        self.stdout.write('Seeding system settings...')
        
        with transaction.atomic():
            # Create General Settings (only one instance)
            if not GeneralSetting.objects.exists():
                general_setting = GeneralSetting.objects.create(
                    industry_name='Django Kit',
                    site_title='Django Kit - Modern Web Framework',
                    description='A powerful Django starter kit with REST API, JWT authentication, and modern admin interface. Built for rapid development and scalability.',
                    address='123 Tech Street, Silicon Valley, CA 94025, USA',
                    phone='+1 (555) 123-4567',
                    email='info@djangokit.com'
                )
                self.stdout.write(self.style.SUCCESS('✓ Created General Settings'))
            else:
                self.stdout.write(self.style.WARNING('⚠ General Settings already exists'))

            # Create Social Media Links
            social_media_data = [
                {
                    'platform_name': 'Facebook',
                    'profile_url': 'https://www.facebook.com/djangokit'
                },
                {
                    'platform_name': 'Twitter',
                    'profile_url': 'https://twitter.com/djangokit'
                },
                {
                    'platform_name': 'Instagram',
                    'profile_url': 'https://www.instagram.com/djangokit'
                },
                {
                    'platform_name': 'LinkedIn',
                    'profile_url': 'https://www.linkedin.com/company/djangokit'
                },
                {
                    'platform_name': 'YouTube',
                    'profile_url': 'https://www.youtube.com/@djangokit'
                },
                {
                    'platform_name': 'GitHub',
                    'profile_url': 'https://github.com/djangokit'
                },
                {
                    'platform_name': 'Discord',
                    'profile_url': 'https://discord.gg/djangokit'
                },
                {
                    'platform_name': 'Reddit',
                    'profile_url': 'https://www.reddit.com/r/djangokit'
                },
                {
                    'platform_name': 'TikTok',
                    'profile_url': 'https://www.tiktok.com/@djangokit'
                },
                {
                    'platform_name': 'Pinterest',
                    'profile_url': 'https://www.pinterest.com/djangokit'
                },
                {
                    'platform_name': 'Telegram',
                    'profile_url': 'https://t.me/djangokit'
                },
                {
                    'platform_name': 'WhatsApp',
                    'profile_url': 'https://wa.me/15551234567'
                },
                {
                    'platform_name': 'Snapchat',
                    'profile_url': 'https://www.snapchat.com/add/djangokit'
                },
                {
                    'platform_name': 'Medium',
                    'profile_url': 'https://medium.com/@djangokit'
                },
                {
                    'platform_name': 'Twitch',
                    'profile_url': 'https://www.twitch.tv/djangokit'
                }
            ]

            created_count = 0
            for social_data in social_media_data:
                if not SocialMedia.objects.filter(platform_name=social_data['platform_name']).exists():
                    SocialMedia.objects.create(**social_data)
                    created_count += 1
                    self.stdout.write(self.style.SUCCESS(f'✓ Created social media: {social_data["platform_name"]}'))
                else:
                    self.stdout.write(self.style.WARNING(f'⚠ Social media {social_data["platform_name"]} already exists'))

        self.stdout.write(self.style.SUCCESS(f'\n✅ Seeding completed! Created {created_count} social media links.'))
        self.stdout.write(self.style.SUCCESS('\nNote: Logo and favicon images need to be uploaded manually through the admin panel.'))
