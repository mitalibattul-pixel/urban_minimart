from django.urls import path
from . import views

app_name = 'delivery'

urlpatterns = [
    path('', views.login_view, name='home'),   # 👈 ADD THIS
    path('login/', views.login_view, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('profile/', views.profile, name='profile'),
    path('orders/', views.orders, name='orders'),
]
