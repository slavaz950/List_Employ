
from rest_framework import viewsets #  Импорт набора представлений (Инструменты для обработки HTTP-запросов (GET,POST,PUT,DELETE))
from rest_framework.response import Response
from django.http import  JsonResponse
from django.shortcuts import get_object_or_404 # , render
from ListEmp.models import Employ,Positions, Category # Импорт моделей
from ListEmp.api.serializers import  EmploySerializer,  PositionSerializer, CategorySerializer # Импорт сериализаторов  
from django.db import connection
from ListEmp.sql_query import * #  Импорт sql-запросов
from rest_framework import status
from django.db import IntegrityError

'''
Класс EmpViewSet (а также все остальные классы-представлений описанные в этом файле) - 
это расширенные версии класса ModelViewSet из DRF, которые поддерживает API-режим (JSON/XML) — стандартное поведение DRF.
'''

# --------------------------------------------------------------------------------------------------  
# РАБОТАЕМ СО СПИСКОМ ЗАПИСЕЙ ТАБЛИЦЫ "СОТРУДНИКИ"      
#  Обработка методов HTTP (GET, POST) - API-режим (JSON/XML)    — стандартное поведение DRF  
class EmpViewSet(viewsets.ModelViewSet):
    queryset = Employ.objects.raw(sql_employ_list) # Возможно не нужно - потестить
    serializer_class = EmploySerializer # Объявляем используемый сериализатор
    serializer = EmploySerializer(queryset, many=True)  # Создаём экземпляр сериализатора и передаём ему набор данных (queryset)
    
    # Переопределение метода create для корректной обработки исключения IntegrityError (при нарушении ограничений БД)
    # Плюсы: полный контроль над обработкой.
    # Минусы: дублирование кода в разных представлениях.
    # клиенты получают информативные сообщения (вместо 500);
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            try:
                self.perform_create(serializer)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            except IntegrityError as e: # Перехватываем исключение  IntegrityError
                # Парсим ошибку для определения типа нарушения
                error_msg = str(e).lower() # Получаем информацию об ошибке
                print(error_msg) 
                # Ищем в тексте информации об ошибки ключенвые слова, для определения её сути.
                if 'повторяющееся значение' in error_msg or 'уже существует' in error_msg:
                    return Response(status=status.HTTP_409_CONFLICT)   # Возвращаем корректный статусный код
                else:
                    return Response(status=status.HTTP_400_BAD_REQUEST)  # Возвращаем корректный статусный код
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
# -----------------------------------------------------------------------------------------    
#  РАБОТАЕМ С КОНКРЕТНОЙ ЗАПИСЬЮ ТАБЛИЦЫ "СОТРУДНИКИ" (Детализация)
#  Обработка методов HTTP (GET, PUT, DELETE)
class EmpViewSetDetail(viewsets.ModelViewSet):
 queryset = Employ.objects.raw(sql_employ_detail) #  Получаем целевой объект модели Employ
 serializer_class = EmploySerializer   # Объявляем используемый сериалайзер
 lookup_field = 'id' # Указываем поле, где искать идентификатор записи
 
 '''
 Имел место конфликт имён между параметром URL-маршрута id и встроенной функцией
 Python id(). Один из способов решения данной проблемы создание вспомогательного метода, 
 который извлекает значение параметра URL-маршрута 
 '''
 # Извлекаем значение параметра URL-маршрута 
 def get_object_by_id(self,model_class):
   obj_id = self.kwargs['id'] # Получаем значение идентификатора целевой записи
   return get_object_or_404(model_class,id=obj_id) # Возвращаем объект из БД по полученому выше идентификатору
 
 # Переопределяем встроенный метод классов-представлений get_object(), (получения объекта БД по URL-параметру)
 def get_object(self):
   return self.get_object_by_id(Employ) # Передаём в метод get_object_by_id() в качестве параметра класс текущей модели

