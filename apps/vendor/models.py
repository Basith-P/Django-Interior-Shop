from django.contrib.auth.models import User
from django.db import models


class Vendor(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.OneToOneField(User, on_delete=models.CASCADE)

    class Meta:
        # verbose_name = 'Vendor'
        # verbose_name_plural = 'Vendors'
        ordering = ['name']

    def __str__(self):
        return self.name
