from django.contrib import admin
from .models import Article
# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']
    list_display_links = ['title']
    ordering = ['id']

admin.site.register(Article, ArticleAdmin)