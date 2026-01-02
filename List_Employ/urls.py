
#from django.contrib import admin # В контексте данного проекта не используется
#from django.urls import path # Определение маршрутов (URL-адресов) для более свежих версий Django (Django 2.0+)
from django.conf.urls import url # Определение маршрутов (URL-адресов) для старых версий Django (например Django 1.10)
from ListEmp.views import   EmpViewSet, EmpViewSetDetail,  PositionViewSetDetail, PositionViewSet  # Импорт наборов представлений 



urlpatterns =  [ 
     # Вариант записи при использовании импорта from django.conf.urls import url (Django 1.10)           
     url("api/employlist/<int:id>/",EmpViewSetDetail.as_view({'get': 'retrieve','put': 'update', 'delete': 'destroy'})),
     url("api/positions/<int:id>/", PositionViewSetDetail.as_view({'get': 'retrieve','put': 'update', 'delete': 'destroy'})),
     url("api/employ/", EmpViewSet.as_view({'get': 'list','post': 'create'})),
     url("api/positions/", PositionViewSet.as_view({'get': 'list','post': 'create'})),      
]

'''
# Вариант записи при использовании импорта from django.urls import path (Django 2.0+)) 
     path("api/employlist/<int:id>/",EmpViewSetDetail.as_view({'get': 'retrieve','put': 'update', 'delete': 'destroy'})),
     path("api/positions/<int:id>/", PositionViewSetDetail.as_view({'get': 'retrieve','put': 'update', 'delete': 'destroy'})),
     path("api/employ/", EmpViewSet.as_view({'get': 'list','post': 'create'})),
     path("api/positions/", PositionViewSet.as_view({'get': 'list','post': 'create'})),
     '''