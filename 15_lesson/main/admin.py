from symtable import Class
from .models import New
from django.contrib import admin

# Register your models here.

class NewAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('title', )
    search_fields = ('id', 'title')
    list_filter = ('title', )

admin.site.register(New, NewAdmin)
