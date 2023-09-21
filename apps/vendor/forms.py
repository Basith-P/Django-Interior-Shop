from django.forms import ModelForm

from apps.products.models import Product


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ["category", "name", "description", "price", "image"]
