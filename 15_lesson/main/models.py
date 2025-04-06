from django.db import models
from django.utils.text import slugify
from django.db.models.signals import post_save, pre_save

# Create your models here.

class New(models.Model):
    image = models.ImageField(upload_to='images/',null=True,blank=True)
    title = models.CharField(max_length=221)
    slug = models.SlugField(null=True, blank=True)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    


def pre_save_new_receiver(sender, instance, *args, **kwargs):
    instance.slug = slugify(instance.title)
    if New.objects.filter(slug=slugify(instance.title)).exclude(id=instance.id).exists():
        import uuid
        instance.slug += f"{slugify(instance.title)}-{uuid.uuid4()}"


pre_save.connect(pre_save_new_receiver, sender=New)