from django.shortcuts import render
from product.models import Category, Product

def index(request):
    categories = Category.objects.all()
    products = Product.objects.prefetch_related('images', 'category')

    context = {
        'categories': categories,
        'products': products,
    }
    return render(request, 'pages/index.html', context)
def about(request):
    return render(request, 'pages/about.html')

def service(request):
    return render(request, 'pages/service.html')

def faq(request):
    return render(request, 'pages/faq.html')

def contact(request):
    return render(request, 'pages/contact.html')

def product_details(request,category_slug, product_slug):
    try:
        single_product = Product.objects.get(category__slug = category_slug, slug=product_slug)
    except Exception as e:
        raise e

    context ={
        'single_product' : single_product,
    }
    return render(request,'pages/product_details.html',context)


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