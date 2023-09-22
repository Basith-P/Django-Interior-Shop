from django.urls import path

from . import views

app_name = "products"

urlpatterns = [
    path("search/", views.search, name="search"),
    path("<slug:cat_slug>/<slug:prod_slug>/", views.product, name="product"),
    path("<slug:cat_slug>/", views.category, name="category"),
]
