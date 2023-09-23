from apps.cart.cart import Cart

from .models import Order, OrderItem


def checkout(
    request,
    first_name,
    last_name,
    email,
    address,
    postal_code,
    city,
    phone,
    paid_amount,
):
    order = Order.objects.create(
        first_name=first_name,
        last_name=last_name,
        email=email,
        address=address,
        postal_code=postal_code,
        city=city,
        phone=phone,
        paid_amount=paid_amount,
    )

    cart = Cart(request)
    for item in cart:
        OrderItem.objects.create(
            order=order,
            product=item["product"],
            vendor=item["product"].vendor,
            price=item["product"].price,
            quantity=item["quantity"],
        )
        order.Vendors.add(item["product"].vendor)
    return order
