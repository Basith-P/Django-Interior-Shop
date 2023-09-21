from django.contrib.auth import views as auth_views
from django.urls import path

from . import views

app_name = "vendor"

urlpatterns = [
    path("become-vendor/", views.become_vendor, name="become_vendor"),
    path("dashboard/", views.vendor_dashboard, name="vendor_dashboard"),
    path(
        "login/",
        auth_views.LoginView.as_view(template_name="vendor/login.html"),
        name="login",
    ),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
]
