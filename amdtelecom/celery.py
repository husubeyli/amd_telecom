from __future__ import absolute_import
import os
from celery import Celery
from django.conf import settings
from celery.schedules import crontab

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'amdtelecom.settings')
app = Celery('amdtelecom')

# Using a string here means the worker will not have to
# pickle the object when using Windows.
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))

# app.conf.beat_schedule = {
#     'check-new-product-daily': {
#         'task': 'new_prod_published_date',
#         'schedule': crontab(minute='2')
#     },
# }

# app.conf.broker_transport_options = {
#     'max_retries': 3,
#     'interval_start': 0,
#     'interval_step': 0.2,
#     'interval_max': 0.2,
# }


# Procfile
# celery -A amdtelecom worker -l info
# celery -A amdtelecom worker --beat --scheduler django --loglevel=info

