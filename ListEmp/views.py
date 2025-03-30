from django.shortcuts import render
#import List_Employ
from .models import Employees, Positions, Category
from django.http import JsonResponse
#from .forms import  

# Create your views here.

# Контроллер (Список сотрудников)
def index(request):
  return render(request, 'show_listEmploy.html')
  
  
   '''# global listEmp
    listEmp = Employees.objects.raw('SELECT * FROM public."ListEmp_employees"') 
   # print(listEmp.FIO)
    
    Employees_data = []
    
    #for listEmp in List_Employ:
      
    for Employees  in listEmp:
      
    #for listEmp  in  Employees.objects.raw('SELECT * FROM public."ListEmp_employees" oRDER BY id ASC'):
      
      
      
     Employees_data.append({
      'FIO': messages.FIO,
      'gender':messages.gender,   
        
     })
     return JsonResponse({'listEmploy':Employees_data})  '''
    
   return render(request, 'show_listEmploy.html')  # 