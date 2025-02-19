from django.shortcuts import render
from .models import New


# Create your views here.

def index(request):
    news = New.objects.all()

    context = {
        "news": news
    }

    return render(request, "article/index.html", context)

def blog(request):
    news = New.objects.all()
    context = {
        "news": news
    }

    return render(request, "article/blog.html", context)

def details(request):
    news = New.objects.get(id=id)

    context = {
        "news": news
    }
    return render(request, details, context)