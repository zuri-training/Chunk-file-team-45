import email
from django.shortcuts import render, redirect
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout


# Create your views here.

def register_view(request):

    if request.method == 'Post':
        form = UserCreationForm(request.Post)
        if form.is_valid():
            User = form.save()

        email = form.cleaned_data['email']
        password = form.cleaned_data['password']
        User = authenticate(email=email, password=password)

        login(request, User)
        messages.success(request, 'Registration Successful')
        return redirect('home.html')

    else:
        form = UserCreationForm()

    return render(request, 'register.html', {form: forms})


def login_view(request):

    if request.method == 'Post':
        email = request.Post['email']
        password = request.Post['password']
        User = authenticate(request, email=email, password=password)

        if User is not None:
            login(request,User)
            return redirect('home.html')
        else:
            messages.error(request, 'Invalid Username or Password')
            return redirect('login.html')

    else:
        return render(request, 'login.html')


def logout_view(request):
    logout(request)
    messages.success(request, 'You logged out' )
    return redirect('main.html')

def home(request):
    return render (request, 'home.html')