from django.urls import path
from . import views

app_name = 'carts'  # THIS MUST MATCH YOUR APP NAME

urlpatterns = [

    path('add_cart/<int:product_id>/', views.add_cart, name='add_cart'),
    path('remove_cart/<int:product_id>/', views.remove_cart, name='remove_cart'), 
    path('remove_item/<int:product_id>/', views.remove_cart_item, name='remove_cart_item'),
 # add product to cart
    # path('detail/<int:pk>/', views.cart_detail, name='cart_detail'),  # view a single cart
    # path('delete/<int:pk>/', views.cart_delete, name='cart_delete'),  # delete cart
    # path('', views.cart_list, name='cart_list'),  # view all carts (admin/testing)
    # # Cart item operations
    # path('item/update/<int:pk>/', views.cart_item_update, name='cart_item_update'),
    # path('item/delete/<int:pk>/', views.cart_item_delete, name='cart_item_delete'),
]
