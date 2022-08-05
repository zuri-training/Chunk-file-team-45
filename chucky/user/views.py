
from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .forms import UserCreateForm, UserLoginForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout


def register(request):
    
    if request.user.is_authenticated:
        return redirect('shredit:dashboard')
    
    form = UserCreateForm()
    if request.method == 'POST':
        form = UserCreateForm(request.POST)
        
        if not (agree := request.POST.get('agree')):
            messages.error(request, "You cannot access this platform if you do not agree to terms of services")
            return redirect('user:user-register')

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            email = form.cleaned_data['email']
            
            user = User.objects.create_user(
                            username=username,
                            password=password,
                            email=email
                            )
            messages.success(request, 'Registration Successful')
            
            login(request, user)
            return redirect('shredit:dashboard')

        else:
            messages.error(request, "An error occurred during registration")

    context = {'form':form}

    return render(request, 'user/registration.html', context)

def signin_view(request):

    if request.user.is_authenticated:
        return redirect('shredit:dashboard')

    form = UserLoginForm()
    
    if request.method == 'POST':
        form = UserLoginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")

            user = authenticate(request, username=username, password=password)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    messages.success(request, 'Login was successful')
                    return redirect('shredit:dashboard')
            
            else:
                messages.error(request, 'Invalid Credentials')
                return redirect('user:user-login')
        
    context = {'form':form}
    return render(request, 'user/login.html', context)

@login_required(login_url='/author/login/')
def signout_view(request):
    logout(request)
    messages.success(request, 'You logged out' )
    return redirect('shredit:index-page')