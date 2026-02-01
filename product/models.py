from django.db import models
from django.db.models.signals import post_delete
from django.dispatch import receiver
import os

class Brand(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
class Category(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name



class UnitOfMeasurement(models.Model):
    name = models.CharField(max_length=50)
    symbol = models.CharField(max_length=10)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name} ({self.symbol})"

class Product(models.Model):
    product_name = models.CharField(max_length=25)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.CharField(max_length=50)
    stock = models.IntegerField()
    mfg_date = models.DateField()
    exp_date = models.DateField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    unit = models.ForeignKey(UnitOfMeasurement, on_delete=models.CASCADE)

    def __str__(self):
        return self.product_name

class Batch(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='batches')
    batch_number = models.CharField(max_length=50)
    quantity = models.PositiveIntegerField()
    mfg_date = models.DateField()
    exp_date = models.DateField()

    def __str__(self):
        return f"{self.batch_number} - {self.product.product_name}"
    

class ProductImage(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='images'
    )
    image = models.ImageField(upload_to='product_images/')


@receiver(post_delete, sender=ProductImage)
def auto_delete_image_on_delete(sender, instance, **kwargs):
    if instance.image and os.path.isfile(instance.image.path):
        os.remove(instance.image.path)
