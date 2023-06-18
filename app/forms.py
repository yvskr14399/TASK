from django import forms
from app.models import *
class Employee_Form(forms.ModelForm):
    class Meta:
        model=Employee
        fields="__all__"
class Employment_Form(forms.ModelForm):
    class Meta:
        model=Employment
        fields="__all__"
        exclude=['variables']
        ch=(('PERMANENT','PERMANENT'),('CONTRACT','CONTRACT'))
        widgets={'emp_typ':forms.RadioSelect(choices=ch)}

class Calculation_Form(forms.Form):
    chh=[('EAST','EAST'),('WEST','WEST'),('SOUTH','SOUTH'),('NORTH','NORTH')]

    select_emp_id=forms.ModelChoiceField(queryset=Employee.objects.all())
    select_country=forms.ModelChoiceField(queryset=Country.objects.all())
    select_region=forms.ChoiceField(choices=chh)