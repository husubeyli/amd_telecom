from django.urls import path, include
from .import views
from .views import (
    ProductListView, 
    # CategoryListView,
    ProductsFilterListView,
    # product_filter
    # product_detail,
    ProductDetailView
)
from django.conf.urls.static import static

app_name = 'product'

urlpatterns = [
    # path('', CategoryListView.as_view(), name='amd-home'),
    path('products/', ProductListView.as_view(), name='products_list'),
    path('products/<slug:slug>/', ProductsFilterListView.as_view(), name='products_filter'),
    # path('products/<slug:slug>/', product_filter, name='products_filter'),
    # path('', views.home_page, name='amd-home'),
    path('product/<slug:slug>/', ProductDetailView.as_view(), name='product_detail'),
    # path('products/filter/<int:pk>/', views.product_detail, name='products_detail'),
    # path('products/', views.about, name='amd-about'),
    path('api/v1.0/', include('product.api.urls')),
]