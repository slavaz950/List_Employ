
#from django.contrib import admin # В контексте данного проекта не используется
#from django.urls import path # Определение маршрутов (URL-адресов) для более свежих версий Django (Django 2.0+)
from django.conf.urls import url # Определение маршрутов (URL-адресов) для старых версий Django (например Django 1.10)
from django.conf.urls.static import static 
from django.conf import settings
from ListEmp.api.views import *

urlpatterns =  [ 
      
    url(r'^employee/(?P<id>\d+)/$', EmpViewSetDetail.as_view({'get': 'retrieve','put': 'update', 'delete': 'destroy'}), name='api-employ-detail'), #  API для конкретного сотрудника 
    url(r'^position/(?P<id>\d+)/$', PositionViewSetDetail.as_view({'get': 'retrieve','put': 'update', 'delete': 'destroy'}), name='api-position-detail'), # API для конкретной должности   
    url(r'^positions/(?P<category>\d+)/$', PositionViewSet.as_view({'get': 'list','post': 'create'}), name='api-positions-list'),  # API для списка должностей 
    url(r'^countpos/(?P<positions>\d+)/$', countEmpByPositions, name='api-positions-count'),   # API для списка Категорий
    url(r'^category/$', CategoryViewSet.as_view({'get': 'list','post': 'create'}), name='api-category-list'),  # API для списка Категорий
    url(r'^employees/$', EmpViewSet.as_view({'get': 'list','post': 'create'}), name='api-employ-list'),  # API для списка сотрудников   
]

'''
    Вариант записи при использовании импорта from django.conf.urls import url (Django 1.10)
    Разбор regex-шаблона:
    
     ^ — начало строки.
     api/employlist/ — фиксированная часть URL.
    (?:P<id>\d+) — именованная группа:
    ?P<id> — имя параметра (передаётся в view как id).
    \d+ — любое количество цифр.
    $ — конец строки.
   / — завершающая косая черта (если нужна).
    
    ''' 

# обработку статических файлов (только для разработки):     
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])