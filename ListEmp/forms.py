
from django import forms 
from .models import Employees,Category,Positions


class EmployForm(forms.ModelForm):
    
    class Meta:
        model = Employees
        fields = ("FIO","gender")
        
      
      
      
        
class CategoryForm(forms.ModelForm):
    
    class Meta:
        model = Category
        fields = ("id","name_category")
