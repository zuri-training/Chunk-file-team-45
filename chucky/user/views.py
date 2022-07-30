
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

            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            password2 = form.cleaned_data['password2']
            User = authenticate(username=username, password=password)
        if password != password2:
            messages.error(request, 'Password doesn\'t match')
            return redirect('registration.html')
        elif User.objects.filter(username=username.exists()):
            messages.error(request, 'Username already exist')
        else:
            User = User.objects.get(username)
            User.set_password(password)
            User = form.save()

        login(request, User)
        messages.success(request, 'Registration Successful')
        return redirect('home.html')

    else:
        form = UserCreationForm()

    return render(request, 'registration.html', {form: forms})


def login_view(request):

    if request.method == 'Post':
        username = request.Post['username']
        password = request.Post['password']
        User = authenticate(request, username=username, password=password)

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
    return redirect('index.html')

def home(request):
    return render (request, 'home.html')