
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
            return redirect('/')
        else:
            return render(request, 'register.html', {
                'error': 'Passwords do not match'
            })

    return render(request, 'pages/register.html')


def login_view(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']

        user = UserRegister.objects.filter(
            email=email,
            password=password
        ).first()

        if user:
            request.session['user_id'] = user.id
            request.session['user_name'] = user.email


            return redirect('/')   
        else:
            return render(request, 'pages/login.html', {
                'error': 'Invalid email or password'
            })

    return render(request, 'pages/login.html')
