from django.urls import path
from . import views
# from .views import CheckoutView

# from .views import checkout

app_name='order'

urlpatterns = [
    # path('deletefromcart/<int:id>/', views.deletefromcart, name='deletefromcart'),
    path('order/cart/', views.cart, name="cart"),
    path('order/checkout/', views.checkout, name="checkout"),
    # path('checkout/', checkout, name="checkout"),

]