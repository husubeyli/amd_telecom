from django.urls import path
from . import views

urlpatterns = [
    path('', views.apiOverview, name="api-overview"),
    path('orderItem-list/', views.all_order_items, name="orderItem-list"),
    path('orderItem-list/<str:pk>/', views.get_order_item, name="orderItem-detail"),
    path('orderItem-id/<str:pk>/', views.get_order_items_id, name="orderItem-get-id"),
    path('orderItem-create/', views.create_order_item, name="orderItem-create"),
    path('orderItem-update/<str:pk>/', views.update_order_item, name="orderItem-update"),
    path('orderItem-patch/<str:pk>/', views.patch_order_item, name="orderItem-patch"),
    path('orderItem-delete/<str:pk>/', views.delete_order_item, name="orderItem-delete"),
    path('orderItem-count/', views.get_order_items_count, name="orderItem-count"),
    path('orderItem-listbypaginator/', views.ApiOrderItemsView.as_view(), name="orderItem-paginator"),
]