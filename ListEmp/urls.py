
#from django.contrib import admin # В контексте данного проекта не используется
#from django.urls import path # Определение маршрутов (URL-адресов) для более свежих версий Django (Django 2.0+)
from django.conf.urls import url # Определение маршрутов (URL-адресов) для старых версий Django (например Django 1.10)
#from ListEmp.views import   EmpViewSet, EmpViewSetDetail,  PositionViewSetDetail, PositionViewSet,EmployGetViews  # Импорт наборов представлений 
from django.conf.urls.static import static 

from django.conf import settings
#from ListEmp import views
from ListEmp.views import *


urlpatterns =  [ 
     # Вариант записи при использовании импорта from django.conf.urls import url (Django 1.10) 
     # Django 1.10 не понимает <int:id> и не сопоставляет URL. 
     # Перепишем маршруты через url() с regex       
     
    url(r'^employ/card/(?P<id>\d+)/$', EmpCardView ,name='employ-card'),  # Переход на страницу "Карточка сотрудника" 
    url(r'^position/update/(?P<id>\d+)/$', UpdateViewPositions ,name='employ-update'),  # Переход на страницу "Изменение должности "
    url(r'^employ/update/(?P<id>\d+)/$', employUpdateView,name='employ-update'),  # Переход на страницу "Изменение данных о сотруднике" 
    url(r'^position/new/$', NewAddPositions ,name='position-new'),  # Переход на страницу "Добавление должности"
    url(r'^employ/new/$', EmpNewAdd,name='employ-new'),  # Переход на страницу "Добавление сотрудника" 
    url(r'^positions/$', ListPositions ,name='positions-list'),  # список должностей
    url(r'^employlist/$', ListEmp ,name='employ-list'),  # список Сотрудников     
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
     
     
# обработку статических файлов (только для разработки):     
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])