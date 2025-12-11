


from django.contrib import admin
from django.urls import path,include,re_path # Определение маршрутов (URL-адресов)
from rest_framework.routers import DefaultRouter # Автоматическая генерация URL-адресов для классов ViewSet 


from rest_framework import renderers
from rest_framework.urlpatterns import format_suffix_patterns

#from ListEmp import views # Импорт всех представлений проекта
from ListEmp.views import * # Альтернативная запись строки выше
from ListEmp.views import   EmpViewSet, EmpViewSetDetail,  PositionViewSetDetail, PositionViewSet  # EmpAddViewSet,EmpListViewSet, EmpDetailAPIView,  



urlpatterns =  [ 
      
      
     path("api/employlist/<int:id>/",EmpViewSetDetail.as_view({'get': 'retrieve','put': 'update', 'delete': 'destroy'})),
       # path("api/positions/<int:id>/", PositionAPIView.as_view()),
        path("api/positions/<int:id>/", PositionViewSetDetail.as_view({'get': 'retrieve','put': 'update', 'delete': 'destroy'})),
      
      
      path("api/employ/", EmpViewSet.as_view({'get': 'list','post': 'create'})),
         path("api/positions/", PositionViewSet.as_view({'get': 'list','post': 'create'})),
      
      

    
    
    
]
