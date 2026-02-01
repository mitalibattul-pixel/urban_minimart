from django import forms
from .models import *

class BrandForm(forms.ModelForm):
    class Meta:
        model = Brand
        fields = ['name']

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']



class UnitForm(forms.ModelForm):
    class Meta:
        model = UnitOfMeasurement
        fields = ['name', 'symbol', 'is_active']

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        widgets = {
            'mfg_date': forms.DateInput(attrs={'type': 'date'}),
            'exp_date': forms.DateInput(attrs={'type': 'date'}),
        }

class BatchForm(forms.ModelForm):
    class Meta:
        model = Batch
        fields = '__all__'
        widgets = {
            'product': forms.Select(attrs={'class': 'form-select'}),
            'batch_number': forms.TextInput(attrs={'class': 'form-control'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control'}),
            'mfg_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'exp_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }
class ProductImageForm(forms.ModelForm):
    class Meta:
        model = ProductImage
        fields = ['image']