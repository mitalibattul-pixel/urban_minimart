
from django.shortcuts import render, redirect
from .models import UserRegister

def register(request):
    if request.method == "POST":
        first_name = request.POST.get('firstname')
        last_name = request.POST.get('lastname')
        gender = request.POST.get('gender')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password == confirm_password:
            UserRegister.objects.create(
                first_name=first_name,
                last_name=last_name,
                gender=gender,
                email=email,
                phone=phone,
                password=password
            )
            return redirect('register')
        else:
            return render(request, 'register.html', {
                'error': 'Passwords do not match'
            })

    return render(request, 'pages/register.html')


def login_view(request):
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]

        try:
            user = UserRegister.objects.get(email=email, password=password)
            # store user info in session
            request.session['user_id'] = user.id
            request.session['user_email'] = user.email
            return redirect('index')
        except UserRegister.DoesNotExist:
            return render(request, 'pages/login.html', {'error': 'Invalid credentials'})
    
    return render(request, 'pages/login.html')
