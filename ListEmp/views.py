
from django.forms import model_to_dict # Преобразование объекта модели Django в словарь
from rest_framework import generics, viewsets, mixins # type: ignore # Инструменты для обработки HTTP-запросов (GET,POST,PUT,DELETE)
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User, Permission
from typing import List,Tuple,Any,Optional,Dict # Позволяет явно указывать, какие типы данных ожидаются в функциях, переменных и классах

from django.template.context_processors import csrf
from django.views.decorators.csrf import csrf_exempt

from django.shortcuts import render, get_object_or_404 # Обработка шаблонов (templates) и выдача в формате HTTP-ответа клиенту
from rest_framework.response import Response # Создание ответов для веб-API, которые могут быть преобразованы в JSON
from rest_framework.views import APIView # pyright: ignore[reportMissingImports] # Создание представлений на основе классов, которые обрабатывают различные HTTP-методы (GET,POST,PUT,DELETE)
from django.db import connection # Прямой доступ к БД, обходя уровень модели

from rest_framework.viewsets import ModelViewSet, ViewSet
from rest_framework.views import APIView

import psycopg2 # Взаимодействие с СУБД PostgreSQL

from .models import Employ,Positions,Category,Gender # Импорт моделей
from .serializers import  EmploySerializer, DetailEmploySerializer, PositionSerialezer # Импорт сериализаторов  EmployFullSerializer,  ListEmploySerializer,

from django.http import Http404


 
 #from rest_framework import *
 
from django.http import HttpResponse  # 
from django.views.decorators.csrf import ensure_csrf_cookie  #
from django.http import JsonResponse,HttpResponse, HttpResponseRedirect  #

import requests   #

from django.shortcuts import  redirect  #  
from .functions import dictfetchall,create_record, raw_queryset_to_list_dict #ident_from_url
from collections import namedtuple  #
from django.views.decorators.csrf import csrf_protect #
import json  #

from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.renderers import StaticHTMLRenderer, TemplateHTMLRenderer, JSONRenderer #


# всех классов представления Django REST Framework . Это базовый функционал 

from rest_framework.decorators import action, api_view,renderer_classes #


# Глобальная переменная хранящая конфигурацию подключения к базе данных
conn = psycopg2.connect(host= 'localhost', user = 'postgres', password = 'Cen78Ter19', dbname = 'ListEmpDB')

# ФОРМИРУЕМ SQL-ЗАПРОСЫ

# SQL-запрос для вывода списка всех сотрудников (выводим только необходимые поля)

sql_emp ='\
                                   SELECT\
                                      e.id,\
                                      e."FIO",\
                                      e.id_gender,\
                                      e.age,\
                                      e.id_positions,\
                                      e.id_category,\
                                     p.name_position,\
                                      e.id_gender \
                                        FROM employ e\
                                            INNER JOIN positions  p ON p.id = e.id_positions \
                                            INNER JOIN category  c ON c.id = e.id_category \
                                            INNER JOIN gender  g ON g.id = e.id_gender'
 
 
                 
order_by = ' ORDER BY e.id'  # Условия сортировки

# Запрос для вывода списка сотрудников 
sql_employ_list = sql_emp + order_by  
   
# SQL-запрос для вывода детализированной информации о сотруднике (выводим только необходимые поля из всех таблиц)
sql_emp_detail = sql_emp + ' WHERE e.id = %s' 

# SQL-запрос для получения данных о конкретном сотруднике (выборка только из таблицы "Сотрудники", выводим все поля таблицы)
sql_employ_only = 'SELECT * FROM employ WHERE id = %s'


# sql_employ_only = 'SELECT e.id, e.fio, e,age, e.id_positions, e.id_category, e.id_gender FROM employ e WHERE id = %s'




# -----------------------------------------------------------------------------------------------



#  SELECT * FROM positions ORDER BY id ASC 
#  SELECT * FROM positions WHERE id_category = 2
#  sql_employ_only = 'SELECT * FROM employ WHERE id = %s'






# Получаем данные только из модели
sql_position_mod = 'SELECT * FROM positions ORDER BY id ASC'
sql_position_mod_params = 'SELECT * FROM positions WHERE id_category = %s'


class PositionAPIView(APIView):
  def get(self, request):
    #  w = Women.objects.all()
   #    position: List[Positions] = list(Positions.objects.raw(sql_position_mod))
  #    position = list(Positions.objects.raw(sql_position_mod))
    
    
    position = list(Positions.objects.raw(sql_position_mod_params,[]))
    return Response({'posts': PositionSerialezer(position, many = True).data}) # Обрабатываем список записей (many = True)
  # .data - колекция которая представляет собой словарь преобразованных данных из таблицы
  
  
 
   
  
  
# РАБОТАЕМ СО СПИСКОМ ЗАПИСЕЙ ТАБЛИЦЫ "СОТРУДНИКИ"
#  Обработка методов HTTP (GET, POST)    
class EmpTestViewSet(viewsets.ModelViewSet):
    queryset = Employ.objects.raw(sql_employ_list)
    serializer_class = EmploySerializer
    serializer = EmploySerializer(queryset, many=True)  # , many=True   ListEmploySerializer
     
  
   
#  РАБОТАЕМ С ОТДЕЛЬНЫМИ ЗАПИСЯМИ ТАБЛИЦЫ "СОТРУДНИКИ" (Детализация)
#  Обработка методов HTTP (GET, PUT, DELETE)
class EmpViewSetDetail(viewsets.ModelViewSet):

 queryset = Employ.objects.raw(sql_employ_only)
 serializer_class = DetailEmploySerializer 
 '''
 Имел место конфликт имён между параметром URL-маршрута id и встроенной функцией
 Python id(). Один из способов решения данной проблемы создание вспомогательного метода, 
 который извлекает значение параметра URL-маршрута 
 '''
 
 # Извлекаем значение параметра URL-маршрута 
 def get_object_by_id(self,model_class):
   obj_id = self.kwargs['id']
   return get_object_or_404(model_class,id=obj_id)
 
 # Переопределяем метод get_object()
 def get_object(self):
   return self.get_object_by_id(Employ) # Передаём в метод get_object_by_id() в качестве параметра класс текущей модели

lookup_field = 'id' # Указываем поле, где искать идентификатор записи





"""  
     
    ДЛЯ ПРИМЕРА ПО ЗАВЕРШЕНИЮ УДАЛИТЬ
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
  """ 
  
