
from rest_framework import viewsets #  Импорт набора представлений (Инструменты для обработки HTTP-запросов (GET,POST,PUT,DELETE))
from rest_framework.views import APIView
from django.views.decorators.csrf import csrf_exempt  # импорт декоратора csrf_exempt
from django.utils.decorators import method_decorator  # позволяет применять обычные (функциональные) декораторы к методам классов

from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import HttpResponse, JsonResponse

from rest_framework.renderers import TemplateHTMLRenderer, JSONRenderer #  Импорт встроенных классов-рендеров
'''
JSONRenderer - Преобразует данные (обычно результат serializer.data) в JSON‑ответ. Это стандартный формат для REST API.
Когда используется:
По умолчанию для большинства API‑эндпоинтов.
Когда клиент ожидает данные в формате JSON (например, фронтенд на React/Vue, мобильные приложения).

TemplateHTMLRenderer - Отрисовывает HTML‑шаблон с использованием контекста Django. Позволяет возвращать полноценные веб‑страницы из API‑представлений.
Когда используется:
Если нужно отрисовать HTML‑страницу (например, для админки или публичной страницы).
Когда API должно поддерживать и JSON, и HTML (например, для браузеров и машин).
'''

from django.shortcuts import get_object_or_404, render # 
from ListEmp.models import Employ,Positions, Category # Импорт моделей
from ListEmp.api.serializers import  EmploySerializer,  PositionSerializer # Импорт сериализаторов  
from typing import List, Dict, Any
from typing import cast
from django.views.generic import TemplateView
from django.shortcuts import render, redirect
import json
from django.db import connection
import psycopg2
from ListEmp.functions import raw_queryset_to_list_dict # Получение списка словарей из результата raw-запроса
from ListEmp.sql_query import * #  Импорт sql-запросов



# Глобальная переменная хранящая конфигурацию подключения к базе данных
conn = psycopg2.connect(host= 'localhost', user = 'postgres', password = 'Cen78Ter19', dbname = 'ListEmpDB')


'''
Класс EmpViewSet (а также все остальные классы-представлений описанные в этом файле) - 
это расширенные версии класса ModelViewSet из DRF, которые одновременно поддерживают 
два режима работы:

- API-режим (JSON/XML) — стандартное поведение DRF.

- HTML-режим — отдача полноценных HTML-шаблонов для браузерных форм.

'''


# --------------------------------------------------------------------------------------------------  
# РАБОТАЕМ СО СПИСКОМ ЗАПИСЕЙ ТАБЛИЦЫ "СОТРУДНИКИ"      
#  Обработка методов HTTP (GET, POST) - API-режим (JSON/XML)    — стандартное поведение DRF  
class EmpViewSet(viewsets.ModelViewSet):
    queryset = Employ.objects.raw(sql_employ_list) # Возможно не нужно - потестить
    serializer_class = EmploySerializer # Возможно не нужно - потестить
    serializer = EmploySerializer(queryset, many=True)  # , many=True   ListEmploySerializer  # Возможно не нужно - потестить
    
  
    
'''
    
    #  ПРЕЖНИЙ ВАРИАНТ
    #  Переопределяем метод list (Обработка GET)
    def list(self, request, *args, **kwargs):
        queryset = Employ.objects.raw(sql_employ_list)
        serializer = EmploySerializer(queryset, many=True)
        return Response({'employs': list(serializer.data)},template_name = 'ListEmp/show_listEmploy.html') 
       #print({'employs': list(serializer.data)})
    
    
    #  Переопределяем метод create (Обработка POST) ???????????????????????????????
    def create(self, request, *args, **kwargs):
        #  queryset = Employ.objects.raw(sql_employ_list)
        #  serializer = EmploySerializer(queryset, many=True) 
        return Response(template_name = 'add_employ.html')
        #  return Response({'employs': list(serializer.data)},template_name = 'add_employ.html')
      
       # return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
   
    print(template_name)
   
   '''
