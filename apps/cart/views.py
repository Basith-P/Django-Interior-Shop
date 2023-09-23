import stripe
from django.conf import settings
from django.contrib import messages
from django.shortcuts import redirect, render

from apps.orders.utils import checkout

from .cart import Cart
from .forms import CheckoutForm


def cart_view(request):
    cart = Cart(request)

    if request.method == "POST":
        form = CheckoutForm(request.POST)

        if form.is_valid():
            stripe.api_key = settings.STRIPE_SECRET_KEY
            stripe_token = form.cleaned_data["stripe_token"]

            stripe.Charge.create(
                amount=int(cart.get_total_cost() * 100),
                currency="inr",
                description="Charge from Interior Shop",
                source=stripe_token,
            )

            cd = form.cleaned_data
            checkout(
                request,
                cd["name"],
                cd["email"],
                cd["address"],
                cd["postal_code"],
                cd["city"],
                cd["stripe_token"],
                cd["phone"],
                cart.get_total_cost(),
            )

            cart.clear()
            return redirect("cart:success")
        # else:
        #     messages.error(request, "Error processing your order")
    else:
        form = CheckoutForm()

    remove_item = request.GET.get("remove")
    change_quantity = request.GET.get("change_quantity")
    quantity = request.GET.get("quantity")

    if remove_item:
        cart.remove(remove_item)
        return redirect("cart:cart")

    if change_quantity:
        cart.add(change_quantity, quantity, True)
        return redirect("cart:cart")

    context = {
        "form": form,
        "stripe_pub_key": settings.STRIPE_PUB_KEY,
    }

    return render(request, "cart/cart_details.html", context)


def success(request):
    return render(request, "cart/success.html")
