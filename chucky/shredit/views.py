from django.shortcuts import render

def index(request):
    return render(request, 'shredit/index.html')

def home(request):
    return render(request, 'shredit/homepage.html')