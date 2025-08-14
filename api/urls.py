from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.ProductListAPIView.as_view(), name='product_list'),
    path('products/info/', views.product_info, name='product_info'),
    path('products/<int:pk>', views.product_detail, name='product_detail'),
    path('orders/', views.order_list, name='order_list'),
]
