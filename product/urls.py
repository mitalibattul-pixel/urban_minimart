from django.urls import path
from . import views

urlpatterns = [
    path('admin/products/', views.product_list, name='product_list'),
    path('admin/products/add/', views.add_product, name='add_product'),
]
