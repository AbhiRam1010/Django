from django.shortcuts import render
from django.http import HttpResponse
from app.models import Emp
# Create your views here.

def home(request):
    # return HttpResponse("Anything on this page")
    EO=Emp.objects.all() 
    dick={'EO':EO}
    return render(request,'home.html',dick)

def register(request):
    if request.method=='POST':
        name= request.POST.get('ename')
        pno= request.POST.get('pno')
        email= request.POST.get('email')
        add= request.POST.get('add')
        un = request.POST.get('un')
        pw = request.POST.get('pw')
        EO = Emp(ename= name, pno=pno,email=email,add=add, un=un, pw=pw)
        EO.save()
        return render(request,'login.html')
    return render(request,'register.html')

def login(requst):  
    if requst.method == 'POST':
        un= requst.POST.get('un')
        pw= requst.POST.get('pw')
        EO=Emp.objects.all()
        for user in EO:
            if user.un==un:
                if user.pw==pw:
                    O={'obj':EO}
                    return render(requst,'home.html',O)
                return HttpResponse("password doesnot matched")
        else:
            return HttpResponse('Username doesnot match')
    return render(requst,'login.html')       