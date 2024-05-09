from django.shortcuts import render
from app.form import *
from django.http import HttpResponse
# Create your views here.

def inserttopicform(request):
    TFEO= Topicform
    d={'TFEO':TFEO}            
    if request.method==  'POST':
            TFDO=Topicform(request.POST)
            if TFDO.is_valid():
                TFDO.save()
                return HttpResponse('Done')
            return HttpResponse('INVALID DATA')
    return render(request,'iserttopic.html',d)
        
def insertwebsite(request):
    WFEO= Websiteform
    d={'WFEO':WFEO}
    if request.method == 'POST':
        WFDO= Websiteform(request.POST)
        if WFDO.is_valid:
            WFDO.save()
            return HttpResponse('done')
        return HttpResponse('INVALID DATA')
    return render (request,'website.html',d)


def insertauthor(request):
    AFEO=Accessform
    d={'AFEO':AFEO}
    if request.method == 'POST':
        AFDO=Accessform(request.POST)
        if AFDO.is_valid():
            AFDO.save()
            return HttpResponse("DONE")
        return HttpResponse('INVALID DATA')
    return render (request,'author.html',d)