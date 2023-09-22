from django.shortcuts import redirect, render

from .cart import Cart


def cart_view(request):
    cart = Cart(request)
    remove_item = request.GET.get("remove")
    if remove_item:
        cart.remove(remove_item)

        return redirect("cart:cart")
    return render(request, "cart/cart_details.html")
