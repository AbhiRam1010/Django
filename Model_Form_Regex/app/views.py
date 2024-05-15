from django.shortcuts import render
from app.forms import *
from django.http import HttpResponse

# Create your views here.

def register(request):
    ECFO= CredForm()
    d={'ECFO':ECFO}
    if request.method == 'POST':
        CFO=CredForm(request.POST)
        if CFO.is_valid():
            CFO.save()
            return HttpResponse ('Done')
        return HttpResponse('Invalid Data')
    return render (request,'register.html',d)