from django.urls import path
from . import views

app_name = 'adminpanel'   # 🔥 THIS LINE WAS MISSING

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('users/', views.admin_users, name='admin_users'),
]
