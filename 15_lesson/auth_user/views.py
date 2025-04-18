from django.shortcuts import render, redirect

# Create your views here.k

from django.contrib import auth
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from .forms import MyUserCreationForm

def login_view(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'You are now logged in')
            return redirect('main:article')
        else:
            messages.error(request, 'Invalid credentials')

    context = {

    }

    return render(request, 'auth/login.html', context)

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        messages.success(request, 'You are now logged out')
        return redirect('main:article')

    context = {}

    return render(request, 'auth/logout.html', context)

def register_view(request):
    form = MyUserCreationForm()
    if request.method == 'POST':
        form = MyUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'You are now registered')
            return redirect('auth_user:login')

    context = {
        'form': form,
    }

    return render(request, 'auth/register.html', context)