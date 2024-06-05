from django.shortcuts import render
from .forms import *
from django.http import HttpResponse
from django.contrib.auth import authenticate,login
# Create your views here.
def home(request):
    return render(request,'home.html')

def user_regitration(request):
    EUFO= CostumerForm()
    d={'EUFO':EUFO}
    if request.method == 'POST':
        UFDO=CostumerForm(request.POST)
        if UFDO.is_valid():
            pw=UFDO.cleaned_data['password']
            MFDO=UFDO.save(commit=False)
            MFDO.set_password(pw)
            MFDO.save()
            return HttpResponse('You are registered to Zomato')
    return render(request,'user_regitration.html',d)

def user_login(request):
    if request.method == 'POST':
        un=request.POST.get('un')
        pw=request.POST.get('pw')
        UO=User.objects.get(username=un)
        AMO=authenticate(username=un,password=pw)
        if AMO and AMO.is_active:
            login(request,AMO)
            request.session['username']=un
            if UO.is_staff :
                return render (request,'additem.html')
            return HttpResponse('you are logged in to zomato')
    return render (request,'login.html')