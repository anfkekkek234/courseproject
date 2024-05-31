from django.shortcuts import render , HttpResponse , HttpResponseRedirect
from website.models import *
from website.forms import *
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request,'website/index.html')

def about(request):
    return render(request,'website/about.html')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.name = "unknown"
            form.save()
            messages.add_message(request,messages.SUCCESS,'Thank you for contacting us.')
        else:
            messages.add_message(request,messages.ERROR,'Something went wrong.')
    form = ContactForm()
    return render(request,'website/contact.html',{'form':form})

def subscribe_view(request):
    if request.method == 'POST':
        form = SubscribeForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Your ticket subscribe successfully.')

            return HttpResponseRedirect('/')
    else:
        messages.add_message(request, messages.ERROR, 'your ticket didnt subscribe')
        return HttpResponseRedirect('/')