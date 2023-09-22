from django.shortcuts import redirect, render

from .cart import Cart


def cart_view(request):
    cart = Cart(request)
    remove_item = request.GET.get("remove")
    change_quantity = request.GET.get("change_quantity")
    quantity = request.GET.get("quantity")

    if remove_item:
        cart.remove(remove_item)
        return redirect("cart:cart")

    if change_quantity:
        cart.add(change_quantity, quantity, True)
        return redirect("cart:cart")

    return render(request, "cart/cart_details.html")
