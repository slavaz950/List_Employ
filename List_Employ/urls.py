
#from django.contrib import admin
from django.urls import path # Определение маршрутов (URL-адресов)
from ListEmp.views import   EmpViewSet, EmpViewSetDetail,  PositionViewSetDetail, PositionViewSet  # EmpAddViewSet,EmpListViewSet, EmpDetailAPIView,  



urlpatterns =  [ 
     path("api/employlist/<int:id>/",EmpViewSetDetail.as_view({'get': 'retrieve','put': 'update', 'delete': 'destroy'})),
     path("api/positions/<int:id>/", PositionViewSetDetail.as_view({'get': 'retrieve','put': 'update', 'delete': 'destroy'})),
     path("api/employ/", EmpViewSet.as_view({'get': 'list','post': 'create'})),
     path("api/positions/", PositionViewSet.as_view({'get': 'list','post': 'create'})),
]