# -----------------------------------------------------------------------------------------    
#  РАБОТАЕМ С КОНКРЕТНОЙ ЗАПИСЬЮ ТАБЛИЦЫ "СОТРУДНИКИ" (Детализация)
#  Обработка методов HTTP (GET, PUT, DELETE)
class EmpViewSetDetail(viewsets.ModelViewSet):
 queryset = Employ.objects.raw(sql_employ_detail)  # 
 serializer_class = EmploySerializer   # DetailEmploySerializer
 lookup_field = 'id' # Указываем поле, где искать идентификатор записи
 
 
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

# ---------------------------------------------------------------------------------------- 
# РАБОТАЕМ СО СПИСКОМ ЗАПИСЕЙ ТАБЛИЦЫ "ДОЛЖНОСТИ"
#  Обработка методов HTTP (GET, POST)    
class PositionViewSet(viewsets.ModelViewSet):
    serializer_class = PositionSerializer
  #  Переопределяем метод list (Обработка GET)
    def list(self, request, *args, **kwargs):
        category_id = self.kwargs.get('category')
        queryset = Positions.objects.raw(sql_position_list, [category_id])
        serializer = PositionSerializer(queryset, many=True)
        return Response({'positions': list(serializer.data)})  # ,template_name = 'ListEmp/show_listEmploy.html'
      
    '''
    # ВОЗМОЖНО ЭТОТ ПЕРЕОПРЕДЕЛЁННЫЙ МЕТОД НЕ ПОНАДОБИТЬСЯ
    #  Переопределяем метод create (Обработка POST) ???????????????????????????????
    def create(self, request, *args, **kwargs):
        #  queryset = Employ.objects.raw(sql_position_list)
        #  serializer = EmploySerializer(queryset, many=True) 
        return Response(template_name = 'add_employ.html')
        #  return Response({'employs': list(serializer.data)},template_name = 'add_employ.html')
      
       # return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
  '''
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  

#  ----------------------------------------------------------------------------------  
#  РАБОТАЕМ С КОНКРЕТНОЙ ЗАПИСЬЮ ТАБЛИЦЫ "ДОЛЖНОСТИ" (Детализация)
#  Обработка методов HTTP (GET, PUT, DELETE)
class PositionViewSetDetail(viewsets.ModelViewSet):
 queryset = Positions.objects.raw(sql_position_detail)
 serializer_class = PositionSerializer 
 lookup_field = 'id' # Указываем поле, где искать идентификатор записи
 '''
 По аналогии с моделью "Сотрудники" используем те же самые действия 
 для получения конкретной записи
 '''
 # Извлекаем значение параметра URL-маршрута 
 def get_object_by_id(self,model_class):
   obj_id = self.kwargs['id']
   return get_object_or_404(model_class,id=obj_id)
 
 # Переопределяем метод get_object()
 def get_object(self):
   return self.get_object_by_id(Positions) # Передаём в метод get_object_by_id() в качестве параметра класс текущей модели
 
 
 
 
 
    
'''
    
    """УНИВЕРСАЛЬНЫЙ ВАРИАНТ API-HTML. Обработка GET-запросов (запрос ко всему списку)""" 
    def list(self, request, *args, **kwargs):
        queryset = Employ.objects.raw(sql_employ_list) # набор объектов модели для операций
        serializer = EmploySerializer(queryset, many=True) # сериализатор для конвертации данных в JSON и валидации
        if self.request.accepted_renderer.format == 'html': # Проверка. Какой формат запросил клиент(Accept-заголовок). Если html 
              return render(request, 'ListEmp/show_listEmploy.html', {'data': self.queryset}) #  Возвращает шаблон show_listEmploy.html с данными
        else:                                                                 
         return Response({'employs': list(serializer.data)}) # Иначе. Возвращает из DRF JSON‑список объектов
      
      
    '''
     
          