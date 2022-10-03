from django.shortcuts import render
from .models import cvelement

def cvsite(request):
    cvelements = cvelement.objects.all()
    return render(request, 'cvsite/homepage.html', {'cvelements': cvelements})
    
def contatti(request):
    return render(request, 'cvsite/contatti.html')   
