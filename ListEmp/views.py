
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
from .models import Employ,Positions, Category # Импорт моделей
# from .serializers import  EmploySerializer,  PositionSerializer # Импорт сериализаторов  
from ListEmp.api.serializers import  EmploySerializer,  PositionSerializer # Импорт сериализаторов
from typing import List, Dict, Any
from typing import cast
from django.views.generic import TemplateView
from django.shortcuts import render, redirect
import json
from django.db import connection
import psycopg2
from .functions import raw_queryset_to_list_dict # Получение списка словарей из результата raw-запроса
from .sql_query import * #  Импорт sql-запросов



# Глобальная переменная хранящая конфигурацию подключения к базе данных
conn = psycopg2.connect(host= 'localhost', user = 'postgres', password = 'Cen78Ter19', dbname = 'ListEmpDB')


'''
Класс EmpViewSet (а также все остальные классы-представлений описанные в этом файле) - 
это расширенные версии класса ModelViewSet из DRF, которые одновременно поддерживают 
два режима работы:

- API-режим (JSON/XML) — стандартное поведение DRF.

- HTML-режим — отдача полноценных HTML-шаблонов для браузерных форм.

'''


    
#  Обработка методов HTTP (GET, POST) - HTML-режим — отдача полноценных HTML-шаблонов для браузерных форм

'''
     method_decorator — вспомогательный декоратор из django.utils.decorators. Он позволяет:
     применить обычный декоратор (рассчитанный на функции) к методу класса;

     csrf_exempt — декоратор который отключает защиту от CSRF (Cross‑Site Request Forgery) для представления.

     dispatch — это ключевой метод любого CBV в Django. Он:
         - получает HTTP‑запрос;
         - определяет, какой HTTP‑метод вызван (GET, POST, PUT и т. д.);
         - перенаправляет запрос на соответствующий метод (get(), post() и т. д.).

     Указывая name='dispatch', мы говорим: «Примени csrf_exempt к методу dispatch этого класса».
     Это означает, что все HTTP‑методы (get, post, put, delete и др.) данного представления будут без проверки CSRF.
  
     '''
@method_decorator(csrf_exempt, name= 'dispatch') #  Этот декоратор сам выбирает метод класса (get или post) в зависимости от того какой HTTP-метод используется
class EmployView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    def get(self, request, *args, **kwargs):  # self, request, *args, **kwargs
        queryset = Employ.objects.raw(sql_employ_list)
        serializer = EmploySerializer(queryset, many=True)
        return Response({'employs': list(serializer.data)},template_name = 'ListEmp/show_listEmploy.html') 
    
    #  Обрабатываем добавление нового сотрудника (Метод POST)
    def post(self, request, *args, **kwargs):
            #  Получаем данные из Html-формы  
            fio = request.POST.get('fio')
            gender = request.POST.get('gender')
            age = request.POST.get('age')
            category = request.POST.get('CategorySelect')
            position = request.POST.get('PositionSelect')
          
           #   try:
            with connection.cursor() as cursor:
                cursor.execute(sql_employ_insert,[fio,age,position,category,gender])
                return redirect('employ-list')  # перенаправляем на список
               #    return JsonResponse({'status': 'success', 'message': 'Сотрудник добавлен.'}, template_name = 'ListEmp/show_listEmploy.html')
                #   return JsonResponse({'status': 'success', 'message': 'Сотрудник добавлен.'}, status=201) 
            #  except Exception as errDB:
            #   return JsonResponse({'error': 'Ошибка базы данных: {str(errDB)}'}, status=500)
           
    
  



def get_category(request):
    with connection.cursor() as cursor:
        cursor.execute(sql_category_list)
        rows = cursor.fetchall()
    # Преобразуем результат в список словарей (Так как JsonResponse не может сериализовать объекты RawQuerySet)
    categories = [{'id': row[0], 'name': row[1]} for row in rows]
    return JsonResponse(categories, safe=False)
    
    
"""
def get_positions(request,category ):
    category_id = request.GET.get('category')
    with connection.cursor() as cursor:
        cursor.execute(sql_position_list, [category_id])
        rows = cursor.fetchall()
    # Преобразуем результат в список словарей (Так как JsonResponse не может сериализовать объекты RawQuerySet)
    positions = [{'id': row[0], 'name': row[1]} for row in rows]
    return JsonResponse(positions, safe=False)   
    
  """ 
    
    
 


def get_positions(request,category ):
    if not category:  # Если значение category_id отсутствует возвращается пустой список
        return JsonResponse([], safe=False) # safe=False разрешает возвращать любые структуры 
                                            #  (список, число, строку и т. п.). Без этого флага 
                                            #  код вызвал бы исключение при попытке вернуть список.
                                            
                                             # По умолчанию (safe=True) JsonResponse разрешает только
                                             # словари (т. к. JSON‑объект — это пара «ключ‑значение»).
    
   # Выполняем Raw-запрос с параметром
    positions = Positions.objects.raw(sql_position_list, [category])  # category_id

    # Преобразуем в список словарей для JsonResponse
    # Так как JsonResponse не может сериализовать объекты RawQuerySet
    result = []
    for position in positions:
        result.append({
            'id': position.id,
            'name_position': position.name_position,
           #  'category': position.category
        })
    return JsonResponse(result, safe=False)



 






def EmpNewAdd(request):
    # Просто возвращаем рендеринг шаблона add_employ.html
    return render(request, 'ListEmp/add_employ.html')


    
    
    
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
     
          