from django.contrib import admin
from django.utils.html import format_html

from .models import Slide
from adminsortable2.admin import SortableAdminMixin


@admin.register(Slide)
class SlideAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ('title', 'order', 'image_preview')
    readonly_fields = ('order', 'image_preview')

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="max-height: 75px; max-width: 75px;" />'.format(obj.image.url))
        else:
            return 'Нет картинки'

    image_preview.short_description = 'Превью картинки'
