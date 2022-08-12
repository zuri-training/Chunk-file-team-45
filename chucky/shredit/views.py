from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import ContactForm, UploadForm
from django.http import HttpResponse
from django.contrib import messages
from django.http import Http404
from .utils import Shredding
from .models import Shredit


def index(request):
    return render(request, 'shredit/index.html')


@login_required(login_url='/author/login/')
def home(request):

    files = Shredit.objects.filter(owner=request.user)
    resent_file = files.order_by('-updated').first()
    upload_form = UploadForm()

    if request.method == 'POST':
        upload_form = UploadForm(request.POST, request.FILES)

        if upload_form.is_valid():
            file = request.FILES.get('file')
            chunk_num = upload_form.cleaned_data.get('chunk_num')
            size_type = upload_form.cleaned_data.get('size_type')

            proccessed_file = Shredding.processing_file(
                request,
                file,
                chunk_num,
                size_type
            )
            if proccessed_file:
                Shredit.objects.create(
                    owner=request.user,
                    _file_name=file.name,
                    chucked_file=proccessed_file,
                    size_type=size_type,
                    chunk_num=chunk_num,
                )
                messages.success(
                    request, f'{file.name} chuncking was sucessful')
                return redirect('shredit:dashboard')
            else:
                messages.error(
                    request, f'{file.name} chunking was not sucessful')
                return redirect('shredit:dashboard')

    context = {'upload_form': upload_form,
               'activities': files, 'resent_file': resent_file, }
    return render(request, 'shredit/homepage.html', context)


@login_required(login_url='/author/login/')
def download(request, id=None):
    try:
        file_ins = Shredit.objects.get(id=id)
    except Shredit.DoesNotExist:
        raise Http404

    context = {'file_ins': file_ins}

    return render(request, 'shredit/download.html', context)


@login_required(login_url='/author/login/')
def download_file(request, id=None):
    try:
        file_ins = Shredit.objects.get(id=id)
        fl_path = file_ins.chucked_file.path
        filename = file_ins.chucked_file.name

        zip_file = open(fl_path, 'rb')
        response = HttpResponse(
            zip_file, content_type='application/force-download')
        response['Content-Disposition'] = 'attachment; filename="%s"' % filename
        return response
    except:
        raise Http404


def about_us(request):
    return render(request, 'shredit/about.html')


def docs_page(request):
    return render(request, 'shredit/docs.html')


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

    context = {'form': contact_form}
    return render(request, 'shredit/contact.html', context)


def share_page(request):
    return render(request, 'shredit/share.html')


def page_404(request, exception):
    return render(request, "404.html")
