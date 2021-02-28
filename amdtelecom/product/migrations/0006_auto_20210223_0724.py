# Generated by Django 3.1.4 on 2021-02-23 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_auto_20210223_0722'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product_details_property_name',
            name='title',
        ),
        migrations.RemoveField(
            model_name='product_details_property_value',
            name='content',
        ),
        migrations.RemoveField(
            model_name='product_details_property_value',
            name='file',
        ),
        migrations.AddField(
            model_name='product_details_property_name',
            name='content',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Content'),
        ),
        migrations.AddField(
            model_name='product_details_property_name',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='products_files', verbose_name='File'),
        ),
        migrations.AddField(
            model_name='product_details_property_value',
            name='title',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Title'),
        ),
        migrations.AlterModelTable(
            name='product_details_property_name',
            table='Property name',
        ),
        migrations.AlterModelTable(
            name='product_details_property_value',
            table='Property value ',
        ),
    ]