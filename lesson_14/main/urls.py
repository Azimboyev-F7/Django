from django.urls import path
from .views import index, articles, detail

app_name = 'main'

urlpatterns = [
    path('', index, name='index'),
    path('articles/', articles, name='articles'),
    path('articles/<int:pk>', detail, name='detail'),
]