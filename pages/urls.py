
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("admin/", admin.site.urls),
    path("about/", views.about, name="about"),
    path("service/", views.service, name="service"),
    path("faq/", views.faq, name="faq"),

    path("contact/", views.contact, name="contact"),
    path("shop/", views.shop, name="shop"),
    path("product_details/", views.product_details, name="product_details"),
    path("cart/", views.cart, name="cart"),
    path("wishlist/", views.wishlist, name="wishlist"),
    path("login/", views.login, name="login"),
    path("register/", views.register, name="register"),
    path("account/", views.account, name="account"),

]
