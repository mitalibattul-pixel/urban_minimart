from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from .models import UserProfile

def register(request):
    if request.method == "POST":
        first_name = request.POST.get("firstname")
        last_name = request.POST.get("lastname")
        email = request.POST.get("email")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirmpassword")

        if password != confirm_password:
            messages.error(request, "Passwords do not match")
            return redirect("register")

        if User.objects.filter(username=email).exists():
            messages.error(request, "Email already registered")
            return redirect("register")

        user = User.objects.create_user(
            username=email,
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name
        )

        UserProfile.objects.create(user=user)

        messages.success(request, "Registration successful. Please login.")
        return redirect("login")

    return render(request, "register.html")
