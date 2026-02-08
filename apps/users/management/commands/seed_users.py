from django.core.management.base import BaseCommand
from django.db import transaction
from apps.users.models import User, UserProfile


class Command(BaseCommand):
    help = 'Seed database with test users and superuser'

    def handle(self, *args, **options):
        self.stdout.write('Seeding users...')
        
        with transaction.atomic():
            # Create superuser
            if not User.objects.filter(email='admin@admin.com').exists():
                admin = User.objects.create_superuser(
                    email='admin@admin.com',
                    password='12345678'
                )
                UserProfile.objects.create(
                    user=admin,
                    first_name='Admin',
                    last_name='User',
                    bio='System Administrator',
                    location='Head Office'
                )
                self.stdout.write(self.style.SUCCESS('✓ Created superuser: admin@admin.com'))
            else:
                self.stdout.write(self.style.WARNING('⚠ Superuser admin@admin.com already exists'))

            # Create test users
            test_users = [
                {
                    'email': 'john.doe@example.com',
                    'password': 'password123',
                    'profile': {
                        'first_name': 'John',
                        'last_name': 'Doe',
                        'bio': 'Software Developer with 5 years experience',
                        'location': 'New York, USA',
                        'contact_number': '+1234567890'
                    }
                },
                {
                    'email': 'jane.smith@example.com',
                    'password': 'password123',
                    'profile': {
                        'first_name': 'Jane',
                        'last_name': 'Smith',
                        'bio': 'UI/UX Designer passionate about user experience',
                        'location': 'London, UK',
                        'contact_number': '+4412345678'
                    }
                },
                {
                    'email': 'bob.wilson@example.com',
                    'password': 'password123',
                    'profile': {
                        'first_name': 'Bob',
                        'last_name': 'Wilson',
                        'bio': 'Product Manager with startup experience',
                        'location': 'San Francisco, USA',
                        'contact_number': '+1987654321'
                    }
                },
                {
                    'email': 'alice.johnson@example.com',
                    'password': 'password123',
                    'profile': {
                        'first_name': 'Alice',
                        'last_name': 'Johnson',
                        'bio': 'Data Scientist specializing in ML',
                        'location': 'Berlin, Germany',
                        'contact_number': '+4930123456'
                    }
                },
                {
                    'email': 'charlie.brown@example.com',
                    'password': 'password123',
                    'profile': {
                        'first_name': 'Charlie',
                        'last_name': 'Brown',
                        'bio': 'DevOps Engineer and cloud enthusiast',
                        'location': 'Toronto, Canada',
                        'contact_number': '+1416555000'
                    }
                },
            ]

            created_count = 0
            for user_data in test_users:
                if not User.objects.filter(email=user_data['email']).exists():
                    user = User.objects.create_user(
                        email=user_data['email'],
                        password=user_data['password']
                    )
                    UserProfile.objects.create(
                        user=user,
                        **user_data['profile']
                    )
                    created_count += 1
                    self.stdout.write(self.style.SUCCESS(f'✓ Created user: {user_data["email"]}'))
                else:
                    self.stdout.write(self.style.WARNING(f'⚠ User {user_data["email"]} already exists'))

        self.stdout.write(self.style.SUCCESS(f'\n✅ Seeding completed! Created {created_count} new test users.'))
        self.stdout.write(self.style.SUCCESS('\nSuperuser credentials:'))
        self.stdout.write(self.style.SUCCESS('  Email: admin@admin.com'))
        self.stdout.write(self.style.SUCCESS('  Password: 12345678'))
