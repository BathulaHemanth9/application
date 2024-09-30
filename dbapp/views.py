from django.shortcuts import render,redirect
from django.http import HttpResponse
from.models import employee,department
from django.db.models import Q

# Create your views here.
def dbprocess(request):
    if request.method=='GET':
        return HttpResponse('db got request')

def dbinsert(request):
    if request.method == 'GET':
        dept=department.objects.all()
        return render(request,'dbapp/insert.html',{'departments':dept})
    
    if request.method =='POST':
        eno=int(request.POST['eno'])
        ename=request.POST['ename']
        sal=int(request.POST['sal'])
        edept=int(request.POST['dept'])
        dept=department.objects.get(deptno=edept)

        emp=employee(empno=eno,empname=ename,salary=sal,department=dept,profile_pic=request.FILES['pic'])
        emp.save()
        return redirect('selectemployeeurl')
def dbselect(request):
    if request.method =='GET':
        empobjects=employee.objects.all()
        print(empobjects)
        return render(request,'dbapp/select.html',{'emps':empobjects})

def dbupdate(request,emno):
    if request.method ==  'GET':
        empdata=employee.objects.get(empno=emno)
        dept=department.objects.all()
        return render(request,'dbapp/update.html',{'eupdate':empdata,'departments':dept})

    if request.method == 'POST':
        eno=int(request.POST['eno1'])
        ename=(request.POST['ename1'])
        sal=int(request.POST['sal1'])
        edept=int(request.POST['dept'])
        print(request.FILES)
        dept=department.objects.get(deptno=edept)
        obj=employee(empno=eno,empname=ename,salary=sal,department=dept,profile_pic=request.FILES['pic'])
        obj.save()
        return redirect('selectemployeeurl')


'''def dbupdate2(request):
    if request.method == 'POST':
        eno=int(request.POST['eno1'])
        ename=(request.POST['ename1'])
        sal=int(request.POST['sal1'])

        obj=employee(empno=eno,empname=ename,salary=sal)
        obj.save()
        return render(request,'dbapp/update.html',{'message':'Update successfully'})'''

def dbdelete(request,emno1):
    print(request.method)
    if request.method == 'GET':
        print(request.emno)
        print("hI")
        empdata=employee.objects.get(empno=emno1)
        return render(request,'dbapp/delete.html',{'emdata':empdata})
    
    if request.method == 'POST':
        empdata=employee.objects.get(empno=emno1)
        empdata.delete()
        return redirect('selectemployeeurl')

def dbsearch(request):
    if request.method == 'POST':
        minsal=int(request.POST['minsal'])
        maxsal=int(request.POST['maxsal'])
        empdata=employee.objects.filter(Q(salary__gt=minsal) & Q(salary__lt=maxsal))
        return render(request,'dbapp/select.html',{'emps':empdata})

def dbdetail(request,eno):
    obj=employee.objects.get(empno=eno)
    return render(request,'dbapp/detail.html',{'data':obj})
