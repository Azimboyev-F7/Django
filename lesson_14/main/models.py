from django.db import models

# Create your models here.

class Article(models.Model):
    image = models.ImageField(upload_to='article/')
    title = models.CharField(max_length=100)
    content = models.TextField()
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
