from django.core.management.base import BaseCommand

from elostars.main.models import Picture


class Command(BaseCommand):
    help = "Completely reset scores."

    def handle(self, *args, **kwargs):
        Picture.objects.update(wins=0, losses=0, score=1600)





