from rest_framework import serializers
from dbapp.models import employee
from rest_framework.exceptions import ValidationError

class EmpSerializer(serializers.ModelSerializer):
    class Meta:
        model = employee
        fields = '__all__'
    
    def validate_salary(self,esal):
        if esal<0:
            raise serializers.ValidationError("Negative salary")
        
        return esal