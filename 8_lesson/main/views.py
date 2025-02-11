from django.shortcuts import render
from .models import Post

def main(request):
    news = Post.objects.all()
    Post.objects.all().delete
    context = {"posts": news}
    return render(request,"index.html", context)