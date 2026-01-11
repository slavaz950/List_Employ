
from rest_framework import viewsets #  Импорт набора представлений (Инструменты для обработки HTTP-запросов (GET,POST,PUT,DELETE))



from rest_framework.response import Response

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
from .serializers import  EmploySerializer,  PositionSerializer # Импорт сериализаторов  
from typing import List, Dict, Any
from typing import cast
from django.views.generic import TemplateView
from django.shortcuts import render


from .functions import raw_queryset_to_list_dict # Получение списка словарей из результата raw-запроса


# ФОРМИРУЕМ SQL-ЗАПРОСЫ

# SQL-запрос для вывода списка всех сотрудников 
sql_emp ='\
          SELECT\
            e.id,\
            e."FIO",\
            e.id_gender,\
            g.name_gender,\
            e.age,\
            e.id_positions,\
            p.name_position,\
            e.id_category,\
            c.name_category\
              FROM employ e\
                  INNER JOIN positions  p ON p.id = e.id_positions \
                  INNER JOIN category  c ON c.id = e.id_category \
                  INNER JOIN gender  g ON g.id = e.id_gender'
                
order_by = ' ORDER BY e.id'  # Условия сортировки

# Запрос для вывода списка сотрудников 
sql_employ_list = sql_emp + order_by  

# SQL-запрос для получения данных о конкретном сотруднике 
sql_employ_detail = 'SELECT * FROM employ WHERE id = %s'


# Получаем данные только из модели
sql_position_mod = 'SELECT * FROM positions ORDER BY id ASC'
sql_position_mod_params = 'SELECT * FROM positions WHERE id_category = %s'


'''
Класс EmpViewSet (а также все остальные классы-представлений описанные в этом файле) - 
это расширенные версии класса ModelViewSet из DRF, которые одновременно поддерживают 
два режима работы:

- API-режим (JSON/XML) — стандартное поведение DRF.

- HTML-режим — отдача полноценных HTML-шаблонов для браузерных форм.

'''


# --------------------------------------------------------------------------------------------------  
# РАБОТАЕМ СО СПИСКОМ ЗАПИСЕЙ ТАБЛИЦЫ "СОТРУДНИКИ"      
#  Обработка методов HTTP (GET, POST)    
class EmpViewSet(viewsets.ModelViewSet):
    renderer_classes = [JSONRenderer, TemplateHTMLRenderer]  #  Закоментить если нужно вывести данные в DRF
   #   template_name = 'show_listEmploy.html'   #  Закоментить если нужно вывести данные в DRF
    
    queryset = Employ.objects.raw(sql_employ_list) # Возможно не нужно - потестить
   
    serializer_class = EmploySerializer # Возможно не нужно - потестить
    serializer = EmploySerializer(queryset, many=True)  # , many=True   ListEmploySerializer  # Возможно не нужно - потестить
    
    
    
    
    """УНИВЕРСАЛЬНЫЙ ВАРИАНТ API-HTML. Обработка GET-запросов (запрос ко всему списку)""" 
    def list(self, request, *args, **kwargs):
        queryset = Employ.objects.raw(sql_employ_list) # набор объектов модели для операций
        serializer = EmploySerializer(queryset, many=True) # сериализатор для конвертации данных в JSON и валидации
        if self.request.accepted_renderer.format == 'html': # Проверка. Какой формат запросил клиент(Accept-заголовок). Если html 
              return render(request, 'ListEmp/show_listEmploy.html', {'data': self.queryset}) #  Возвращает шаблон show_listEmploy.html с данными
        else:                                                                 
         return Response({'employs': list(serializer.data)}) # Иначе. Возвращает из DRF JSON‑список объектов
      
      
    '''
      
      return Response({'employs': list(serializer.data)},template_name = 'ListEmp/show_listEmploy.html')
      В таком варианте тоже работает
      
      Закоментил 
      #    if self.request.accepted_renderer.format == 'html':
          #    return render(request, 'ListEmp/show_listEmploy.html', {'data': self.queryset})
       #   else:
       
       Страница открылась как положено.
      
         '''
            #  return super().list(request, *args, **kwargs)
          
          
    """Обработка POST-запросов"""
    def create(self, request, *args, **kwargs):
        queryset = Employ.objects.raw(sql_employ_list) # набор объектов модели для операций
        serializer = EmploySerializer(queryset, many=True) # сериализатор для конвертации данных в JSON и валидации
        if self.request.accepted_renderer.format == 'html':
            return render(request, 'ListEmp/add_employ.html')
        else:
            # return super().create(request, *args, **kwargs)
            return Response({'employs': list(serializer.data)}) # Иначе. Возвращает из DRF JSON‑список объектов
    
'''		
   EXAMPLE
   def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
   
   '''
   
    
   #    ListEmp/show_listEmploy.html    #  Список сотрудников
    
    
    
   #    ListEmp/card_employ.html   #  Просмотр
    
    #   ListEmp/update_card_employ.html   #  Изменение
    
    
    
    
    
    
    
    
    
    
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
    queryset = Positions.objects.raw(sql_position_mod)
    serializer_class = PositionSerializer
    serializer = PositionSerializer(queryset, many=True)  

#  ----------------------------------------------------------------------------------  
#  РАБОТАЕМ С КОНКРЕТНОЙ ЗАПИСЬЮ ТАБЛИЦЫ "ДОЛЖНОСТИ" (Детализация)
#  Обработка методов HTTP (GET, PUT, DELETE)
class PositionViewSetDetail(viewsets.ModelViewSet):
 queryset = Positions.objects.raw(sql_position_mod_params)
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
 
 
 
 
 
 
 
 
def get_category(request):
    categories = Category.objects.all()
    return render(request, 'ListEmp/add_employ.html', {'categories': categories})

def get_positions(request):
    category_id = request.GET.get('category_id')
    
    if not category_id:  # Если значение category_id отсутствует возвращается пустой список
        return JsonResponse([], safe=False) # safe=False разрешает возвращать любые структуры 
                                            #  (список, число, строку и т. п.). Без этого флага 
                                            #  код вызвал бы исключение при попытке вернуть список.
                                            
                                             # По умолчанию (safe=True) JsonResponse разрешает только
                                             # словари (т. к. JSON‑объект — это пара «ключ‑значение»).
                                             
    
    # Формируем Raw-запрос для получения Должностей по категории
    query = 'SELECT id, name_position FROM positions where id_category = %s'
    
   # Выполняем Raw-запрос с параметром
    positions = Positions.objects.raw(query, [category_id])
    
    # Преобразуем в список словарей для JsonResponse
    # Так как JsonResponse не может сериализовать объекты RawQuerySet
    result = []
    for position in positions:
        result.append({
            'id': position.id,
            'name': position.name
        })
    
    return JsonResponse(result, safe=False)