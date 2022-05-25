from django.contrib import admin
from places_to_go.models import Location, LocationImage
from django.utils.html import format_html
from django.utils.safestring import mark_safe
from adminsortable2.admin import SortableAdminMixin, SortableInlineAdminMixin


class LocationImageInline(SortableInlineAdminMixin, admin.TabularInline):
    model = LocationImage
    readonly_fields = ['preview_image', ]

    def preview_image(self, obj):
        return format_html(
            '<img src={} height ={} />',
            mark_safe(obj.image.url),
            200)


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    search_fields = ['title']
    inlines = [
        LocationImageInline,
    ]