# ---------------------------------------------------------------------------------------- 
# РАБОТАЕМ СО СПИСКОМ ЗАПИСЕЙ ТАБЛИЦЫ "ДОЛЖНОСТИ"
#  Обработка методов HTTP (GET, POST)    
class PositionViewSet(viewsets.ModelViewSet):
  queryset = Positions.objects.raw(sql_position_detail) #  Получаем целевой объект модели Positions
  serializer_class = PositionSerializer  # Объявляем используемый сериализатор
  lookup_field = 'category' # Указываем поле, где искать идентификатор записи
  
  #  Переопределяем метод list (Обработка GET)
  def list(self, request, *args, **kwargs):
        category_id = self.kwargs.get('category')  #  Получаем именнованый параметр из URL-маршрута
        
        with connection.cursor() as cursor:
                cursor.execute(sql_position_list,[category_id])
                rows = cursor.fetchall() 
                 
         # Конвертируем строки в словарь (для сериализации)
        data = []
        for row in rows:
              data.append({
                'id': row[0],
                'name_position': row[1],
                'category': row[2],
                'category_name': row[3],
            })
        return Response(data)  # Возвращаем JSON-объект 
      
      
      # Переопределение метода create для корректной обработки исключения IntegrityError (при нарушении ограничений БД)
    # Плюсы: полный контроль над обработкой.
    # Минусы: дублирование кода в разных представлениях.
    # клиенты получают информативные сообщения (вместо 500);
  def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            try:
                self.perform_create(serializer)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            except IntegrityError as e: # Перехватываем исключение  IntegrityError
                # Парсим ошибку для определения типа нарушения
                error_msg = str(e).lower() # Получаем информацию об ошибке 
                print(error_msg)
                # Ищем в тексте информации об ошибки ключенвые слова, для определения её сути.
                if 'повторяющееся значение' in error_msg or 'уже существует' in error_msg:
                    return Response(status=status.HTTP_409_CONFLICT)   # Возвращаем корректный статусный код
                else:
                    return Response(status=status.HTTP_400_BAD_REQUEST)  # Возвращаем корректный статусный код
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
#  ----------------------------------------------------------------------------------  
#  РАБОТАЕМ С КОНКРЕТНОЙ ЗАПИСЬЮ ТАБЛИЦЫ "ДОЛЖНОСТИ" (Детализация)
#  Обработка методов HTTP (GET, PUT, DELETE)
class PositionViewSetDetail(viewsets.ModelViewSet):
 queryset = Positions.objects.raw(sql_position_detail) #  Получаем целевой объект модели Positions
 serializer_class = PositionSerializer  # Объявляем используемый сериализатор
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
 
 
 #  ---------------------------------------------------------------------------------- 
 # РАБОТАЕМ СО СПИСКОМ ЗАПИСЕЙ ТАБЛИЦЫ "КАТЕГОРИИ"
#  Обработка методов HTTP (GET, POST)    
class CategoryViewSet(viewsets.ModelViewSet):
    #  serializer_class = CategorySerializer  # Объявляем используемый сериализатор
    queryset = Category.objects.raw(sql_category_list) #  Получаем целевой объект модели Category
    serializer_class = CategorySerializer  # Объявляем используемый сериализатор
    serializer = CategorySerializer(queryset, many=True) # Создаём экземпляр сериализатора и передаём ему набор данных (queryset)
     #    return Response({'category': list(serializer.data)})  # Возвращаем JSON-объект с ключом category
   #   def list(self, request, *args, **kwargs):
        #  category_id = self.kwargs.get('category')  #  Получаем именнованый параметр из URL-маршрута
    
 
#  Определяем количество сотрудников принятых на определённую должность 
# Используем класс JsonResponse (то есть DRF не используем)
def countEmpByPositions(request, *args, **kwargs):
        position_id = kwargs.get('positions')  #  Получаем именнованый параметр из URL-маршрута
        
        with connection.cursor() as cursor:
                cursor.execute(sql_count_employ_by_position,[position_id])
                result = cursor.fetchone()  #  Всегда получаем только одно значение, поэтому  fetchone()       
        data = {'count': result,}  # Формируем объект (для сериализации)
        return JsonResponse(data)
 
 