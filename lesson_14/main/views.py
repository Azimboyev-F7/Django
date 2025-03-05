from django.http import HttpResponse
from django.shortcuts import render

from main.models import Article


# Create your views here.

def index(request):
    context = {

    }
    return render(request, "article/index.html", context)


def articles(request):
    articles = Article.objects.all()

    query = request.GET.get("q")
    if query:
        articles = articles.filter(title__icontains=query)

    context = {
        'articles': articles,
    }
    return render(request, "article/articles.html", context)

def detail(request, pk):
    article = Article.objects.get(id=pk)
    context = {
        'article': article,
    }
    return render(request, "article/detail.html", context)

def create(request):

    if request.method == "POST":
        article = Article.objects.create(title=request.POST["title"], content=request.POST["content"])
        return HttpResponse(content='Article created successfully! <a href="../">Go home</a>')
    context = {
        'object_list': Article.objects.all(),
    }
    return render(request, "article/create.html", context)