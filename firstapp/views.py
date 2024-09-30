from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def function(request):
    if request.method=='POST':
        print(request.POST)
        return HttpResponse(request.POST['t1'])
    return render(request,'first.html')

def mathtable(request):
    if request.method == 'GET':
        return render(request,'math.html')
    
    if request.method == 'POST':
        num=int(request.POST['t2'])
        output=''
        result=[]
        for i in range(1,11):
            output=str(i)+'*'+str(num)+'='+str(num*i)
            result.append(output)
        return render(request,'math.html',{'result':result})
