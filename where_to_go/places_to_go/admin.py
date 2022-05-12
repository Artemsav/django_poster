from django.contrib import admin
from places_to_go.models import Location, LocationImage


class LocationImageInline(admin.TabularInline):
    model = LocationImage


class LocationAdmin(admin.ModelAdmin):
    inlines = [
        LocationImageInline,
    ]


admin.site.register(Location, LocationAdmin)
admin.site.register(LocationImage)
