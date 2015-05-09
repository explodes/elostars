import sys

from django.core.management.base import BaseCommand
from django.apps import apps

from elostars.lib.models import AutoImageSizingModel


class Command(BaseCommand):
    help = "Completely rebuild any generated images."

    def handle(self, *args, **kwargs):

        for model in apps.get_models():
            if issubclass(model, AutoImageSizingModel):
                name = model._meta.verbose_name.title()
                plural_lower = model._meta.verbose_name_plural.title().lower()

                qs = model._default_manager.all()

                count = len(qs)
                print >> sys.stdout, "Rebuilding", count, plural_lower

                for index, item in enumerate(qs):
                    num = index + 1
                    print >> sys.stdout, name, num, "of", count,
                    sys.stdout.flush()

                    item.clear_images()
                    item.save()

                    print >> sys.stdout, "...done"
                    sys.stdout.flush()

                print >> sys.stdout, "Completed rebuild of", plural_lower



