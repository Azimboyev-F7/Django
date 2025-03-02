from django.urls import path
from .views import index, article, detail

app_name = 'main'

urlpatterns = [
    path('', index, name="index"),
    path('article/', article, name='article'),
    path('article/<int:pk>/', detail, name='detail'),
]
