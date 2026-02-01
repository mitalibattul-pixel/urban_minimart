from django.shortcuts import render, redirect, get_object_or_404
from .models import (
    Brand, Category, 
    UnitOfMeasurement, Product,
    Batch, ProductImage
)
from .forms import (
    BrandForm, CategoryForm,
    UnitForm, ProductForm, BatchForm, ProductImageForm
)

# ==========================
# BRAND
# ==========================

def brand_list(request):
    brands = Brand.objects.all()
    return render(request, 'product/brand_list.html', {'brands': brands})


def brand_add(request):
    form = BrandForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('product:brand_list')
    return render(request, 'product/brand_form.html', {'form': form})


def brand_edit(request, pk):
    brand = get_object_or_404(Brand, pk=pk)
    form = BrandForm(request.POST or None, instance=brand)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('product:brand_list')
    return render(request, 'product/brand_form.html', {'form': form})


def brand_delete(request, pk):
    brand = get_object_or_404(Brand, pk=pk)
    if request.method == 'POST':
        brand.delete()
        return redirect('product:brand_list')
    return render(request, 'product/confirm_delete.html', {'object': brand})


# ==========================
# CATEGORY
# ==========================

def category_list(request):
    categories = Category.objects.all()
    return render(request, 'product/category_list.html', {'categories': categories})


def category_add(request):
    form = CategoryForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('product:category_list')
    return render(request, 'product/category_form.html', {'form': form})


def category_edit(request, pk):
    category = get_object_or_404(Category, pk=pk)
    form = CategoryForm(request.POST or None, instance=category)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('product:category_list')
    return render(request, 'product/category_form.html', {'form': form})


def category_delete(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        category.delete()
        return redirect('product:category_list')
    return render(request, 'product/confirm_delete.html', {'object': category})


# ==========================
# SUB CATEGORY
# ==========================




# ==========================
# UNIT
# ==========================

def unit_list(request):
    units = UnitOfMeasurement.objects.all()
    return render(request, 'product/unit_list.html', {'units': units})


def unit_add(request):
    form = UnitForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('product:unit_list')
    return render(request, 'product/unit_form.html', {'form': form})


def unit_edit(request, pk):
    unit = get_object_or_404(UnitOfMeasurement, pk=pk)
    form = UnitForm(request.POST or None, instance=unit)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('product:unit_list')
    return render(request, 'product/unit_form.html', {'form': form})


def unit_delete(request, pk):
    unit = get_object_or_404(UnitOfMeasurement, pk=pk)
    if request.method == 'POST':
        unit.delete()
        return redirect('product:unit_list')
    return render(request, 'product/confirm_delete.html', {'object': unit})


# ==========================
# PRODUCT
# ==========================

def product_list(request):
    products = Product.objects.select_related(
        'category', 'unit'
    )
    return render(request, 'product/product_list.html', {'products': products})


def product_add(request):
    form = ProductForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('product:product_list')
    return render(request, 'product/product_form.html', {'form': form})


def product_edit(request, pk):
    product = get_object_or_404(Product, pk=pk)
    form = ProductForm(request.POST or None, instance=product)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('product:product_list')
    return render(request, 'product/product_form.html', {'form': form})


def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('product:product_list')
    return render(request, 'product/confirm_delete.html', {'object': product})


# ==========================
# BATCH
# ==========================

def batch_list(request):
    batches = Batch.objects.select_related('product')
    return render(request, 'product/batch_list.html', {'batches': batches})


def batch_add(request):
    form = BatchForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('product:batch_list')
    return render(request, 'product/batch_form.html', {'form': form})


def batch_edit(request, pk):
    batch = get_object_or_404(Batch, pk=pk)
    form = BatchForm(request.POST or None, instance=batch)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('product:batch_list')
    return render(request, 'product/batch_form.html', {'form': form})


def batch_delete(request, pk):
    batch = get_object_or_404(Batch, pk=pk)
    if request.method == 'POST':
        batch.delete()
        return redirect('product:batch_list')
    return render(request, 'product/confirm_delete.html', {'object': batch})


# ==========================
# PRODUCT IMAGES
# ==========================

def add_product_image(request, pk):
    product = get_object_or_404(Product, pk=pk)
    images = product.images.all()

    form = ProductImageForm(request.POST or None, request.FILES or None)
    if request.method == 'POST' and form.is_valid():
        img = form.save(commit=False)
        img.product = product
        img.save()
        return redirect('product:add_product_image', pk=pk)

    return render(request, 'product/add_product_image.html', {
        'product': product,
        'form': form,
        'images': images
    })


def product_image_delete(request, image_id):
    image = get_object_or_404(ProductImage, pk=image_id)
    product_id = image.product.id
    image.delete()
    return redirect('product:add_product_image', pk=product_id)

def shop(request):
    products = Product.objects.prefetch_related('images')
    product_count=products.count()
    context={
        'products': products,
       'product_count':product_count,
        
    }
    return render(request, 'product/shop.html',context )

