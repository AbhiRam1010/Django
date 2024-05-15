from django.shortcuts import render
from django.http import HttpResponse
from app.forms import *
from app.models import *
# Create your views here.

def register(request):
    ECFO = CredForm()
    d = {'ECFO':ECFO}
    if request.method == 'POST' and request.FILES:
        CFDO = CredForm(request.POST, request.FILES)
        if CFDO.is_valid():
            name = CFDO.cleaned_data.get('name')
            pno = CFDO.cleaned_data.get('pno')
            email = CFDO.cleaned_data.get('email')
            un = CFDO.cleaned_data.get('username')
            pw = CFDO.cleaned_data.get('password')
            photo = CFDO.cleaned_data.get('profile')
            CO = Credential(name = name, pno = pno, email = email, username = un, password = pw, profile=photo)
            CO.save()
            return render(request,'login.html')
        return HttpResponse('Invalid Data') 
    return render(request, 'register.html', d)


def login(request):
    if request.method == 'POST':
        un = request.POST.get('un')
        pw = request.POST.get('pw')
        CO = Credential.objects.filter(username=un, password=pw)
        if CO:
            d = {'CO':CO}
            return render(request, 'home.html',d)
        return HttpResponse('Invalid Credentials')
    return render(request, 'login.html')