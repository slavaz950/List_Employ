from django.shortcuts import render
#from .models import Employs, Positions, Category  # Возможно не нужно будет
from django.db import connection
from django.http import JsonResponse
import psycopg2
from django.http import HttpResponse
from django.core import serializers


from collections import namedtuple

#from .forms import  

# Create your views here.


def create_record(obj,fields):
  #данный объект из базы данных возвращает именованный кортеж с полями, сопоставленными со значениями
  Record = namedtuple("Record",fields)
  mappings = dict(zip(fields, obj))
  return Record(**mappings)





# Метод (функция) для возвращения всех строк из курсора в виде словаря
def dict_get(cursor):
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]






# Контроллер (Список сотрудников)
def index(request):
 # Подключение к базе данных 
  conn = psycopg2.connect(host= 'localhost', user = 'postgres', password = 'Cen78Ter19', dbname = 'ListEmpDB')
  
  cur_list = conn.cursor() # Создаём курсор
  
  cur_list.execute('select e."FIO",e.gender,e.age,p.name_position,c.name_category from employ e inner join positions p on e.id_positions = p.id inner join category c on e.id_category = c.id')
  colnames = [desc[0] for desc in cur_list.description]
  rows = cur_list.fetchall()
  conn.close() # Закрытие курсора
  result = []
  for row in rows:
    result.append(create_record(row, colnames))
  
  
  
 # rows = cur_list.fetchall()  # Запоминаем результаты работы курсора
  #column_names = [d[0] for d in cur_list.description]
 # for row in rows:
    #row_dict = {column_names[index]: value for (indewx, value) in enumerate(row)}
    
  
  #CurList = dict_get(cur_list.fetchall())
  #CurDict = dict(CurList)
  
  
 #  with connection.cursor() as cur_list:
  #  cur_list.execute('select e."FIO",e.gender,e.age,p.name_position,c.name_category from employ e inner join positions p on e.id_positions = p.id inner join category c on e.id_category = c.id')
  
   
   #CurList = dict_get(CurBuf)
   
  
   
   
  conn.close() # Закрытие курсора
  # ListEmp = dict_get(CurBuf)
   #return JsonResponse({dict_get(cursor)})
 # return 

  context =  JsonResponse(result, safe = False)
  #return HttpResponse(result)
  return render(request, 'show_listEmploy.html')  #


   
   #select e."FIO" ,e.gende from public."ListEmp_employees" e
''' 
    Employees_data = []  
    for employees  in listEmp:

     Employees_data.append({
       'id':listEmp.id, 
      'FIO':listEmp.FIO,
      'gender':listEmp.gender,
      })   '''
    #return JsonResponse({'listEmploy':Employees_data}) 
     
    
   #return render(request, 'show_listEmploy.html')  # 