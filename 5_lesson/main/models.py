from django.db import models

# Create your models here.

class Workers(models.Model):
    name = models.CharField(max_length=221)
    second_name = models.CharField(max_length=221)
    email = models.EmailField(max_length=221)
    phone = models.CharField(max_length=221)
    datetime = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
