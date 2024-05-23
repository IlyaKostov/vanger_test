from django import template
from easy_thumbnails.files import get_thumbnailer

register = template.Library()


@register.filter
def small_image_url(image_field):
    thumbnail_options = {'size': (165, 165), 'crop': 'smart'}
    if not image_field:
        return ''
    return get_thumbnailer(image_field).get_thumbnail(thumbnail_options).url
