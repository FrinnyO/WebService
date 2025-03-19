from django.core.management import call_command
from django.core.management.base import BaseCommand

from catalog.models import Category, Product


class Command(BaseCommand):
    help = "Add products to the database"

    def handle(self, *args, **kwargs):
        Category.objects.all().delete()
        Product.objects.all().delete()
        call_command("loaddata", ["category_fixture.json", "product_fixture.json"])
        self.stdout.write(self.style.SUCCESS(f"Successfully loaded data from fixtures"))
