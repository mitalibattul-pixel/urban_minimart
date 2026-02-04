from django.urls import path
from . import views

app_name = 'carts'  # THIS MUST MATCH YOUR APP NAME

urlpatterns = [
    path('', views.cart_list, name='cart_list'),  # view all carts (admin/testing)
    path('add_cart/<int:product_id>/', views.add_cart, name='add_cart'),  # add product to cart
    path('detail/<int:pk>/', views.cart_detail, name='cart_detail'),  # view a single cart
    path('delete/<int:pk>/', views.cart_delete, name='cart_delete'),  # delete cart

    # Cart item operations
    path('item/update/<int:pk>/', views.cart_item_update, name='cart_item_update'),
    path('item/delete/<int:pk>/', views.cart_item_delete, name='cart_item_delete'),
]
