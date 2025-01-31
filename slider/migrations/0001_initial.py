# Generated by Django 4.1 on 2024-05-23 05:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import filer.fields.image


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.FILER_IMAGE_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Slide',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='название')),
                ('image', filer.fields.image.FilerImageField(on_delete=django.db.models.deletion.CASCADE, related_name='slide_image', to=settings.FILER_IMAGE_MODEL, verbose_name='изображение')),
            ],
            options={
                'ordering': ['id'],
            },
        ),
    ]
