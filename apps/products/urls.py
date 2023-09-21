from django.urls import path

from . import views

app_name = "products"

urlpatterns = [
    path("<slug:cat_slug>/<slug:prod_slug>/", views.product, name="product"),
]
