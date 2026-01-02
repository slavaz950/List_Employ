
#from django.contrib import admin # В контексте данного проекта не используется
#from django.urls import path # Определение маршрутов (URL-адресов) для более свежих версий Django (Django 2.0+)
from django.conf.urls import url # Определение маршрутов (URL-адресов) для старых версий Django (например Django 1.10)
from ListEmp.views import   EmpViewSet, EmpViewSetDetail,  PositionViewSetDetail, PositionViewSet  # Импорт наборов представлений 



urlpatterns =  [ 
     # Вариант записи при использовании импорта from django.conf.urls import url (Django 1.10) 
     # Django 1.10 не понимает <int:id> и не сопоставляет URL. 
     # Перепишем маршруты через url() с regex       
     
      # Маршрут для /api/employlist/6/
    url(r'^api/employlist/(?P<id>\d+)/$', EmpViewSetDetail.as_view({'get': 'retrieve','put': 'update', 'delete': 'destroy'}), name='employlist-detail'), 
     
    # Маршрут для /api/positions/5/
    url(r'^api/positions/(?P<id>\d+)/$', PositionViewSetDetail.as_view({'get': 'retrieve','put': 'update', 'delete': 'destroy'}), name='positions-detail'),  
     
    # Список сотрудников
    url(r'^api/employ/$', EmpViewSet.as_view({'get': 'list','post': 'create'}), name='employ-list'),
   
    # Список позиций
    url(r'^api/positions/$', PositionViewSet.as_view({'get': 'list','post': 'create'}), name='positions-list'),     
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








'''
# Вариант записи при использовании импорта from django.urls import path (Django 2.0+)) 
     path("api/employlist/<int:id>/",EmpViewSetDetail.as_view({'get': 'retrieve','put': 'update', 'delete': 'destroy'})),
     path("api/positions/<int:id>/", PositionViewSetDetail.as_view({'get': 'retrieve','put': 'update', 'delete': 'destroy'})),
     path("api/employ/", EmpViewSet.as_view({'get': 'list','post': 'create'})),
     path("api/positions/", PositionViewSet.as_view({'get': 'list','post': 'create'})),
     '''