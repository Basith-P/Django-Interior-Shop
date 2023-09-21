import random

from django.shortcuts import get_object_or_404, render

from .models import Product


def product(request, cat_slug, prod_slug):
    product = get_object_or_404(Product, slug=prod_slug, category__slug=cat_slug)

    similar_products = list(product.category.products.exclude(id=product.id))
    if len(similar_products) > 4:
        similar_products = random.sample(similar_products, 4)

    context = {
        "product": product,
        "similar_products": similar_products,
    }
    return render(request, "products/product.html", context)
