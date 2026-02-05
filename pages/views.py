from django.shortcuts import render
from product.models import Category, Product
from django.shortcuts import render, redirect, get_object_or_404
from carts.models import Cart, CartItem
from django.http import HttpResponse

def index(request):
    categories = Category.objects.all()
    products = Product.objects.prefetch_related('images', 'category')
    
    # Slider ke liye cart data yahan bhi chahiye
    total = 0
    quantity = 0
    cart_items = []
    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))
        cart_items = CartItem.objects.filter(cart=cart)
        for cart_item in cart_items:
            total += cart_item.product.price * cart_item.quantity
            quantity += cart_item.quantity
    except ObjectDoesNotExist:
        pass

    context = {
        'categories': categories,
        'products': products,
        'cart_items': cart_items, # Ye zaroori hai slider ke liye
        'total': total,
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
        in_cart=CartItem.objects.filter(cart__cart_id=_cart_id(request),product=single_product).exists()
     
    except Exception as e:
        raise e

    context ={
        'single_product' : single_product,
        'in_cart' : in_cart,
    }
    return render(request,'pages/product_details.html',context)

def _cart_id(request):
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()
    return cart

from django.core.exceptions import ObjectDoesNotExist

def cart(request, total=0, quantity=0, cart_items=None):
    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))
        cart_items = CartItem.objects.filter(cart=cart)

        for cart_item in cart_items:
            total += cart_item.product.price * cart_item.quantity
            quantity += cart_item.quantity

    except ObjectDoesNotExist:
        cart_items = []

    context = {
        'total': total,
        'quantity': quantity,
        'cart_items': cart_items,
    }
    return render(request, 'pages/cart.html', context)


def wishlist(request):
    return render(request, 'pages/wishlist.html')

def login(request):
    return render(request, 'pages/login.html')

def register(request):
    return render(request, 'pages/register.html')

def account(request):
    return render(request, 'pages/account.html')

def checkout(request):
    return render(request, 'pages/checkout.html')