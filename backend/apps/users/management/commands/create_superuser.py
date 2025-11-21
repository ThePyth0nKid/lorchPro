"""
Management command to create a default superuser
"""
from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Create default superuser'

    def handle(self, *args, **kwargs):
        User = get_user_model()
        
        if not User.objects.filter(email='admin@lorchpro.com').exists():
            User.objects.create_superuser(
                email='admin@lorchpro.com',
                username='admin',
                password='admin123',
                first_name='Admin',
                last_name='User',
                rolle='ADMIN'
            )
            self.stdout.write(self.style.SUCCESS('Superuser created: admin@lorchpro.com / admin123'))
        else:
            self.stdout.write(self.style.WARNING('Superuser already exists'))

