from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.response import Response
from dbapp.models import employee
from.serializers import EmpSerializer
from rest_framework.decorators import api_view
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST, HTTP_200_OK
import time
from rest_framework.decorators import authentication_classes,permission_classes
# Create your views here.
'''
def getemployeeapi(request):

    data = employee.objects.all()
    empdata = [{'empno':obj.empno,'empname':obj.empname,'salary':obj.salary} for obj in data]

    return JsonResponse(empdata , safe=False)'''

def internalprocessing():
    print('Internal processing is started')
    time.sleep(5)
    print('Internal processing is ended')

@api_view(['GET','POST'])
def getemployeeapi(request):
    if request.method == 'GET':
        #internalprocessing()
        emps = employee.objects.all()
        empdata = EmpSerializer(emps,many =True)
        return Response(empdata.data)

    if request.method == 'POST':
        empdata = EmpSerializer(data=request.data)
        if empdata.is_valid() == True:
            empdata.save()
            return Response(status = HTTP_201_CREATED)
        else:
            return Response(empdata.errors,status = HTTP_400_BAD_REQUEST)

@api_view(['PUT','GET','DELETE'])
def modifyemployeeapi(request,pk):
    print("hooo")
    print(request.method)
    emps = employee.objects.get(empno = pk)
    if request.method == 'PUT':
        empdata= EmpSerializer(emps,data=request.data)

        if empdata.is_valid() == True:
            empdata.save()
            return Response(status = HTTP_200_OK)
        else:
            return Response(empdata.errors,status = HTTP_400_BAD_REQUEST)
    if request.method == 'GET':
        empdata = EmpSerializer(emps)
        print(empdata.data)
        return Response(empdata.data)
        
    if request.method == 'DELETE':
        print("Hi")
        emps = employee.objects.get(empno = pk)
        emps.delete()
        return Response(status = HTTP_200_OK)

