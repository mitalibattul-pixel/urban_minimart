from django.shortcuts import render, redirect
from .models import Product, Category

def add_product(request):
    categories = Category.objects.all()

    if request.method == 'POST':
        Product.objects.create(
            name=request.POST['name'],
            category_id=request.POST['category'],
            price=request.POST['price'],
            stock=request.POST['stock'],
            image=request.FILES['image'],
            description=request.POST.get('description')
        )
        return redirect('product_list')

    return render(request, 'adminpanel/product/add_product.html', {
        'categories': categories
    })
def product_list(request):
    products = Product.objects.all()
    return render(request, 'adminpanel/product/product_list.html', {
        'products': products
    })

