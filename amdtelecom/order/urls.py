from django.urls import path
from . import views
from .views import CheckoutView

app_name='order'

urlpatterns = [
    path('deletefromcart/<int:id>/', views.deletefromcart, name='deletefromcart'),
    path('cart/', views.cart, name="cart"),
    path('checkout/', CheckoutView.as_view(), name="checkout"),

]