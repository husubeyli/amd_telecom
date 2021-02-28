from django.urls import path

from .views import (
    ProductFilterListAPIView,
    ProductImageListAPIView,
    all_product,
)


app_name = 'product_apis'



urlpatterns = [
    path('filter-api-product/', ProductFilterListAPIView.as_view(), name='api_filter_product'),
    path('filter-api-product-images/', ProductImageListAPIView.as_view(), name='filter_api_product_images'),
    path('products/', all_product, name='all_product')
]

