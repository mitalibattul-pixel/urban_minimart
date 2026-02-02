from django.urls import path
from . import views

app_name = 'product'

urlpatterns = [


    # 🛍 SHOP
    path("shop/", views.shop, name="shop"),
    path("shop/<slug:category_slug>/", views.shop, name="product_by_category"),

    # 🔹 BRAND
    path("brands/", views.brand_list, name="brand_list"),
    path("brands/add/", views.brand_add, name="brand_add"),
    path("brands/edit/<int:pk>/", views.brand_edit, name="brand_edit"),
    path("brands/delete/<int:pk>/", views.brand_delete, name="brand_delete"),

    # 🔹 CATEGORY (ADMIN)
    path("category/", views.category_list, name="category_list"),
    path("category/add/", views.category_add, name="category_add"),
    path("category/edit/<int:pk>/", views.category_edit, name="category_edit"),
    path("category/delete/<int:pk>/", views.category_delete, name="category_delete"),

    # 🔹 UNITS
    path("units/", views.unit_list, name="unit_list"),
    path("units/add/", views.unit_add, name="unit_add"),
    path("units/edit/<int:pk>/", views.unit_edit, name="unit_edit"),
    path("units/delete/<int:pk>/", views.unit_delete, name="unit_delete"),

    # 🔹 PRODUCTS
    path("products/", views.product_list, name="product_list"),
    path("products/add/", views.product_add, name="product_add"),
    path("products/edit/<int:pk>/", views.product_edit, name="product_edit"),
    path("products/delete/<int:pk>/", views.product_delete, name="product_delete"),

    # 🔹 PRODUCT IMAGES
    path("product/<int:pk>/images/add/", views.add_product_image, name="add_product_image"),
    path("product-image/delete/<int:image_id>/", views.product_image_delete, name="product_image_delete"),

    # 🔹 BATCHES
    path("batches/", views.batch_list, name="batch_list"),
    path("batches/add/", views.batch_add, name="batch_add"),
    path("batches/edit/<int:pk>/", views.batch_edit, name="batch_edit"),
    path("batches/delete/<int:pk>/", views.batch_delete, name="batch_delete"),
    
]
