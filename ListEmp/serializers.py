from rest_framework import serializers
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser


class ShowListEmployModel:
    def __init__(self, FIO, gender, age, name_position, name_category):
        self.FIO = FIO
        self.gender = gender
        self.age = age
        self.name_position = name_position
        self.name_category = name_category



class ShowListEmploySerializer(serializers.Serializer):
    FIO = serializers.CharField(max_length=35)  # Field name made lowercase.
    gender = serializers.CharField(max_length=3)
    age = serializers.IntegerField#(blank=True, null=True)
    name_position = serializers.CharField(max_length=40)
    name_category = serializers.CharField(max_length=20)
    
    
    # ПРЕОБРАЗОВАНИЕ в JSON
    def encode():
        
        model = ShowListEmployModel('Зайцев','муж','34','Слесарь','Рабочий')
        
        # Создаём объект сериализатора (создаётся коллекция из значений атрибутов объектов  в виде словаря)
        model_sr = ShowListEmploySerializer(model)
        
        
        print(model_sr.data, type(model_sr.data), sep='\n')
        
        # Преобразуем словарь в JSON строку
        json = JSONRenderer().render(model_sr.data)
        print(json)
        
        # ДЕКОДИРОВАНИЕ ИЗ JSON
        def decode():
            stream = io.BytesIO(b'{"title":"Angelina Jolie","content":"Content Angelina Jolie"}')
            data = JSONParser().parse(stream)
            serializer = ShowListEmploySerializer(data=data)
           # Проверяем корректность полученых данных
            print(serializer.validated_data) # Результат