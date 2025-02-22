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

def detail(request):
    news = New.objects.get(pk=id)
    context = {
        'id': news.id,
    }
    return render(request, 'article/detail.html', context)