from django.core.management.base import BaseCommand
from ...models import Photo


class Command(BaseCommand):
    help = "Get all photos"

    def handle(self, *args, **options):
        photos = Photo.objects.all()
        photos_list = []
        for photo in photos:
            photos_list.append(f"id: {photo.id} {photo}")
        photos_str = "\n".join(photos_list)
        self.stdout.write(f"{photos_str}")