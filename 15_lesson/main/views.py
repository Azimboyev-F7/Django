from django.db.models.fields import return_None
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import New
from .form import NewForm

# Create your views here.


def index(request):
    news = New.objects.all()
    context = {
        'news': news
    }
    return render(request, 'article/index.html', context)

def article(request):
    news = New.objects.all()

    query = request.GET.get('q')
    if query:
        news = New.objects.filter(title__icontains=query)
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

# def create(request):
#
#     if request.method == "POST":
#         New.objects.create(title=request.POST['title'], content=request.POST['content'])
#         messages.success(request, 'New successfully created!')
#         return redirect('main:article')
#     context = {
#         "object": New.objects.all(),
#     }
#     return render(request, 'article/create.html', context)


def create_form(request):
    form = NewForm()
    if request.method == "POST":
        form = NewForm(request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Article successfully created!')
            return redirect('main:article')


    context = {
        "object": New.objects.all(),
        'form': form,
    }
    return render(request, 'article/create.html', context)


def remove(request, pk):
    articles = New.objects.get(id=pk)
    if request.method == "POST":
        articles.delete()
        messages.error(request, 'Article successfully removed!')
        return redirect('main:article')

    context = {
        "object": articles,
    }

    return render(request, 'article/delete.html', context)
