
from os import getlogin
import re
from django.contrib import auth
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse
from traitlets import Instance

from users.forms import ProfileForm, UserRegistrationForm, UserloginForm

def login(request):
    if request.method == 'POST':
        form = UserloginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('main:index'))
    else:
        form = UserloginForm()
    context = {
        'title': 'Home - Авторизация',
        'form': form
    }
    return render(request, 'users/login.html', context)

def registration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            user = form.instance
            auth.login(request, user)
            return HttpResponseRedirect(reverse('main:index'))
    else:
        form = UserRegistrationForm()
        
    context = {
        'title': 'Home - Регистрация',
        'form': form 
    }
    return render(request, 'users/registration.html', context)


def profile(request):
    if request.method == 'POST':
        form = ProfileForm(data=request.POST, instance=request.user, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('user:profile'))
    else:
        form = ProfileForm(instance=request.user)
    
    
    
    context = {
        'title': 'Home - Кабинет',
        'form': form
    }
    return render(request, 'users/profile.html', context)

def users_cart(request):
    return render(request, 'users/users_cart.html')


def logout(request):
    auth.logout(request)
    return redirect(reverse('main:index'))