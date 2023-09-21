from django.shortcuts import render

from apps.products.models import Product


def frontpage(request):
    products = Product.objects.all()[:6]
    return render(request, "core/front_page.html", {"products": products})


def contact(request):
    return render(request, "core/contact.html")
