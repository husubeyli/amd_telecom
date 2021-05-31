from django.urls import path, include
from django.conf.urls.static import static
from .import views
from .views import (
    SearchProductListView,
    ProductsListView,
    # product_filter
    # product_detail,
    ProductDetailView
)


app_name = 'product'

urlpatterns = [
    path('search/', SearchProductListView.as_view(), name='products_list_filter'),
    path('<slug:slug>/', ProductsListView.as_view(), name='products_filter'),
    path('product/<slug:slug>/', ProductDetailView.as_view(), name='product_detail'),
    # path('products/<slug:slug>/', product_filter, name='products_filter'),
    # path('product/<slug:slug>/', product_detail, name='product_detail'),
    path('api/v1.0/', include('product.api.urls')),
]