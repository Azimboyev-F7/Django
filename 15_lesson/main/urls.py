from django.urls import path
from .views import index, article, detail, remove, create_form, update

app_name = 'main'

urlpatterns = [
    path('', index, name="index"),
    path('article/', article, name='article'),
    path('article/<int:pk>/', detail, name='detail'),
    # path('create/', create, name='article-add'),
    path('article/remove/<int:pk>', remove, name='article-remove'),
    path('article/create-form/', create_form, name='create-form'),
    path('article/update/<int:pk>', update, name='update'),
]
