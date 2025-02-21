from django.db import models

# Create your models here.

class New:
    title = models.CharField(max_length=221)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title