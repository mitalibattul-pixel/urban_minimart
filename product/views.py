from django.shortcuts import render, redirect, get_object_or_404
from .models import Brand, Category, SubCategory, UnitOfMeasurement,Product,Batch,ProductImage
from .forms import (
    BrandForm,
    CategoryForm,
    SubCategoryForm,
    UnitForm,
    ProductForm,
    BatchForm,
      ProductImageForm,
)
import os
# ==========================
# BRAND VIEWS
# ==========================

def brand_list(request):
    brands = Brand.objects.all()
    return render(request, 'product/brand_list.html', {
        'brands': brands
    })


def brand_add(request):
    form = BrandForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('product:brand_list')

    return render(request, 'product/brand_form.html', {
        'form': form
    })


def brand_edit(request, id):
    brand = get_object_or_404(Brand, id=id)
    form = BrandForm(request.POST or None, instance=brand)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('product:brand_list')

    return render(request, 'product/brand_form.html', {
        'form': form
    })


def brand_delete(request, id):
    brand = get_object_or_404(Brand, id=id)
    brand.delete()
    return redirect('product:brand_list')


# ==========================
# CATEGORY VIEWS
# ==========================

def category_list(request):
    categories = Category.objects.all()
    return render(request, 'product/category_list.html', {
        'categories': categories
    })


def category_add(request):
    form = CategoryForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('product:category_list')

    return render(request, 'product/category_form.html', {
        'form': form
    })


def category_edit(request, id):
    category = get_object_or_404(Category, id=id)
    form = CategoryForm(request.POST or None, instance=category)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('product:category_list')

    return render(request, 'product/category_form.html', {
        'form': form
    })


def category_delete(request, id):
    category = get_object_or_404(Category, id=id)
    category.delete()
    return redirect('product:category_list')


# ==========================
# SUBCATEGORY VIEWS
# ==========================

def subcategory_list(request):
    subcategories = SubCategory.objects.select_related('category')
    return render(request, 'product/subcategory_list.html', {
        'subcategories': subcategories
    })


def subcategory_add(request):
    form = SubCategoryForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('product:subcategory_list')

    return render(request, 'product/subcategory_form.html', {
        'form': form
    })


def subcategory_edit(request, id):
    subcategory = get_object_or_404(SubCategory, id=id)
    form = SubCategoryForm(request.POST or None, instance=subcategory)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('product:subcategory_list')

    return render(request, 'product/subcategory_form.html', {
        'form': form
    })


def subcategory_delete(request, id):
    subcategory = get_object_or_404(SubCategory, id=id)
    subcategory.delete()
    return redirect('product:subcategory_list')


# ==========================
# UNIT OF MEASUREMENT VIEWS
# ==========================

def unit_list(request):
    units = UnitOfMeasurement.objects.all()
    return render(request, 'product/unit_list.html', {
        'units': units
    })


def unit_add(request):
    form = UnitForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('product:unit_list')

    return render(request, 'product/unit_form.html', {
        'form': form
    })


def unit_edit(request, id):
    unit = get_object_or_404(UnitOfMeasurement, id=id)
    form = UnitForm(request.POST or None, instance=unit)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('product:unit_list')

    return render(request, 'product/unit_form.html', {
        'form': form
    })


def unit_delete(request, id):
    unit = get_object_or_404(UnitOfMeasurement, id=id)
    unit.delete()
    return redirect('product:unit_list')


def product_list(request):
    products = Product.objects.all()
    return render(request, 'product/product_list.html', {'products': products})

# Add new product
def product_add(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product:product_list')
    else:
        form = ProductForm()
    return render(request, 'product/product_form.html', {'form': form, 'title': 'Add Product'})

# Edit product
def product_edit(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product:product_list')
    else:
        form = ProductForm(instance=product)
    return render(request, 'product/product_form.html', {'form': form, 'title': 'Edit Product'})

# Delete product
def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('product:product_list')
    return render(request, 'product/product_confirm_delete.html', {'product': product})
    
def batch_list(request):
    batches = Batch.objects.select_related('product').all()
    return render(request, 'product/batch_list.html', {'batches': batches})


def batch_add(request):
    form = BatchForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('product:batch_list')
    return render(request, 'product/batch_form.html', {'form': form})


def batch_edit(request, id):
    batch = get_object_or_404(Batch, id=id)
    form = BatchForm(request.POST or None, instance=batch)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('product:batch_list')
    return render(request, 'product/batch_form.html', {'form': form})


def batch_delete(request, id):
    batch = get_object_or_404(Batch, id=id)
    batch.delete()
    return redirect('product:batch_list')


def add_product_image(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    images = product.images.all()

    if request.method == 'POST':
        form = ProductImageForm(request.POST, request.FILES)
        if form.is_valid():
            img = form.save(commit=False)
            img.product = product
            img.save()
            return redirect('product:add_product_image', product_id=product.id)
    else:
        form = ProductImageForm()

    return render(request, 'product/add_product_image.html', {
        'form': form,
        'product': product,
        'images': images,
    })


def product_image_delete(request, image_id):
    image = get_object_or_404(ProductImage, id=image_id)

    # Delete file from server
    if image.image and os.path.isfile(image.image.path):
        os.remove(image.image.path)

    # Delete DB record
    image.delete()

    return redirect('product:add_product_image', product_id=image.product.id)
