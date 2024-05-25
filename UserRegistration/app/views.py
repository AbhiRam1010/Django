from django.shortcuts import render
from app.forms import *
from django.http import HttpResponse
from django.core.mail import send_mail
from django.contrib.auth import authenticate
from django.contrib.auth import login
import random
# Create your views here.


def register(request):
    EUFO=UserForm()
    EPFO=ProfileForm()
    d={'EUFO':EUFO,'EPFO':EPFO}
    if request.method == 'POST'and request.FILES:
        UFDO=UserForm(request.POST)
        PFDO=ProfileForm(request.POST, request.FILES)
        if UFDO.is_valid() and PFDO.is_valid():
            pw=UFDO.cleaned_data.get('password')
            MUFDO=UFDO.save(commit=False)
            MUFDO.set_password(pw)
            MUFDO.save()
            MPFDO=PFDO.save(commit=False)
            MPFDO.username=MUFDO
            MPFDO.save()
            message=f"Hello Your registration is done successfully"
            email=UFDO.cleaned_data.get('email')
            send_mail('Registration',message,'abhirammohapatra25@gmail.com',[email],fail_silently=False)
            return render(request,'user_login.html')
        return HttpResponse('Invalid data')
    return render(request,'register.html',d)


def user_login(request):
    if  request.method== 'POST':
        un=request.POST.get('un')
        pw=request.POST.get('pw')
        AUO=authenticate(username=un,password=pw)
        if AUO:
                login(request,AUO)
                d={'AUO':AUO}
                request.session['un']=un
                return render(request,'home.html',d)
        return HttpResponse('Invalid Credentials')    
    return render (request,'user_login.html')
                


def user_profile(request):
    try: 
        un=request.session['un']
        UO=User.objects.get(username=un)
        d={'UO':UO}
        request.session.modified=True
        return render(request,'user_profile.html',d)
    except KeyError:
        return HttpResponse('Key error')
    
   
def change_password(request):
    if request.method == 'POST':
        np= request.POST.get('np')
        cp= request.POST.get('cp')
        if cp!=np:
            return HttpResponse("Password doesn't match /n Reconfirm Your Password")
        send_otp=str(random.randint(100000,999999))
        my_mail='abhirammohapatra25gmail.com'
        un=request.session['un']
        UO=User.objects.get(username=un)
        send_mail('OTP',send_otp,my_mail,[UO.email],fail_silently=False)
        request.session['cp']=cp
        request.session['otp']=send_otp
        return render(request,'otp.html')
        
    return render (request,'change.html')

def otp(request):
    if request.method =='POST':
        get_otp=request.POST.get('otp')
        un=request.session['un']
        send_otp=request.session['otp']
        if un is None or send_otp is None:
            return HttpResponse('Session data not found. Please try again.')
        if get_otp==str(send_otp):
            UO=User.objects.get(username=un)
            UO.set_password(request.session['cp'])
            UO.save()
            return HttpResponse('Password_changed')
        return HttpResponse(send_otp)
    return render (request,'otp.html')






def home(request):
    return render(request,'home.html')
        