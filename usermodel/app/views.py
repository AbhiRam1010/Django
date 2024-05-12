from django.shortcuts import render
from app.forms import  *
from django.http import HttpResponse
# Create your views here.


def insert_user(request):
    EUFO=UserForm()
    d={'EUFO':EUFO}
    if request.method=='POST':
        UFDO= UserForm(request.POST)
        if UFDO.is_valid():
           pw=UFDO.cleaned_data.get('password')
           MUFDO= UFDO.save(commit=False)
           MUFDO.set_password(pw)
           MUFDO.save()
           return HttpResponse('Done')
        return HttpResponse('Invalid data')
    return render(request,'insert_user.html',d)