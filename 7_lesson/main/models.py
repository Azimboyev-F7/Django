from django.db import models

# Create your models here.

class News(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

