from django.core.management.base import BaseCommand, CommandError
import requests
from places_to_go.models import Location, LocationImage
from django.core.files.base import ContentFile
import os


class Command(BaseCommand):
    help = 'Load places describtion and images to database'

    def add_arguments(self, parser):
        parser.add_argument('place_url')

    def handle(self, *args, **options):
        decoded_respond = requests.get(options['place_url']).json()
        location, created = Location.objects.get_or_create(
            title=decoded_respond['title'],
            short_describtion=decoded_respond['description_short'],
            long_describtion=decoded_respond['description_long'],
            lat=decoded_respond['coordinates']['lat'],
            lon=decoded_respond['coordinates']['lng'],
        )
        for img_url in decoded_respond['imgs']:
            img_request = requests.get(img_url)
            img = ContentFile(img_request.content)
            _, img_name = os.path.split(img_url)
            image_obj, created = LocationImage.objects.get_or_create(
                title=img_name,
                location=location
            )
            image_obj.image.save(img_name, img, save=True)
        self.stdout.write(self.style.SUCCESS(f'Location is {created}'))
