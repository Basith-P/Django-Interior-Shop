from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render
from django.utils.text import slugify

from .forms import ProductForm
from .models import Vendor


def become_vendor(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            Vendor.objects.create(created_by=user, name=user.username)
            return redirect("core:frontpage")
    else:
        form = UserCreationForm()

    return render(request, "vendor/become_vendor.html", {"form": form})


@login_required
def vendor_dashboard(request):
    vendor = request.user.vendor
    products = vendor.products.all()

    context = {"vendor": vendor, "products": products}

    return render(request, "vendor/dashboard.html", context)


@login_required
def add_product(request):
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)

        if form.is_valid():
            product = form.save(commit=False)
            product.vendor = request.user.vendor
            product.slug = slugify(product.name)
            product.save()

            return redirect("vendor:vendor_dashboard")
    else:
        form = ProductForm()

    return render(request, "vendor/add_product.html", {"form": form})
