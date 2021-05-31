# Generated by Django 3.1.4 on 2021-03-18 22:47

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product', '0001_initial'),
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True, verbose_name='name')),
                ('surname', models.CharField(blank=True, max_length=50, null=True, verbose_name='surname')),
                ('email', models.EmailField(blank=True, max_length=50, null=True, verbose_name='email')),
                ('tel_number', models.CharField(blank=True, error_messages={'required': 'Mobil nomre 10 reqemli olmalidir'}, max_length=10, null=True, validators=[django.core.validators.MinLengthValidator(10)], verbose_name='telefon')),
                ('complete', models.BooleanField(default=False, verbose_name='Complete')),
                ('transaction_id', models.CharField(max_length=100, null=True, verbose_name='Transaction id')),
                ('message', models.TextField(blank=True, verbose_name='Comment')),
                ('status', models.BooleanField(default=True, verbose_name='Status')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='account.customer')),
            ],
            options={
                'verbose_name': 'Order',
                'verbose_name_plural': 'Orders',
                'db_table': 'order',
            },
        ),
        migrations.CreateModel(
            name='ShippingAddress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=200, verbose_name='Adress')),
                ('city', models.CharField(max_length=200, verbose_name='City')),
                ('state', models.CharField(max_length=200, verbose_name='State')),
                ('zipcode', models.CharField(max_length=200, verbose_name='Zipcode')),
                ('status', models.BooleanField(default=True, verbose_name='Status')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='account.customer')),
                ('order', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='order.order')),
            ],
            options={
                'verbose_name': 'Shipping address',
                'verbose_name_plural': 'Shipping addresses',
                'db_table': 'shipping_address',
                'ordering': ('created_at',),
            },
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(blank=True, default=0, null=True, verbose_name='Quantity')),
                ('status', models.BooleanField(default=True, verbose_name='Status')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='account.customer')),
                ('order', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='order.order')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='order_items', to='product.product')),
            ],
            options={
                'verbose_name': 'Order items',
                'verbose_name_plural': 'Order items',
                'db_table': 'order_item',
                'ordering': ('created_at',),
            },
        ),
    ]