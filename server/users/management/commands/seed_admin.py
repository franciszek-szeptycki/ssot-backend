import os
from django.core.management.base import BaseCommand
from dotenv import load_dotenv


class Command(BaseCommand):
    help = 'Generate admin user if not exists.'

    def handle(self, *args, **kwargs):
        load_dotenv()

        admin_username = os.getenv('ADMIN_USERNAME')
        admin_email = os.getenv('ADMIN_EMAIL')
        admin_password = os.getenv('ADMIN_PASSWORD')

        from django.apps import apps
        User = apps.get_model('auth', 'User')

        if not User.objects.filter(username=admin_username).exists():
            User.objects.create_superuser(admin_username, admin_email, admin_password)
            self.stdout.write(self.style.SUCCESS('Admin user created successfully'))
        else:
            admin_user = User.objects.get(username=admin_username)
            admin_user.set_password(admin_password)
            admin_user.save()
            self.stdout.write(self.style.SUCCESS('Admin user updated successfully'))
