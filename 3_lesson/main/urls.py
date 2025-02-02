from django.shortcuts import render
from django.urls import path
from .views import index, blogs

app_name = 'main'

urlpatterns = [
    path("", view=index, name="index"),
    path("blogs/", view=blogs, name="blogs"),
]