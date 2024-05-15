from django.shortcuts import render
from app.forms import * 
from django.http import HttpResponse
# Create your views here.


def register(request):
    EUFO=Userform()
    EPFO=Profileform()
    d={'EUFO':EUFO,'EPFO':EPFO}
    if request.method =='POST' and request.FILES:
        UFDO=Userform(request.POST)
        PFDO=Profileform(request.POST, request.FILES)
        if UFDO.is_valid():
            MUFDO=UFDO.save(commit=False)
            pw=UFDO.cleaned_data.get('password')
            MUFDO.set_password(pw)
            MUFDO.save()
            MPFDO=PFDO.save(commit=False)
            MPFDO.username=UFDO
            MPFDO.save()
            return HttpResponse(request,'User registered successfully')
        return HttpResponse('Invalid Input')
    return render (request,'register.html',d)
    