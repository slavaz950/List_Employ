from django.shortcuts import render

from django.db import connection
from django.http import JsonResponse
import psycopg2
from django.http import HttpResponse
from django.views.decorators.csrf import ensure_csrf_cookie

from rest_framework import generics

#from .models import Positions
from collections import namedtuple
from django.views.decorators.csrf import csrf_protect
import json

#from .serializers import ShowListEmploySerializer
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer, JSONRenderer


# Функция подготавливает данные для формирования JSON объекта
def create_record(obj,fields):
  #данный объект из базы данных возвращает именованный кортеж с полями, сопоставленными со значениями
  Record = namedtuple("Record",fields)
  mappings = dict(zip(fields, obj))
  return  mappings    #(**mappings)


class ViewAPI(generics.ListAPIView):
  #renderer_classes = [TemplateHTMLRenderer]
  #template_name = 'show_listEmploy.html'
  
  def get(self, request):
    
   # data = json.loads(request.body) # Считываем строку в формате JSON и возвращаем
    #id = data.get('id') 
    
    #id = request.query_params["id"]
    
    
    conn = psycopg2.connect(host= 'localhost', user = 'postgres', password = 'Cen78Ter19', dbname = 'ListEmpDB')
    queryset = conn.cursor() # Создаём курсор
    lst = queryset.execute('select e.id,e."FIO",e.gender,e.age,p.name_position,c.name_category from employ e inner join positions p on e.id_positions = p.id inner join category c on e.id_category = c.id')
    
    colnames = [desc[0] for desc in queryset.description]
    rows = queryset.fetchall()
 # conn.close() # Закрытие курсора
    result = []
    for row in rows:
      result.append(create_record(row, colnames))
    #conn.close() # Закрытие курсора 
  
  
  # Подготавливаем полученые данные к формированию JSON объекта   
    return Response({'posts':result})
   
    
    
class CardAPI(generics.ListAPIView):
  def get(self, request):
    conn = psycopg2.connect(host= 'localhost', user = 'postgres', password = 'Cen78Ter19', dbname = 'ListEmpDB')
    queryset = conn.cursor() # Создаём курсор
    lst = queryset.execute('select e.id,e."FIO",e.gender,e.age,e.id_positions,e.id_category,p.name_position,c.name_category from employ e inner join positions p on e.id_positions = p.id inner join category c on e.id_category = c.id where e.id = 2')
    
    #lst = queryset.execute('select e."FIO",e.gender,e.age,p.name_position,c.name_category from employ e inner join positions p on e.id_positions = p.id inner join category c on e.id_category = c.id where e.id = 1')
    
    colnames = [desc[0] for desc in queryset.description]
    rows = queryset.fetchall()
 # conn.close() # Закрытие курсора
    result = []
    for row in rows:
      result.append(create_record(row, colnames))
  # Подготавливаем полученые данные к формированию JSON объекта   
    return Response({'posts':result})


  # Формируем список должностей для вывода в выпадающем списке
#$@csrf_protect 
class Get_positionsAPI(generics.ListAPIView):
   def get(self, request):
    conn = psycopg2.connect(host= 'localhost', user = 'postgres', password = 'Cen78Ter19', dbname = 'ListEmpDB')
    queryset = conn.cursor() # Создаём курсор
    lst = queryset.execute('select p.id ,p.id_category , p.name_position,c.name_category from  positions p  inner join category c on p.id_category = c.id')
    colnames = [desc[0] for desc in queryset.description]
    rows = queryset.fetchall()
 # conn.close() # Закрытие курсора
    result = []
    for row in rows:
      result.append(create_record(row, colnames))
  # Подготавливаем полученые данные к формированию JSON объекта   
    return Response({'posts':result})
  
 


# Контроллер (HTML.Список сотрудников)
def index(request):
 return render(request, 'show_listEmploy.html') 



# Контроллер (HTML. Карточка сотрудника)
def update_positions(request):
  return render(request, 'update_positions.html') 


# Контроллер (HTML. Карточка сотрудника)
def card_employ(request):
  return render(request, 'card_employ.html') 

# Контроллер (HTML. Карточка сотрудника)
def list_positions(request):
  return render(request, 'show_listPosition.html') 


# Контроллер (HTML. Изменение Карточки сотрудника)
def update_card_employ(request):
  # position = Positions.objects.all()
   return render(request, 'update_card_employ.html') 

#, {'position':position}




def post_id(request):
      if request.method == 'POST':  # Если используется метод POST
      # data = json.loads(request.body) # Считываем строку в формате JSON и возвращаем
       id = request.POST.get('id')   # Получаем идентификатор для нашего
      # id = request.data.get("id")
       print(id)
       
       
     #      content = request.data
      conn = psycopg2.connect(host= 'localhost', user = 'postgres', password = 'Cen78Ter19', dbname = 'ListEmpDB')
      queryset = conn.cursor() # Создаём курсор
     # queryset.execute('select e."FIO",e.gender,e.age,p.name_position,c.name_category from employ e inner join positions p on e.id_positions = p.id inner join category c on e.id_category = c.id where e.id =  %s', [id])
    
      queryset.execute('select e."FIO",e.gender,e.age,p.name_position,c.name_category from employ e inner join positions p on e.id_positions = p.id inner join category c on e.id_category = c.id where e.id = 3')
    
    
      result = queryset.fetchall()
    
    
      return Response({'posts':result})  


