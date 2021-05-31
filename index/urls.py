from django.urls import path
from django.conf.urls.static import static
from .views import autocomplete, home_page
app_name = 'index'

urlpatterns = [
    # path('', HomePageTemplateView.as_view(), name='home'),
    path('', home_page, name='home'),
    path('autocomplete', autocomplete, name='autocomplete'),
]