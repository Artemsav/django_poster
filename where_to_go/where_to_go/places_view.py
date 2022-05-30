from places_to_go.models import Location
from django.shortcuts import get_object_or_404
from django.http import JsonResponse


class UTF8JsonResponse(JsonResponse):
    def __init__(self, *args, json_dumps_params=None, **kwargs):
        json_dumps_params = {"ensure_ascii": False, **(json_dumps_params or {})}
        super().__init__(*args, json_dumps_params=json_dumps_params, **kwargs)


def places(request, post_id):
    location = get_object_or_404(Location, pk=post_id)
    location_img = location.images.all()
    location_info = {
      'title': location.title,
      'imgs': [
        image.image.url for image in location_img
        ],
      'description_short': location.short_describtion,
      'description_long': location.long_describtion,
      'coordinates': {
        'lat': location.lat,
        'lng': location.lon
      }
    }
    return UTF8JsonResponse(location_info, json_dumps_params={'indent': 4})
