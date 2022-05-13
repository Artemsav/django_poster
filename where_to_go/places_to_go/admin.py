from django.contrib import admin
from places_to_go.models import Location, LocationImage
from django.utils.html import format_html
from django.utils.safestring import mark_safe
from adminsortable2.admin import SortableAdminMixin


class LocationImageInline(SortableAdminMixin, admin.TabularInline):
    model = LocationImage
    readonly_fields = ['preview_image', ]
    extra: int = 2

    def preview_image(self, obj):
        return format_html(
            '<img src={} height ={} />',
            mark_safe(obj.image.url),
            200)


@admin.register(Location)
class LocationAdmin(SortableAdminMixin, admin.ModelAdmin):
    inlines = [
        LocationImageInline,
    ]
