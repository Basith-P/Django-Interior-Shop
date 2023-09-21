from io import BytesIO

from django.core.files import File
from django.db import models
from PIL import Image

from apps.vendor.models import Vendor


class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    ordering = models.IntegerField(default=0)

    class Meta:
        verbose_name_plural = "Categories"
        ordering = ["ordering"]

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="products"
    )
    vendor = models.ForeignKey(
        Vendor, on_delete=models.CASCADE, related_name="products"
    )
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    date_added = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to="products/images", blank=True, null=True)
    thumbnail = models.ImageField(upload_to="products/thumbs", blank=True, null=True)

    class Meta:
        ordering = ["-date_added"]

    def __str__(self):
        return self.name

    def get_thumbnail(self):
        if self.thumbnail:
            return self.thumbnail.url
        else:
            if self.image:
                self.thumbnail = self.make_thumbnail(self.image)
                self.save()
                return self.thumbnail.url
            else:
                return "https://via.placeholder.com/240x180.jpg"

    def make_thumbnail(self, image, size=(300, 200)):
        img = Image.open(image)
        img.convert("RGBA")
        img.thumbnail(size)

        thumb_io = BytesIO()
        img.save(thumb_io, "PNG", quality=85)

        thumbnail = File(thumb_io, name=image.name)

        return thumbnail
