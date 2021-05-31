from __future__ import absolute_import, unicode_literals
from celery import shared_task
from datetime import datetime, date
from django.utils import timezone

from product.models import Product
from amdtelecom.celery import app


# @shared_task
# def new_prod_published_date():
#     products = Product.objects.filter(is_new_expired__lte=timezone.datetime.today()).update(is_new = False)


@app.task()
def changed_is_new(prod_id):
    print('changed_is_new is working')
    product = Product.objects.filter(id=prod_id).filter(is_new_expired__lte=timezone.datetime.today()).update(is_new = False)
