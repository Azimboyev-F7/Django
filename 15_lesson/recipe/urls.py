from django.urls import path

from .views import index

app_name = 'recipe'

urlpatterns = [
    path('', index, name='index'),
]