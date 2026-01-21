from django.shortcuts import render


def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def service(request):
    return render(request, 'service.html')

def faq(request):
    return render(request, 'faq.html')

def locations(request):
    return render(request, 'locations.html')

def contact(request):
    return render(request, 'contact.html')

def shop(request):
    return render(request, 'shop.html')

def product_details(request):
    return render(request, 'product_details.html')

def cart(request):
    return render(request, 'cart.html')

def wishlist(request):
    return render(request, 'wishlist.html')

def login(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')

def account(request):
    return render(request, 'account.html')

<<<<<<< HEAD

=======
def dashboard(request):
    return render(request,'admin/dashboard.html')
>>>>>>> 6d1651d6e17de11ececd7f4637b10adfead69cac
