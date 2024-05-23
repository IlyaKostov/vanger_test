from django.db import models
from filer.fields.image import FilerImageField


class Slide(models.Model):
    title = models.CharField(max_length=100, verbose_name='название')
    image = FilerImageField(related_name='slide_image', on_delete=models.CASCADE, verbose_name='изображение')

    class Meta:
        ordering = ['id']
        verbose_name = 'Слайд'
        verbose_name_plural = 'Слайды'

    def __str__(self):
        return self.title
