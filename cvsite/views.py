from django.http import Http404
from django.shortcuts import render
from .models import cvelement
import mimetypes
import os
from django.http.response import HttpResponse


def cvsite(request):
    cvelements = cvelement.objects.all()
    return render(request, 'cvsite/homepage.html', {'cvelements': cvelements})
    
def contatti(request):
    return render(request, 'cvsite/contatti.html') 
def cv(request):
    return render(request, 'cvsite/cv.html') 
def download_file(request):
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
		# Modifica filename con il nome e l'estensione del file che vuoi far scaricare	
    filename = 'cv.pdf'
    filepath = BASE_DIR + '/download/' + filename
    path = open(filepath, 'rb')
    mime_type, _ = mimetypes.guess_type(filepath)
    response = HttpResponse(path, content_type=mime_type)
    response['Content-Disposition'] = "attachment; filename=%s" % filename
    return response
def details(request, cvelement_id):

    try:
        element = cvelement.objects.get(pk=cvelement_id)

    except cvelement.DoesNotExist:
        raise Http404("CV element does not exist")
    return render(request, 'cvsite/details.html', {'element': element})
def blog(request):
    return render(request, 'cvsite/blog.html')   
def art1(request):
    return render(request, 'cvsite/art1.html')