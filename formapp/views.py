from django.shortcuts import render,redirect
from.forms import Firstform
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def firstform(request):
    if request.method == 'GET':
        emptyform = Firstform()
        return render(request,'formapp/firstform.html',{'form':emptyform})
    
    if request.method == 'POST':
        dataform = Firstform(request.POST)
        emptyform=Firstform()

        if dataform.is_valid() == True:
            v1 = dataform.cleaned_data['value1']
            v2 = dataform.cleaned_data['value2']
            res = v1+v2
            return render(request,'formapp/firstform.html',{'result':res,'form': emptyform})
        else:
            return render(request,'formapp/firstform.html',{'form':dataform})

def loginuser(request):
    if request.method == 'GET':
        return render(request,'formapp/login.html')
    
    if request.method == 'POST':
        uname=request.POST['uname']
        pwd=request.POST['pwd']
        
        user=authenticate(request,username=uname,password=pwd)

        if user != None:
            login(request,user)
            return redirect('selectemployeeurl')
        else:
            return redirect('loginurl')

def logoutuser(request):
    logout(request)
    return redirect('loginurl')

def signupuser(request):
    if request.method == 'GET':
        emptyform= UserCreationForm()
        return render(request,'formapp/signup.html',{'form':emptyform})
    
    if request.method == 'POST':
        dataform = UserCreationForm(request.POST)
        if dataform.is_valid() == True:
            dataform.save()
            return redirect('loginurl')
        else:
            return render(request,'formapp/signup.html',{'form':dataform})
