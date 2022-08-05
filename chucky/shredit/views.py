from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm



def index(request):
    return render(request, 'shredit/index.html')

def home(request):
    return render(request, 'shredit/homepage.html')

def about_us(request):
    return render(request, 'shredit/about.html')

def contact_us(request):

    contact_form = ContactForm()

    if request.method == 'POST':
        contact_form = ContactForm(request.POST)

        if contact_form.is_valid():
            sent = contact_form.send()

            if sent is not None:
                messages.success(request, 'Message sent successfully')
                return redirect('shredit:contact')
            else:
                messages.error(request, 'Message failed!')
                return redirect('shredit:contact')

    context = {'form':contact_form}
    return render(request, 'shredit/contact.html', context)