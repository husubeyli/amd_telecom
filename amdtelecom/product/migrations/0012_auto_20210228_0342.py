# Generated by Django 3.1.4 on 2021-02-27 23:42

from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0011_auto_20210228_0000'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product_images',
            name='image',
            field=django_resized.forms.ResizedImageField(crop=None, force_format=None, keep_meta=True, quality=75, size=[800, 500], upload_to='product_images'),
        ),
    ]
