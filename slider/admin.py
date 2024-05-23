from django.contrib import admin
from .models import Slide
from adminsortable2.admin import SortableAdminMixin


@admin.register(Slide)
class SlideAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ('title', 'image')
