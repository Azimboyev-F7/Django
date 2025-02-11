from django.urls import path
from .views import index

from config.urls import urlpatterns

app_name = 'main'


urlpatterns = [
    path('', index, name='index'),
]