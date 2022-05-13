from django.contrib import admin
from places_to_go.models import Location, LocationImage
from django.utils.html import format_html
from django.utils.safestring import mark_safe


class LocationImageInline(admin.TabularInline):
    model = LocationImage
    readonly_fields = ['preview_image',]

    def preview_image(self, obj):
        return format_html(
            '<img src={} height ={} />',
            mark_safe(obj.image.url),
            200)


class LocationAdmin(admin.ModelAdmin):
    inlines = [
        LocationImageInline,
    ]


admin.site.register(Location, LocationAdmin)
admin.site.register(LocationImage)
