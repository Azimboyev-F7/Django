from django.shortcuts import render

from .models import News


# Create your views here.

def index(request):
    context = {}
    data = News.objects.all()
    return render(request, 'index.html', {'data': data})
