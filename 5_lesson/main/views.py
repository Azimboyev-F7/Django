from django.shortcuts import render
from django.http import HttpResponse
from main.models import Workers, Students

from main.models import Workers


# Create your views here.

def index(request):
    workers = Workers.objects.all()
    workers.create(
        name="Faxriyorrrr",
        second_name="Azimov",
        email="fazogir@gmail.com",
        phone=+998903585202,
    )
    students = Students.objects.all()
    students.create(
        name="Fazogir",
        second_name="Azimov",
        email="fazogir@gmail.com",
        phone=+998903585202,
    )

    context = {}
    return render(request, 'index.html', context)


