from django.db import models
from product.models import Product
from accounts.models import UserRegister 
from django.utils import timezone

class Cart(models.Model):
    user = models.ForeignKey(
        UserRegister,  # use your custom model
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    cart_id=models.CharField(max_length=250,blank=True)
    date_added=models.DateTimeField(auto_now_add=True)
    session_key = models.CharField(max_length=40, null=True, blank=True)

    def __str__(self):
        return self.cart_id


class CartItem(models.Model):
    cart = models.ForeignKey(
        Cart,
        on_delete=models.CASCADE
    )
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    added_at = models.DateTimeField(null=True, blank=True)
    def sub_total(self):
        return self.product.price * self.quantity
    def __str__(self):
        return self.product.product_name
