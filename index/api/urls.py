from django.views.decorators.csrf import csrf_exempt
from django.urls import path

from .views import SubscribeView


app_name = 'index_apis'


subscriber_create = csrf_exempt(SubscribeView.as_view())

urlpatterns = [
    path('subscribe/', subscriber_create, name='subscribe_api'),
   
]

