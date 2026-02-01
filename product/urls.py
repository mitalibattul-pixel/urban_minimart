from django.urls import path
from . import views
app_name = 'product'
urlpatterns = [
    path('brands/', views.brand_list, name='brand_list'),
    path('brands/add/', views.brand_add, name='brand_add'),
    path('brands/edit/<int:pk>/', views.brand_edit, name='brand_edit'),
    path('brands/delete/<int:pk>/', views.brand_delete, name='brand_delete'),
    path('category/', views.category_list, name='category_list'),
    path('category/add/', views.category_add, name='category_add'),
    path('category/edit/<int:id>/', views.category_edit, name='category_edit'),
    path('category/delete/<int:id>/', views.category_delete, name='category_delete'),
    path('subcategories/', views.subcategory_list, name='subcategory_list'),
    path('subcategories/add/', views.subcategory_add, name='subcategory_add'),
    path('subcategories/edit/<int:id>/', views.subcategory_edit, name='subcategory_edit'),
    path('subcategories/delete/<int:id>/', views.subcategory_delete, name='subcategory_delete'),
    path('units/', views.unit_list, name='unit_list'),
    path('units/add/', views.unit_add, name='unit_add'),
    path('units/edit/<int:id>/', views.unit_edit, name='unit_edit'),
    path('units/delete/<int:id>/', views.unit_delete, name='unit_delete'),
    path('products/', views.product_list, name='product_list'),
    path('products/add/', views.product_add, name='product_add'),
    path('products/edit/<int:pk>/', views.product_edit, name='product_edit'),
    path('products/delete/<int:pk>/', views.product_delete, name='product_delete'),
    path('batches/', views.batch_list, name='batch_list'),
    path('batches/add/', views.batch_add, name='batch_add'),
    path('batches/edit/<int:id>/', views.batch_edit, name='batch_edit'),
    path('batches/delete/<int:id>/', views.batch_delete, name='batch_delete'),
    path('product/<int:pk>/images/add/', views.add_product_image, name='add_product_image'),
    path('product-image/delete/<int:image_id>/', views.product_image_delete, name='product_image_delete'),


]