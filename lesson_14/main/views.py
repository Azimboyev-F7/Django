from django.shortcuts import render

# Create your views here.

def index(request):
    context = {

    }
    return render(request, "article/index.html", context)


def articles(request):
    context = {

    }
    return render(request, "article/articles.html", context)