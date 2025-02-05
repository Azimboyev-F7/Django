from django.shortcuts import render
from django.http import HttpResponse
from main.models import Workers

from main.models import Workers


# Create your views here.

def index(request):
    workers = Workers.objects.all()
    Workers.objects.get(id=1).delete()
        # name="Faxriyorrr",
        # second_name="Azimov",
        # email="fazogir@gmail.com",
        # phone=+998903585202,

    context = {}
    return render(request, 'index.html', context)


