
# from rest_framework import viewsets #  Импорт набора представлений (Инструменты для обработки HTTP-запросов (GET,POST,PUT,DELETE))
# from rest_framework.views import APIView
# from django.views.decorators.csrf import csrf_exempt  # импорт декоратора csrf_exempt
# from django.utils.decorators import method_decorator  # позволяет применять обычные (функциональные) декораторы к методам классов

# from rest_framework.response import Response
# from rest_framework.decorators import api_view
# from django.http import HttpResponse, JsonResponse

# from rest_framework.renderers import TemplateHTMLRenderer, JSONRenderer #  Импорт встроенных классов-рендеров
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
# from .models import Employ,Positions, Category # Импорт моделей
# from .serializers import  EmploySerializer,  PositionSerializer # Импорт сериализаторов  
# from ListEmp.api.serializers import  EmploySerializer,  PositionSerializer # Импорт сериализаторов
# from typing import List, Dict, Any
# from typing import cast
# from django.views.generic import TemplateView
from django.shortcuts import render, redirect
# import json
# from django.db import connection
# import psycopg2
# from .functions import raw_queryset_to_list_dict # Получение списка словарей из результата raw-запроса
from .sql_query import * #  Импорт sql-запросов   НО ОН НЕ НУЖЕН ЗДЕСЬ


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
     
     
     
'''   
     
@method_decorator(csrf_exempt, name= 'dispatch') #  Этот декоратор сам выбирает метод класса (get или post) в зависимости от того какой HTTP-метод используется
class EmployView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    def get(self, request, *args, **kwargs):  # self, request, *args, **kwargs
        queryset = Employ.objects.raw(sql_employ_list)
        serializer = EmploySerializer(queryset, many=True)
        return Response({'employs': list(serializer.data)},template_name = 'ListEmp/show_listEmploy.html') 
    
 '''    
    
    
    
  
# Переход на страницу со списком сотрудников
def ListEmp(request):
    # Просто возвращаем рендеринг шаблона add_employ.html
    return render(request, 'ListEmp/show_listEmploy.html')




# Переход на страницу добавления нового сотрудника
def EmpNewAdd(request):
    # Просто возвращаем рендеринг шаблона add_employ.html
    return render(request, 'ListEmp/add_employ.html')


# Переход на страницу просмотра карточки сотрудника
def EmpCardView(request,id):
    # Просто возвращаем рендеринг шаблона card_employ.html
    return render(request, 'ListEmp/card_employ.html')
   
    
# Переход на страницу изменения сотрудника 
def employUpdateView(request,id):
    return render(request, 'ListEmp/update_card_employ.html')  # Отображаем HTML-шаблон с указанными данными
 
 
 # ---------------------------------------------------------------------------------------------------
 
 # Переход на страницу со списком должностей
def ListPositions(request):
    # Просто возвращаем рендеринг шаблона add_employ.html
    return render(request, 'ListEmp/show_listPosition.html')

 
 
# Переход на страницу добавления новой должности
def NewAddPositions(request):
    # Просто возвращаем рендеринг шаблона add_employ.html
    return render(request, 'ListEmp/add_positions.html')
 
 
 # Переход на страницу изменения должности 
def UpdateViewPositions(request,id):
    return render(request, 'ListEmp/update_positions.html')  # Отображаем HTML-шаблон с указанными данными
 
 
          