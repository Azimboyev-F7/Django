from django.shortcuts import render
from .models import New

# Create your views here.


def index(request):
    news = New.objects.all()
    context = {
        'news': news
    }
    return render(request, 'article/index.html', context)

def article(request):
    news = New.objects.all()
    context = {
        "news": news,
    }
    return render(request, 'article/articles.html', context)

def detail(request,pk):
    new = New.objects.get(id=pk)
    context = {
        "object": new,

    }
    return render(request, 'article/detail.html', context)