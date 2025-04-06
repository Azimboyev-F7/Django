from django.urls import path
from .views import index, article, detail, remove, create_form, update, create

app_name = 'main'

urlpatterns = [
    path('', index, name="index"),
    path('article/', article, name='article'),
    path('article/<slug:slug>/', detail, name='detail'),
    # path('create/', create, name='article-add'),
    path('article/remove/<slug:slug>', remove, name='article-remove'),
    path('article/create-form/', create_form, name='create-form'),
    path('article/create/', create, name='create'),
    path('article/update/<slug:slug>', update, name='update'),
]
