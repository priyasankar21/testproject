from django.shortcuts import render
from django.http import HttpResponse,Http404
from .models import *
from .forms import *
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponseRedirect
def index(request):
    return render(request, 'index.html')

def home(request):
    machines=detail.objects.all()
   
    return render(request, 'home.html',{'machines':machines})

def buy(request,m_name):
    machine=detail.objects.get(Machine_name=m_name)
    if request.method=="POST":
        form=myform1(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            c_name=form.cleaned_data['Company_name']
            no=str(form.cleaned_data['Mobile_number'])
            message=c_name +" has shown interest for buying " +machine.Machine_name +"\ncontact number:" + no
            send_mail('interest shown by ',message,'jeevighashri@gmail.com',['jeevighashri@gmail.com'],fail_silently=False)
    else:
        form=myform1() 
    return render(request, 'buy.html',{'machine':machine,'form': form})


def sells(request):
    print("hello")
    if request.method=="POST":
        form=myform(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/index/sell/')
    else:
        form=myform()
    return render(request, 'sel.html',{'form': form})


def contact(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form=ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            from_email =str( form.cleaned_data['from_email'])
            phone_number = str(form.cleaned_data['phone_number'])
            messages = form.cleaned_data['messages']
            message= "Name: " +name +"\nPhone number: " + phone_number+"\nEmail: "+from_email+"\nmessage:\n"+messages
            try:
                send_mail('Got a Message!!',message,from_email,['jeevighashri@gmail.com'],fail_silently=False)
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return HttpResponseRedirect('/index/contact/')
        else:
            form=myform1() 
    return render(request, 'contact.html',{'form': form})
    
