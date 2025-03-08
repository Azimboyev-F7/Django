from django.urls import path
from .views import index, article, detail, create, remove

app_name = 'main'

urlpatterns = [
    path('', index, name="index"),
    path('article/', article, name='article'),
    path('article/<int:pk>/', detail, name='detail'),
    path('create/', create, name='article-add'),
    path('article/remove/<int:pk>', remove, name='article-remove'),
]
