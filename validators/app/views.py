from django.shortcuts import render
from app.forms import *
from django.http import *

# Create your views here.


def insertform(request):
    SFEO= SchoolForm
    d={'SFEO':SFEO}
    if request.method=='POST':
        SFO=SchoolForm(request.POST)
        if SFO.is_valid():
            sname=SFO.cleaned_data.get('sname')
            sprincipal=SFO.cleaned_data.get('sprincipal')
            saddress=SFO.cleaned_data.get('saddress')
            SO=School(sname=sname,sprincipal=sprincipal,saddress=saddress)
            SO.save()
            return HttpResponse('Insert Data is Done')
        return HttpResponse('Invali Data')
    return render(request,'insertform.html',d)