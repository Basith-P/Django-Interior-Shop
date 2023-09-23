from django.urls import path

from .views import cart_view, success

app_name = "cart"

urlpatterns = [
    path("", cart_view, name="cart"),
    path("success/", success, name="success"),
]
