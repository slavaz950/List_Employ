from django.db import models
#from ListEmp import forms
#from .forms import EmployForm

# Create your models here.

# Модель категории
class Category(models.Model):
    name_category = models.CharField(max_length=20)  # Наименование категории
 
# Модель должности  
class Positions(models.Model):
    name_positions = models.CharField(max_length=40) # Наименование должности
    id_category = models.IntegerField                # Идетификатор категории
    
# Модель сотрудника  
class Employees(models.Model):
    FIO = models.CharField(max_length=35)           # ФИО Сотрудника
    gender = models.CharField(max_length=3)         # Пол сотрудника
    age = models.IntegerField                       # Возраст сотрудника
    id_positions = models.IntegerField              # Идентификатор должности
    id_category = models.IntegerField               # Идентификатор категории