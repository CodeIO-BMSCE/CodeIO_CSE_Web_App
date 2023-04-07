from django.shortcuts import render, redirect
from django.http import HttpResponse, FileResponse, Http404
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
import os

MESSAGE_TAGS = {
    messages.DEBUG: 'alert-info',
    messages.INFO: 'alert-info',
    messages.SUCCESS: 'alert-success',
    messages.WARNING: 'alert-warning',
    messages.ERROR: 'alert-danger',
}

# Create your views here.
def home(request):
    if request.method == 'POST' and request.POST['resource']:
        semester = request.POST.get("semester")
        course = request.POST.get("course")
        notes = request.POST.get("resource")
        path=f'media/{semester}/{course}/{notes}'
        try:
            file_list = os.listdir(path)
        except:
            file_list = []
        path2 = f'{semester}.{course}.{notes}.'
        return render(request, 'notes_and_qp_mgmt/view_notes/view_notes.html', {'files': file_list, 'path': path2})
    return render(request, "notes_and_qp_mgmt/view_notes/view_notes.html")


def upload(request):
    if request.method == 'POST' and request.FILES['upload']:
        upload = request.FILES.getlist('upload')
        semester = request.POST.get("semester")
        course = request.POST.get("course")
        notes = request.POST.get("notes")
        fss = FileSystemStorage(location=f'media/{semester}/{course}/{notes}/')
        for x in upload:
            file = fss.save(x.name, x)
        file_url = fss.url(file)
        return render(request, "notes_and_qp_mgmt/upload/index.html", {'file_url': file_url})
    return render(request, "notes_and_qp_mgmt/upload/index.html")


def pdf_view(request, path, file):
    try:
        path = path.replace(".", "/")
        return FileResponse(open('media/'+ path + file, 'rb'), content_type='application/pdf')
    except FileNotFoundError:
        raise Http404()