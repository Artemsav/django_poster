from django.shortcuts import render
from places_to_go.models import Location, LocationImage


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
            "detailsUrl": "https://raw.githubusercontent.com/devmanorg/where-to-go-frontend/master/places/moscow_legends.json"
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
