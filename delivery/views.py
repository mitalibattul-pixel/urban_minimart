from django.shortcuts import render

def login_view(request):
    return render(request, 'delivery/login.html')

def dashboard(request):
    return render(request, 'delivery/dashboard.html')

def profile(request):
    return render(request, 'delivery/profile.html')

def orders(request):
    return render(request, 'delivery/orders.html')
