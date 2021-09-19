from django.shortcuts import render
from django.http import HttpResponse
import datetime
from .forms import  *


def satInfo(request):
    form=SatDetailForm()
    if request.method == 'POST':
        form = SatDetailForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return input(request)
        else:
            print("ERROR FORM INVALID")
    else:
        form = SatDetailForm()  # new form to the user
    return render(request,'check/satinfo/display.html',{'form':form})   



def input(request):
    form=pids_input()
    if request.method == 'POST':
        form = pids_input(request.POST,request.FILES)
        if form.is_valid():
            form.save(commit=True)
            return satInfo(request)
        else:
            print("ERROR FORM INVALID")
    else:
        form = pids_input()  # new form to the user
    return render(request,'check/satinfo/display.html',{'form':form})   


def base(request):

    return render(request,'hello.html',{'form':"anjv"})  


