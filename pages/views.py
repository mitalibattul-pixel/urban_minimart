from django.shortcuts import render

def index(request):
    return render(request, 'pages/index.html')

def about(request):
    return render(request, 'pages/about.html')

def service(request):
    return render(request, 'pages/service.html')

def faq(request):
    return render(request, 'pages/faq.html')

def contact(request):
    return render(request, 'pages/contact.html')

from product.models import Product

def shop(request):
    products = Product.objects.prefetch_related('images')

    return render(request, 'pages/shop.html', {
        'products': products
    })


def product_details(request):
    return render(request, 'pages/product_details.html')

def cart(request):
    return render(request, 'pages/cart.html')

def wishlist(request):
    return render(request, 'pages/wishlist.html')

def login(request):
    return render(request, 'pages/login.html')

def register(request):
    return render(request, 'pages/register.html')

def account(request):
    return render(request, 'pages/account.html')