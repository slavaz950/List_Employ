import requests

from django.shortcuts import render, redirect

from django.db import connection
from django.http import JsonResponse,HttpResponse, HttpResponseRedirect
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

#from rest_framework.views import APIViews  # Базовый класс. Стоит во главе иерархии 
# всех классов представления Django REST Framework . Это базовый функционал 

from rest_framework.decorators import api_view


# Глобальная переменная хранящая конфигурацию подключения к базе данных
conn = psycopg2.connect(host= 'localhost', user = 'postgres', password = 'Cen78Ter19', dbname = 'ListEmpDB')




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
    #conn = psycopg2.connect(host= 'localhost', user = 'postgres', password = 'Cen78Ter19', dbname = 'ListEmpDB')
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
  # Обработка GET-запроса (Просмотр списка должностей)
   def get(self, request):
    id = request.GET.get("category",2)  # Параметр по умолчанию    ,2
    
    conn = psycopg2.connect(host= 'localhost', user = 'postgres', password = 'Cen78Ter19', dbname = 'ListEmpDB')
    queryset = conn.cursor() # Создаём курсор
    queryset.execute('select p.id ,p.id_category , p.name_position,c.name_category from  positions p  inner join category c on p.id_category = c.id and c.id =%s',[id])
    
    #queryset.execute('select p.id ,p.id_category , p.name_position,c.name_category from  positions p  inner join category c on p.id_category = c.id and c.id =2')
    colnames = [desc[0] for desc in queryset.description]
    rows = queryset.fetchall()
 
    result = []
    for row in rows:
      result.append(create_record(row, colnames))
  # Подготавливаем полученые данные к формированию JSON объекта 
    
    return Response({'posts':result})
    #context = {'posts':result}
    #context = Response({'posts':result})
    #return render(request, 'show_listPosition.html',context)   # ,context
  
  
  


# Контроллер (HTML.Список сотрудников)
def index(request):
  return render(request, 'show_listEmploy.html') 



# Контроллер (HTML. Карточка сотрудника)
def update_positions(request):
  return render(request, 'update_positions.html') 


# Контроллер (HTML. Карточка сотрудника)
def card_employ(request):
  return render(request, 'card_employ.html') 




######################################################
# Контроллер (HTML. Карточка сотрудника)
def list_positions(request):
  
  """
  # В завершение удалить всё закоментированное (если не будет востребовано)
  id = request.GET.get('category')
  print(id)
  
 
  #url_api = "http://127.0.0.1:8000/api_Position/?category="
  
  link = 'http://127.0.0.1:8000/api_Position/?category='
 
  url_api = link + id

  
  print(url_api)
  response_get = requests.get(url_api) # Response
  #response_post = requests.post(url_api) # Response
  
 # load_json = load.json(response_get)
  
  status_get = response_get.status_code
  #status_post = response_post.status_code
  
  
  data_get = response_get.json()
  #data_post = response_post.json()
  
  
  # РАЗБИРАЕМ JSON
  # Извекаем необходимое значение из массива
  
  
  
  for k in data_get.items():
    print(k)
    for f in k:
      for dict in f:
        print(dict)
       
          
  values = dict.items()  # Извлекаем все значения словаря
  
  
  # Извлекаем значения из словаря dict
  value_Id = dict["id"] # значение идентификатора должности
  values_id_category = dict["id_category"]  # значение идентификатора категории
  values_name_category = dict["name_category"] # наименование категории
  values_name_position = dict["name_position"] # наименование должности
  
  print('ниже values')
  print(values)
  
  
  #print(data_get)
  
 
  #print(response_get)  # Выводим статусный код в формате  <Response [200]>
  
  
  #print(status_get)   # Выводим статусный код (только сам код)
  
  
  
  #print(value_Id)  # Выводим идентификатор должности
  #print(values_id_category)  # 
  #print(values_name_category) #
  #print(values_name_position) #
  
  data = {'id':value_Id,
        'id_category':values_id_category,
        'name_category':values_name_category,
        'name_position':values_name_position}
  
  
   #context = {'posts':result}
 #print(context)
  print(data)
  
  """
 
  return render(request, 'show_listPosition.html')   # ,context        ,context=data

#########################################################





# Контроллер (HTML. Изменение Карточки сотрудника)
def update_card_employ(request):
  # position = Positions.objects.all()
   return render(request, 'update_card_employ.html') 

# Контроллер (HTML. Добавление Карточки сотрудника)
def add_positions(request):
   return render(request, 'add_positions.html') 

#, {'position':position}



# РАБОТАЕМ ЗДЕСЬ
class Post_AddPositionsAPI(generics.ListAPIView):
  # Обработка GET-запроса (Просмотр списка должностей)
 def post(self, request):


   # Обработка POST-запроса (Добавление новой должности)
#def api_AddPosition(request):
    name_positions = request.POST.get("position")
    id_category = request.POST.get("category")
    
    print(name_positions)
    print(id_category)

    conn = psycopg2.connect(host= 'localhost', user = 'postgres', password = 'Cen78Ter19', dbname = 'ListEmpDB')
    queryset = conn.cursor() # Создаём курсор
    queryset.execute('insert into positions (name_position, id_category)values (%s, %s)',[name_positions, id_category])
 
 # Выводим обновлённый
 
 
 
    #return render(request, 'show_listPosition.html') 
    return Response({'posts':result})