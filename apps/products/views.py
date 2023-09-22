import random

from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render

from .models import Category, Product


def search(request):
    query = request.GET.get("q")
    if not query:
        return redirect("/")
    products = Product.objects.filter(Q(name__icontains=query))
    context = {"products": products, "query": query}
    return render(request, "products/search.html", context)


def product(request, cat_slug, prod_slug):
    product = get_object_or_404(Product, slug=prod_slug, category__slug=cat_slug)

    similar_products = list(product.category.products.exclude(id=product.id))  # type: ignore
    if len(similar_products) > 4:
        similar_products = random.sample(similar_products, 4)

    context = {
        "product": product,
        "similar_products": similar_products,
    }
    return render(request, "products/product.html", context)


def category(request, cat_slug):
    category = get_object_or_404(Category, slug=cat_slug)
    products = category.products.all()  # type: ignore

    context = {
        "category": category,
        "products": products,
    }

    return render(request, "products/category.html", context)
