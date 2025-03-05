from django.urls import path
from .views import index, articles, detail, create, delete

app_name = 'main'

urlpatterns = [
    path('', index, name='index'),
    path('articles/', articles, name='articles'),
    path('articles/<int:pk>', detail, name='detail'),
    path('create/', create, name='create'),
    path('delete/<int:pk>', delete, name='delete'),
]