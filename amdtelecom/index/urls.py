from django.urls import path
from django.conf.urls.static import static
from .views import HomePageTemplateView

app_name = 'index'

urlpatterns = [
    path('', HomePageTemplateView.as_view(), name='home'),
]