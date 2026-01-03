from rest_framework import serializers 
# from rest_framework.serializers import ModelSerializer
# from rest_framework.parsers import JSONParser   
# from rest_framework.renderers import JSONRenderer  
from typing import List, Dict, Any
from .models import Employ,Positions,Category,Gender # Импорт моделей  



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
  category_name = serializers.SerializerMethodField() # Поле из таблицы  Category
  class Meta:
        model = Positions # Указываем модель
        fields = ("id","name_position","category","category_name") # Перечисляем поля (включая поля из связанных таблиц) 
        
 #  Метод для вывода информации о категории 
  def get_category_name(self, obj: Employ):    
     #   category: Category = obj.category       # Для свежих версий Python >= 3.6
      category = obj.category #type: str         #  Для старых версий Python < 3.6
      return (category.name_category)
   

#  Сериализатор для работы с моделью Employ
class EmploySerializer(serializers.ModelSerializer):
   # Объявляем поля, которые будут вычисляться методами get_ИмяПоля
   positions_name = serializers.SerializerMethodField()
   category_name = serializers.SerializerMethodField()
   gender_name = serializers.SerializerMethodField()
   class Meta: # Вложенный класс Meta имеет два атрибута
        model = Employ  # Указываем модель 
        fields = ("id","fio","age","positions","category","gender","positions_name","category_name","gender_name") # Перечисляем поля
     
       
    # ОПРЕДЕЛЯЕМ МЕТОДЫ ДЛЯ РАБОТЫ С ВЛОЖЕННЫМИ ПОЛЯМИ
    # Поле с информацией о должности  
   def get_positions_name(self, obj: Employ):   
     #   positions: Positions = obj.positions      # Для свежих версий Python >= 3.6
      positions = obj.positions   #type: str       #  Для старых версий Python < 3.6
      return (positions.name_position)
     
    #  Поле с информацией о категории 
   def get_category_name(self, obj: Employ):    
      # category: Category = obj.category         # Для свежих версий Python >= 3.6
      category = obj.category #type: str          #  Для старых версий Python < 3.6
      return (category.name_category)
            
    # Пол сотрудника 
   def get_gender_name(self, obj: Employ):        
     #  gender: Gender = obj.gender               # Для свежих версий Python >= 3.6
      gender = obj.gender  #type: str             #  Для старых версий Python < 3.6
      return (gender.name_gender)
    
    
    
