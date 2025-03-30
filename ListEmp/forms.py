
from django import forms 
from .models import Employees,Category,Positions


class EmployForm(forms.ModelForm):
    
    class Meta:
        model = Employees
        fields = ("FIO","gender")
