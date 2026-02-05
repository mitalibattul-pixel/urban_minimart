from .models import Cart, CartItem
from .views import _cart_id

def counter(request):
    cart_count = 0
    cart_items = []
    total = 0
    try:
        cart = Cart.objects.filter(cart_id=_cart_id(request))
        if request.user.is_authenticated:
            cart_items = CartItem.objects.filter(user=request.user)
        else:
            cart_items = CartItem.objects.filter(cart=cart[:1])

        for cart_item in cart_items:
            total += (cart_item.product.price * cart_item.quantity)
            cart_count += cart_item.quantity
    except Cart.DoesNotExist:
        cart_count = 0
    return dict(cart_items=cart_items, total=total, cart_count=cart_count)