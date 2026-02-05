from django.shortcuts import render, redirect, get_object_or_404
from product.models import Product,Category
from .models import Cart, CartItem
from django.utils import timezone
# ==========================
# CART
# ==========================

# def cart_list(request):
#     carts = Cart.objects.all()
#     return render(request, 'carts/cart_list.html', {'carts': carts})


# def cart_detail(request, pk):
#     cart = get_object_or_404(Cart, pk=pk)
#     return render(request, 'carts/cart_detail.html', {'cart': cart})

# def cart_delete(request, pk):
#     cart = get_object_or_404(Cart, pk=pk)
#     if request.method == 'POST':
#         cart.delete()
#         return redirect('carts:cart_list')
#     return render(request, 'carts/confirm_delete.html', {'object': cart})

# # ==========================
# # CART ITEM
# # ==========================

# def cart_item_update(request, pk):
#     item = get_object_or_404(CartItem, pk=pk)

#     if request.method == 'POST':
#         qty = int(request.POST.get('quantity'))
#         if qty > 0:
#             item.quantity = qty
#             item.save()
#         else:
#             item.delete()

#     return redirect('carts:cart_detail', pk=item.cart.id)


# def cart_item_delete(request, pk):
#     item = get_object_or_404(CartItem, pk=pk)
#     cart_id = item.cart.id
#     item.delete()
#     return redirect('carts:cart_detail', pk=cart_id)

def _cart_id(request):
    cart=request.session.session_key
    if not cart:
        cart = request.session.create()
    return cart

def remove_cart(request, product_id):
    try:
        # get the current session cart
        cart = Cart.objects.get(cart_id=_cart_id(request))
    except Cart.DoesNotExist:
        return redirect("cart")

    try:
        # find the cart item for this product
        cart_item = CartItem.objects.get(product_id=product_id, cart=cart)
        if cart_item.quantity > 0:
            cart_item.quantity -= 1
            cart_item.save()  # save the updated quantity
        else:
            cart_item.delete()  # remove the item if quantity is 1
    except CartItem.DoesNotExist:
        pass  # ignore if item not in cart

    return redirect("cart")

def remove_cart_item(request, product_id):
    cart = Cart.objects.get(cart_id=_cart_id(request))
    cart_item = get_object_or_404(CartItem, cart=cart, product__id=product_id)
    cart_item.delete()
    return redirect('cart')

def add_cart(request, product_id):
    product = Product.objects.get(id=product_id)

    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))
    except Cart.DoesNotExist:
        cart = Cart.objects.create(cart_id=_cart_id(request))

    try:
        cart_item = CartItem.objects.get(product=product, cart=cart)
        cart_item.quantity += 1
        cart_item.save()
    except CartItem.DoesNotExist:
        CartItem.objects.create(
            product=product,
            quantity=1,
            cart=cart,
            added_at=timezone.now()
        )

    return redirect('cart')
