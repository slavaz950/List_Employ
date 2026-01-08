
from rest_framework import viewsets #  Импорт набора представлений (Инструменты для обработки HTTP-запросов (GET,POST,PUT,DELETE))



from rest_framework.response import Response

from django.http import HttpResponse

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

from django.shortcuts import get_object_or_404 # 
from .models import Employ,Positions # Импорт моделей
from .serializers import  EmploySerializer,  PositionSerializer # Импорт сериализаторов  
from typing import List, Dict, Any
from typing import cast


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

  
# РАБОТАЕМ СО СПИСКОМ ЗАПИСЕЙ ТАБЛИЦЫ "СОТРУДНИКИ"      
#  Обработка методов HTTP (GET, POST)    
class EmpViewSet(viewsets.ModelViewSet):
    renderer_classes = [JSONRenderer, TemplateHTMLRenderer]  #  Закоментить если нужно вывести данные в DRF
    template_name = 'show_listEmploy.html'   #  Закоментить если нужно вывести данные в DRF
    
    queryset = Employ.objects.raw(sql_employ_list)
   
    serializer_class = EmploySerializer
    serializer = EmploySerializer(queryset, many=True)  # , many=True   ListEmploySerializer
    
    #  Переопределяем метод list (Обработка GET)
    def list(self, request, *args, **kwargs):
        queryset = Employ.objects.raw(sql_employ_list)
        serializer = EmploySerializer(queryset, many=True) 
      #   print({'employs': list(serializer.data)})
        return Response({'employs': list(serializer.data)},template_name = 'ListEmp/show_listEmploy.html')
       #print({'employs': list(serializer.data)})
    
    '''
    # ВОЗМОЖНО ПЕРЕОПРЕДЕЛЕНИЕ НЕ НУЖНО (данные уходят на сервер)
    def create(self, request, *args, **kwargs):
        queryset = Employ.objects.raw(sql_employ_list)
        serializer = EmploySerializer(queryset, many=True) 
        return Response({'employs': list(serializer.data)},template_name = 'add_employ.html')
       # return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
   '''
   
   
   
   
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


# РАБОТАЕМ СО СПИСКОМ ЗАПИСЕЙ ТАБЛИЦЫ "ДОЛЖНОСТИ"
#  Обработка методов HTTP (GET, POST)    
class PositionViewSet(viewsets.ModelViewSet):
    queryset = Positions.objects.raw(sql_position_mod)
    serializer_class = PositionSerializer
    serializer = PositionSerializer(queryset, many=True)  

  
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


