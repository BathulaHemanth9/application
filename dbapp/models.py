from django.db import models

# Create your models here.

class department(models.Model):
    deptno=models.IntegerField(primary_key=True)
    deptname=models.CharField(max_length=20)
    location=models.CharField(max_length=20)
    def __str__ (self):
        return self.deptname

class employee(models.Model):
    empno = models.IntegerField(primary_key=True)
    empname = models.CharField(max_length=20)
    salary = models.IntegerField()
    department=models.ForeignKey(department,null=True,on_delete=models.SET_NULL)
    profile_pic = models.ImageField(upload_to='image/',null=True)
    def __str__ (self):
        return self.empname




