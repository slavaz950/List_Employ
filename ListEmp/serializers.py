from rest_framework import serializers 
from rest_framework.serializers import ModelSerializer
from rest_framework.parsers import JSONParser   
from rest_framework.renderers import JSONRenderer  
from typing import List, Dict, Any
from .models import Employ,Positions,Category,Gender # Импорт моделей  # Импорт модели Employ




'''
class PositionSerializer(serializers.Serializer):
   #  Здесь необходимо прописать все атрибуты модели, которые мы будем использовать
   id = serializers.IntegerField()
   name_position = serializers.CharField()
   # id_category = serializers.IntegerField()
   id_category = serializers.CharField()
'''




class PositionSerializer(serializers.ModelSerializer):
  category_name = serializers.SerializerMethodField()
  class Meta:
        model = Positions
        #  fields = ("id","name_position","id_category")
        fields = ("id","name_position","category","category_name")  
        # fields = ('__all__')


 #  Поле с информацией о категории (идентификатор и наименование)  
  def get_category_name(self, obj: Employ):       # -> dict:
      category: Category = obj.category
      return (category.name_category)
   

"""
Определяем класс-сериализатор для модели Employ.
Используем при этом функционал фреймворка Django REST Framework.
Для упрощения программного кода создаём наш класс на основе 
класса сериализатора ModelSerializer, предназначеного 
для работы непосредственно с моделями Django 
"""


'''
class CategorySerializer(serializers.ModelSerializer):
  
  class Meta:
        model = Category
      #    fields = ("name_category")
        #  fields = ("id","name_category")
        fields = ('__all__')



       
class GenderSerializwer(serializers.ModelSerializer):
    class Meta:
        model = Gender
       #   fields = ("name_gender")
        #  fields = ("id","name_gender")
        fields = ('__all__') 
       
               
'''


'''

#  Positions.name_position

class DetailEmploySerializer(serializers.ModelSerializer):   # ВОЗМОЖНО МОЖНО БУДЕТ УДАЛИТЬ ЗА НЕНАДОБНОСТЬЮ
    class Meta: # Вложенный класс Meta имеет два атрибута
        model = Employ  # Указываем таблицу с которой будем работать
        #  fields = "__all__" # Указываем поля (в данном случае это все поля)

       #   fields = ("id","fio","age","positions","category","gender") 
       #    fields = ("id","fio","age","id_positions","id_category","id_gender","positions","category","gender")
        
          
        fields = ('__all__') 
        #   depth = 1


#   -----------------------------------------------------------------------------

'''




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


# ======================================================================================
# ======================================================================================



'''
class PositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Positions
        #  fields = ("id","name_position","id_category") 
        fields = ('__all__')
'''