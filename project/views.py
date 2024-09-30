from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import UserCreationForm


# Create your views here.

def loginuser(request):
    if request.method == 'GET':
        return render(request,'project/login.html')

    if request.method == 'POST':
        uname=request.POST['uname']
        pwd=request.POST['pwd']
        
        user=authenticate(request,username=uname,password=pwd)
        
        if user !=None:
            login(request,user)
            return render(request,'project/welcome.html ')
        else:
            return redirect('loginpurl')

def logoutuser(request):
    logout(request)
    return redirect('loginurl')

def signup(request):
    if request.method == 'GET':
        emptyform= UserCreationForm()
        return render(request,'project/sign.html',{'form':emptyform})
    
    if request.method == 'POST':
        dataform = UserCreationForm(request.POST)
        if dataform.is_valid() == True:
            dataform.save()
            return redirect('loginpurl')
        else:
            return render(request,'project/sign.html',{'form':dataform})
