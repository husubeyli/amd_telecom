from django.urls import path, include
from .views import ContactCreateView



app_name = 'contact'



urlpatterns = [
    path('us/', ContactCreateView.as_view(), name="contact")
]