from django.urls import path
from .views import index, articles

app_name = 'main'

urlpatterns = [
    path('', index, name='index'),
    path('articles/', articles, name='articles'),
]