from django.shortcuts import render

# Create your views here.

def index(request):
    context = {}
    return render(request, 'index.html', context)

def blogs(request):
    context = {}
    return render(request, 'blogs.html', context)
