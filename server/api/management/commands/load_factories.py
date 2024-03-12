from django.core.management.base import BaseCommand
from django.db import transaction
from api.factories import AreaFactory, ProjectFactory, SectionFactory, QuoteFactory, TaskFactory
from django.core.management import call_command
from django.apps import apps


class Command(BaseCommand):
    help = 'Load initial data using factories for testing purposes'

    def handle(self, *args, **kwargs):
        with transaction.atomic():
            self.stdout.write("Loading initial data...")

            all_models = apps.get_models()
            for model in all_models:
                model.objects.all().delete()

            self.stdout.write("Deleting all data...")

            call_command("seed_admin")

            # Create instances using factories
            areas = AreaFactory.create_batch(5)
            projects = ProjectFactory.create_batch(5)
            sections = SectionFactory.create_batch(5)
            quotes = QuoteFactory.create_batch(5)
            tasks = TaskFactory.create_batch(5)

            self.stdout.write(self.style.SUCCESS("Initial data loaded successfully"))
