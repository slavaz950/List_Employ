# Здесь будут хранится все функции написаные вручную (всё то чего нет в стандарте)
from collections import namedtuple
from typing import List,Tuple,Any,Optional,Dict
import json
from django.db import connection
# from .serializers import EmployFullSerializer # Импорт сериализаторов
from django.http import JsonResponse,HttpResponse, HttpResponseRedirect  #
from rest_framework.renderers import StaticHTMLRenderer, TemplateHTMLRenderer, JSONRenderer #
from django.shortcuts import get_object_or_404





'''
Функция получает значение значение параметра из адресной строки.

Функция была написана для того чтоббы







'''

'''
# Передаём первым параметром сам запрос, вторым имя целевого параметра значение которого нужно получить 
def ident_from_url(request):
    ident = request.GET.get("id")
    return  ident 
'''















# Функция возвращающая все строки из курсора (SQL-запроса) в виде словаря
def dictfetchall(cursor): #  
    columns = [col[0] for col in cursor.description]  
    return [dict(zip(columns,row)) 
            for row in cursor.fetchall() 
            ] 
   
#-----------------------------------------------------------------------------------------   
            
# Функция подготавливает данные для формирования JSON объекта
# (Создаёт словарь с текущими данными)
def create_record(obj,fields):
  #данный объект из базы данных возвращает именованный кортеж с полями, сопоставленными со значениями
  Record = namedtuple("Record",fields)
  mappings = dict(zip(fields, obj))
  return  mappings    #(**mappings)   









#-------------------------------------------------------------------------------------------

"""
Функция обходящая RawQuerySet и работающая напрямую с курсором.
Это более надежный способ получить как данные, так и имена колонок, которые нужны для 
формирования ключей словаря. cursor.description предоставляет метаданные о результирующем 
наборе, включая имена колонок.
"""

#  ПОПРОБОВАТЬ ПОДМЕНИТЬ НА ТУ ФУНКЦИЮ КОТОРАЯ ИСПОЛЬЗУЕТСЯ ПРИ ВЫВОДЕ ВСЕХ СОТРУДНИКОВ

def raw_queryset_to_list_dict(
    sql_query: str,
    params: List[Any] = None
) -> List[Dict[str, Any]]:
    """
    Выполняет 'сырой' SQL запрос и преобразует результат в список словарей.
    Каждый словарь представляет строку результата запроса,
    где ключи - имена колонок, а значения - данные.

    Args:
        sql_query: Строка SQL запроса.
        params: Список параметров для запроса (для защиты от SQL-инъекций).

    Returns:
        Список словарей, представляющих результат запроса.
    """
    # Нет прямого способа надежно получить имена колонок из RawQuerySet
    # без доступа к базовому курсору или специфичным для БД метаданным.
    # Проще работать напрямую с курсором.




'''

    result_list: List[Dict[str, Any]] = []

    with connection.cursor() as cursor:
        cursor.execute(sql_query, params or [])

        # Получаем имена колонок из описания курсора
        columns: List[str] = [col[0] for col in cursor.description]

        # Итерируемся по строкам результата
        for row in cursor.fetchall():
            # Создаем словарь, сопоставляя имена колонок и значения
            result_list.append(dict(zip(columns, row)))

    return result_list
  
'''





'''
# Пример использования:
# Предполагаем, что 'reviews' - это другая таблица
sql = """
SELECT
    p.id,
    p.name,
    p.price,
    AVG(r.rating) as average_rating
FROM
    products_product p
LEFT JOIN
    reviews_review r ON p.id = r.product_id
GROUP BY
    p.id, p.name, p.price
ORDER BY
    p.id;
"""

# Получаем список словарей
data_list = raw_queryset_to_list_dict(sql)

# Преобразуем список словарей в JSON строку
json_output = json.dumps(data_list, indent=4, ensure_ascii=False)

# print(json_output)

'''
  
  
  #----------------------------------------------------------------------------------------

'''        
# Работа с методом Raw()  (Образец_Привязка к сериализатору)            
def serialize_raw_queryset(
        sql_query:str,
        # current_serializer: str,  # Добавленная строка
        params: List[Any] = None
    ) -> bytes:
        """
    Выполняет 'сырой' SQL запрос, преобразует результат в список словарей,
    и сериализует его в JSON с использованием DRF Serializer."""
    
    # Сначала получаем данные в виде списка словарей (используем предыдущую функцию)
        data_list: List[Dict[str, Any]] = raw_queryset_to_list_dict(sql_query, params)

    # Инициализируем сериализатор, передавая ему список данных.
    # many=True указывает, что сериализуем список объектов.
        serializer = EmployFullSerializer(data_list, many=True)  # Строка которая была изначально
        
       #   serializer = current_serializer(data_list, many=True) # Новая добавленная строка

    # Проверяем валидность данных, если нужно (для сериализации обычно не требуется)
    # serializer.is_valid() # Это нужно при десериализации (из JSON в Python)

    # Преобразуем сериализованные данные в JSON строку (bytes)
        json_bytes = JSONRenderer().render(serializer.data)

        return json_bytes    
'''