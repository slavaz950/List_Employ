from rest_framework import serializers 
# from rest_framework.serializers import ModelSerializer
# from rest_framework.parsers import JSONParser   
# from rest_framework.renderers import JSONRenderer  
from typing import List, Dict, Any
from ListEmp.models import Employ,Positions,Category,Gender # Импорт моделей  



"""
Определяем классы-сериализаторы для моделей Positions, Employ.
Используем при этом функционал фреймворка Django REST Framework.
Для упрощения программного кода создаём наш класс на основе 
класса сериализатора ModelSerializer, предназначеного 
для работы непосредственно с моделями Django. При 
использовании этого класса нет необходимости явно 
указывать все поля модели в сериализаторе. Достаточно указать 
модель и перечислить поля, которые будут необходимы для работы. 
Для вывода полей с наименованиями из связанных таблиц 
используем вложенные сериализаторы 
"""

# Сериализатор для работы с моделью Positions
class PositionSerializer(serializers.ModelSerializer):
  # ФОРМИРУЕМ ПОЛЕ ДЛЯ ВЛОЖЕННОГО СЕРИАЛИЗАТОРА
   # Объявляем поле, которое будет вычисляться методом get_category_name
  category_name = serializers.SerializerMethodField() # Поле name_category из таблицы  Category
  class Meta:
        model = Positions # Указываем модель
        fields = ("id","name_position","category","category_name") # Перечисляем поля (включая поля из связанных таблиц) 
        
 #  Метод для вывода информации о категории 
  def get_category_name(self, obj: Employ):    
     #   category: Category = obj.category       # Для свежих версий Python >= 3.6
     if obj.category:   # Проверяем существует ли такой объект
      category = obj.category #type: str         #  Для старых версий Python < 3.6
      return (category.name_category)  # Если объект существует возвращаем объект
     return None  # Если объект не существует - пустая строка




#  Сериализатор для работы с моделью Employ
class EmploySerializer(serializers.ModelSerializer):
   # ФОРМИРУЕМ ПОЛЯ ДЛЯ ВЛОЖЕННОГО СЕРИАЛИЗАТОРА
   # Объявляем поля, которые будут вычисляться методами get_ИмяПоля
   positions_name = serializers.SerializerMethodField()  # Поле name_position из таблицы  Positions
   category_name = serializers.SerializerMethodField()   # Поле name_category из таблицы  Category
   gender_name = serializers.SerializerMethodField()     # Поле name_gender из таблицы  Gender
   class Meta: # Вложенный класс Meta имеет два атрибута
        model = Employ  # Указываем модель 
        fields = ("id","fio","age","positions","category","gender","positions_name","category_name","gender_name") # Перечисляем поля
     
       
    # ОПРЕДЕЛЯЕМ МЕТОДЫ ДЛЯ РАБОТЫ С ВЛОЖЕННЫМИ ПОЛЯМИ
    # Поле с информацией о должности  
   def get_positions_name(self, obj: Employ):   
     #   positions: Positions = obj.positions      # Для свежих версий Python >= 3.6
     if obj.positions:
      positions = obj.positions   #type: str       #  Для старых версий Python < 3.6
      return (positions.name_position)
     return None
     
    #  Поле с информацией о категории 
   def get_category_name(self, obj: Employ):    
      # category: Category = obj.category       #    Для свежих версий Python >= 3.6
      if obj.category:   # Проверяем существует ли такой объект
       category = obj.category #type: str #  Для старых версий Python < 3.6
       return (category.name_category)  # Если объект существует возвращаем объект
      return None  # Если объект не существует - пустая строка
     #  return (category.name_category)
          
    # Пол сотрудника 
   def get_gender_name(self, obj: Employ):        
     #  gender: Gender = obj.gender               # Для свежих версий Python >= 3.6
     if obj.gender:  # Проверяем существует ли такой объект
      gender = obj.gender  #type: str             #  Для старых версий Python < 3.6
      return (gender.name_gender)   # Если объект существует возвращаем объект
     return None  # Если объект не существует - пустая строка
    
    
    
