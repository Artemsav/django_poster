from django.shortcuts import render
from places_to_go.models import Location, LocationImage
from django.urls import reverse
from where_to_go import places_view


def serialize_location(location):
    return {
        "type": "Feature",
        "geometry": {
            "type": "Point",
            "coordinates": [location.lon, location.lat]
          },
        "properties": {
            "title": location.title,
            "placeId": location.pk,
            "detailsUrl": reverse(places_view.places, args=[f'{location.id}'])
          }
        }


def index(request):
    locations = Location.objects.all()
    context = {
        'places_geojson':    {
            "type": "FeatureCollection",
            "features": [serialize_location(location) for location in locations]
            }
    }
    return render(request, 'index.html', context)
