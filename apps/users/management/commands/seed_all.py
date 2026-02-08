from django.core.management.base import BaseCommand
from django.core.management import call_command
from django.db import transaction


class Command(BaseCommand):
    help = 'Seed all data in the database (runs all seed commands)'

    def add_arguments(self, parser):
        parser.add_argument(
            '--skip-users',
            action='store_true',
            help='Skip seeding users',
        )
        parser.add_argument(
            '--skip-settings',
            action='store_true',
            help='Skip seeding system settings',
        )
        parser.add_argument(
            '--skip-subscriptions',
            action='store_true',
            help='Skip seeding subscription plans',
        )

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('=' * 60))
        self.stdout.write(self.style.SUCCESS('🌱 SEED ALL - Starting database seeding...'))
        self.stdout.write(self.style.SUCCESS('=' * 60))
        
        seed_commands = []
        
        # Add seed commands based on options
        if not options['skip_users']:
            seed_commands.append(('seed_users', 'Users & Profiles'))
        
        if not options['skip_settings']:
            seed_commands.append(('seed_system_settings', 'System Settings & Social Media'))
        
        if not options['skip_subscriptions']:
            seed_commands.append(('seed_subscriptions', 'Subscription Plans & Features'))
        
        # Run all seed commands
        total_commands = len(seed_commands)
        success_count = 0
        failed_commands = []
        
        for idx, (command_name, description) in enumerate(seed_commands, 1):
            self.stdout.write(f'\n[{idx}/{total_commands}] Running: {description}...')
            self.stdout.write('-' * 60)
            
            try:
                call_command(command_name)
                success_count += 1
                self.stdout.write(self.style.SUCCESS(f'✅ {description} - COMPLETED'))
            except Exception as e:
                failed_commands.append((description, str(e)))
                self.stdout.write(self.style.ERROR(f'❌ {description} - FAILED: {str(e)}'))
        
        # Summary
        self.stdout.write('\n' + '=' * 60)
        self.stdout.write(self.style.SUCCESS('📊 SEEDING SUMMARY'))
        self.stdout.write('=' * 60)
        self.stdout.write(f'Total commands: {total_commands}')
        self.stdout.write(self.style.SUCCESS(f'Successful: {success_count}'))
        
        if failed_commands:
            self.stdout.write(self.style.ERROR(f'Failed: {len(failed_commands)}'))
            self.stdout.write('\nFailed commands:')
            for desc, error in failed_commands:
                self.stdout.write(self.style.ERROR(f'  - {desc}: {error}'))
        else:
            self.stdout.write(self.style.SUCCESS('\n🎉 All data seeded successfully!'))
        
        self.stdout.write('=' * 60)
