from django.http import HttpResponse,Http404
from django.shortcuts import render
from home.models import contact



def index(request):
    return render(request, 'home1.html')


def about(request):
    return render(request, 'about.html')


def contacts(request):
    if request.method=="POST":
        name1=request.POST['name']
        phone1=request.POST['phone']
        email1=request.POST['email']
        Desc1=request.POST['desc']
       # print(name,phone,email,Desc)
        ins=contact(name=name1,phone=phone1,email=email1, desc=Desc1)
        ins.save() 
        print("Data saved sucessfully")
    return render(request, 'contact.html')
