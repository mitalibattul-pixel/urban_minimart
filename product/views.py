from django.shortcuts import render, redirect, get_object_or_404
from .models import Brand,Category,SubCategory
from .forms import BrandForm,CategoryForm,SubCategoryForm



# List all brands
def brand_list(request):
    brands = Brand.objects.all()
    return render(request, 'product/brand_list.html', {'brands': brands})

# Add a new brand
def brand_add(request):
    if request.method == 'POST':
        form = BrandForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product:brand_list')
    else:
        form = BrandForm()
    return render(request, 'product/brand_form.html', {'form': form})

# Edit brand
def brand_edit(request, pk):
    brand = get_object_or_404(Brand, pk=pk)
    if request.method == 'POST':
        form = BrandForm(request.POST, instance=brand)
        if form.is_valid():
            form.save()
            return redirect('product:brand_list')
    else:
        form = BrandForm(instance=brand)
    return render(request, 'product/brand_form.html', {'form': form})

# Delete brand
def brand_delete(request, pk):
    brand = get_object_or_404(Brand, pk=pk)
    brand.delete()
    return redirect('product:brand_list')

def category_list(request):
    categories = Category.objects.all()
    return render(request, 'product/category_list.html', {
        'categories': categories
    })


# ADD CATEGORY
def category_add(request):
    form = CategoryForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('product:category_list')
    return render(request, 'product/category_form.html', {
        'form': form
    })


# EDIT CATEGORY
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


# DELETE CATEGORY
def category_delete(request, id):
    category = get_object_or_404(Category, id=id)
    category.delete()
    return redirect('product:category_list')

def subcategory_list(request):
    subcategories = SubCategory.objects.select_related('category')
    return render(request, 'product/subcategory_list.html', {
        'subcategories': subcategories
    })


def subcategory_add(request):
    form = SubCategoryForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('product:subcategory_list')
    return render(request, 'product/subcategory_form.html', {'form': form})


def subcategory_edit(request, id):
    subcategory = get_object_or_404(SubCategory, id=id)
    form = SubCategoryForm(request.POST or None, instance=subcategory)
    if form.is_valid():
        form.save()
        return redirect('product:subcategory_list')
    return render(request, 'product/subcategory_form.html', {'form': form})


def subcategory_delete(request, id):
    subcategory = get_object_or_404(SubCategory, id=id)
    subcategory.delete()
    return redirect('product:subcategory_list')
