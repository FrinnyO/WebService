from django.core.management import call_command
from django.core.management.base import BaseCommand

from blog.models import Article


class Command(BaseCommand):
    help = "Add products to the database"

    def handle(self, *args, **kwargs):
        Article.objects.all().delete()

        call_command("loaddata", ["article_fixture.json"])
        self.stdout.write(self.style.SUCCESS("Successfully loaded data from fixtures"))
