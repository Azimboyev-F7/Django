from tkinter.font import names

from django.urls import path
from .views import index

app_name = "main"

urlpatterns = [
    path("", index, name="index"),
]