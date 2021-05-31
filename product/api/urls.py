from django.urls import path

from .views import (
    ProductFilterListAPIView,
    ProductImageListAPIView,
    all_product,
    ProductMarkaListAPIView,
    SearchListAPIView,
)


app_name = 'product_apis'



urlpatterns = [
    path('filter-api-product/', ProductFilterListAPIView.as_view(), name='filter_api_product'),
    # path('filter-api-product-images/', ProductImageListAPIView.as_view(), name='filter_api_product_images'),
    # path('filter-api-product-markas/', ProductMarkaListAPIView.as_view(), name='filter_api_product_markas'),
    # path('products/<str:value>/', all_product, name='all_product'),
    # path('search/<str:title>/', SearchListAPIView.as_view(), name='all_product'),
    path('search/', SearchListAPIView.as_view(), name='all_product')

]

