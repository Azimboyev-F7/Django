from django.shortcuts import HttpResponse


def index(request):
    text = "Hello User This context faced some problems please wait!!!"
    return HttpResponse(text)