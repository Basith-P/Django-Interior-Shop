from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render

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
    return render(request, "vendor/dashboard.html", {"vendor": vendor})
