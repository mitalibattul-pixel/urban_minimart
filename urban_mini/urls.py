"""
URL configuration for urban_mini project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("admin/", admin.site.urls),
    path("about/", views.about, name="about"),
    path("service/", views.service, name="service"),
    path("faq/", views.faq, name="faq"),
    path("locations/", views.locations, name="locations"),
    path("contact/", views.contact, name="contact"),
    path("shop/", views.shop, name="shop"),
    path("product_details/", views.product_details, name="product_details"),
    path("cart/", views.cart, name="cart"),
    path("wishlist/", views.wishlist, name="wishlist"),
    path("login/", views.login, name="login"),
    path("register/", views.register, name="register"),
    path("account/", views.account, name="account"),

    path("accounts/", include("accounts.urls")),
    path("adminpanel/", views.dashboard, name="admin_dashboard"),
]
