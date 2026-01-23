from django.shortcuts import render
from django.contrib.auth import get_user_model
from accounts.models import UserRegister

User = get_user_model()

def dashboard(request):
    return render(request, 'adminpanel/dashboard.html')

def admin_users(request):
    users = UserRegister.objects.all()  # get all users from the table
    return render(request, 'adminpanel/user.html', {'users': users})