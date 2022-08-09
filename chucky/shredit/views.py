from django.contrib.auth.decorators import login_required
from .forms import ContactForm, FileUploadForm
from django.shortcuts import render, redirect
from django.contrib import messages
from .utils import Shredding
from .models import Shredit


def index(request):
    return render(request, 'shredit/index.html')


@login_required(login_url='/author/login/')
def home(request):
    form = FileUploadForm()

    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)

        if form.is_valid():
            file = request.FILES.get('file')
            chunk_num = form.cleaned_data.get('chunk_num')
            size_type = form.cleaned_data.get('size_type')

            proccessed_file = Shredding.processing_file(
                request, file, chunk_num, size_type)
            if proccessed_file:
                ins = Shredit.objects.create(
                    owner=request.user,
                    _file_name=file.name,
                    chucked_file=proccessed_file,
                    size_type=size_type,
                    chunk_num=chunk_num,
                )
                print(ins.file_size, ins.file_name)
                messages.success(request, f'{file.name} shredded sucessfully')
                return redirect('shredit:index-page')
    return render(request, 'shredit/about.html', {'form': form})


def about_us(request):
    return render(request, 'shredit/about.html')


def contact_us(request):

    contact_form = ContactForm()

    if request.method == 'POST':
        contact_form = ContactForm(request.POST)

        if contact_form.is_valid():
            sent = contact_form.send()
            print(sent)
            if sent is not None:
                messages.success(request, 'Message sent successfully')
                return redirect('shredit:contact')
            else:
                messages.error(request, 'Message failed!')
                return redirect('shredit:contact')

    context = {'form': contact_form}
    return render(request, 'shredit/contact.html', context)
