from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def display(request):
    return render(request,'vcube.html')


def addition(request):
    if request.method=='GET':
        return render(request,'add.html')
    if request.method=='POST':
        val1=int(request.POST['t1'])
        val2=int(request.POST['t2'])
        if 'add' in request.POST:
            res=val1+val2
            action='Addition'
        elif 'sub' in request.POST:
            res=val2-val1
            action='Substraction'
        elif 'mul' in request.POST:
            res=val1*val2
            action='Multiplication'
        else:
            res=val2//val1
            action='Division'
        return render(request,'add.html',{'result':res,'action':action})
