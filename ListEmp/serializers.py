from rest_framework import serializers 
from rest_framework.serializers import ModelSerializer
from rest_framework.parsers import JSONParser   
from rest_framework.renderers import JSONRenderer  
from typing import List, Dict, Any
from .models import Employ,Positions,Category,Gender # Импорт моделей  # Импорт модели Employ






'''
# ------------------------------------------------------------------------------------------------------------------------

# КЛАСС ОПРЕДЕЛЁН ДЛЯ ОБЩЕГО ПОНИМАНИЯ РАБОТЫ СЕРИАЛИЗАТОРА
# Класс Serializers

class PositionModel:
   # Инициализатор (Создаём объекты этого класса (модели) id, name_position)
   def  __init__(self, id, name_position, id_category):
       # Создаём локальные атрибуты у экземпляров этого класса
       self.id = id
       self.name_position = name_position
       self.id_category = id_category
       
# в этом классе вручную прописываем весь функционал для преобразования объектов
# класса PositionModel в   JSON-формат       
class PositionSerializer(serializers.Serializer):      
  # для того чтобы работать с моделями внутри этого класса
  # необходимо определить атрибуты класса, и всё за что отвечают эти атрибуты 
  id = serializers.IntegerField()  
  name_position = serializers.CharField() # Класс CharField() отвечает за представление данных в виде обычной строки
  id_category = serializers.IntegerField()  
    
# Преобразование объектов PositionModel в JSON-формат
def encode():
    # Создаём объект класса PositionModel и передаём в качестве аргументов параметры id, name_position
    model = PositionModel(3, 'Тестовые данные', 5)     # Передаём данные для сериализации  'id', 'name_position', 'id_category'   
    # Пропускаем этот наш объект через сериализатор
    model_sr = PositionSerializer(model)  # Объект сериализации (это ещё не JSON-строка)
    print(model_sr.data, type(model_sr.data), sep='\n')  # model_sr.data - сериализовнные данные;   type(model_sr.data) -тип атрибута ; перевод строки
    #  Преобразуем объект сериализации в JSON-строку
    json = JSONRenderer().render(model_sr.data) # JSON-строка, которую можно передать клиенту
    print(json)
    
# Тестировал через shell (python manage.py shell)

# Обратное преобразование из JSON-строки в объект класса PositionModel
# ДЕКОДИРОВАНИЕ
def decode():
   # Имитируем поступление запроса от клиента (как будто получаем и читаем такую JSON-строку, которая пришла от клиента)
   stream = io.BytesIO(b'{'id': 3, 'name_position': 'Тестовые данные', 'id_category': 5}') 
   # Далее для формирования словаря используем JSON-парсер
   data = JSONParser().parse(stream) # В этот метод передаём поступивший поток который содержит JSON-строку
   # С помощью сериализатора преобразовываем набор данных data, для того чтобы получить объект сериализации
   # Для того чтобы сериализатор именно декодировал данные необходимо использовать именованный параметр data=НАБОР ДАННЫХ
   # Когда мы кодировали, то мы просто передавали объект модели, а когда декодируем необходимо использовать data
   serializer = PositionSerializer(data=data) # именованный параметр data=НАБОР ДАННЫХ
   serializer.is_valid()  # Проверяем корректность принятых данных
   # В результате всех этих операций получаем коллекцию serializer.validated_data
   print(serializer.validated_data)
   # validated_data - является результатом декодирования JSON-строки
   

# ------------------------------------------------------------------------------------------------------------------
'''

class PositionSerialezer(serializers.Serializer):
   #  Здесь необходимо прописать все атрибуты модели, которые мы будем использовать
   id = serializers.IntegerField()
   name_position = serializers.CharField()
   # id_category = serializers.IntegerField()
   id_category = serializers.CharField()




































"""
Определяем класс-сериализатор для модели Employ.
Используем при этом функционал фреймворка Django REST Framework.
Для упрощения программного кода создаём наш класс на основе 
класса сериализатора ModelSerializer, предназначеного 
для работы непосредственно с моделями Django 
"""



class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
      #    fields = ("name_category")
        #  fields = ("id","name_category")
        fields = ('__all__')



class PositionNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Positions
       #   fields = ("name_position")
        fields = ("id","name_position","id_category") 
        #  fields = ('__all__')
       
class GenderSerializwer(serializers.ModelSerializer):
    class Meta:
        model = Gender
       #   fields = ("name_gender")
        #  fields = ("id","name_gender")
        fields = ('__all__') 
       
               

#  Positions.name_position

class DetailEmploySerializer(serializers.ModelSerializer):
    class Meta: # Вложенный класс Meta имеет два атрибута
        model = Employ  # Указываем таблицу с которой будем работать
        #  fields = "__all__" # Указываем поля (в данном случае это все поля)

       #   fields = ("id","fio","age","positions","category","gender") 
       #    fields = ("id","fio","age","id_positions","id_category","id_gender","positions","category","gender")
        
          
        fields = ('__all__') 
        #   depth = 1


#   -----------------------------------------------------------------------------






#  РАБОТОСПОСОБНЫЙ СЕРИАЛИЗАТОР ДЛЯ GET,POST для списка
class EmploySerializer(serializers.ModelSerializer):
   # Объявляем поля, которые будут вычисляться методами get_.......
   positions_name = serializers.SerializerMethodField()
   category_name = serializers.SerializerMethodField()
   gender_name = serializers.SerializerMethodField()
   class Meta: # Вложенный класс Meta имеет два атрибута
        model = Employ  # Указываем модель с которой будем работать
        fields = ("id","fio","age","positions","category","gender","positions_name","category_name","gender_name") 
       
    # ОПРЕДЕЛЯЕМ МЕТОДЫ ДЛЯ РАБОТЫ С ВЛОЖЕННЫМИ ПОЛЯМИ
    
    # Поле с информацией о должности (идентификатор и наименование) 
   def get_positions_name(self, obj: Employ):     # -> dict:   'name_position': positions.name_position,  {  
      positions: Positions = obj.positions
      return (positions.name_position)
     
     
    #  Поле с информацией о категории (идентификатор и наименование)  
   def get_category_name(self, obj: Employ):       # -> dict:
      category: Category = obj.category
      return (category.name_category)
            


    # Пол сотрудника (идентификатор и наименование)
   def get_gender_name(self, obj: Employ):         # -> dict:
      gender: Gender = obj.gender
      return (gender.name_gender)



