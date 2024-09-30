from django import forms
from django.core.exceptions import ValidationError

class Firstform(forms.Form):
    value1 = forms.IntegerField()
    value2 = forms.IntegerField()
    doj=forms.DateField(widget=forms.SelectDateWidget)

    def clean_value1(self):
        val1=self.cleaned_data['value1']

        if val1<0:
            raise ValidationError('Negetive values are not allowed')

        return val1
    
    def clean_value2(self):
        val2=self.cleaned_data['value2']

        if val2<0:
            raise ValidationError('Negetive values are not allowed')

        return val2

    