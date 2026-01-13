
#from django.contrib import admin # В контексте данного проекта не используется
#from django.urls import path # Определение маршрутов (URL-адресов) для более свежих версий Django (Django 2.0+)
from django.conf.urls import url # Определение маршрутов (URL-адресов) для старых версий Django (например Django 1.10)
from ListEmp.views import   EmpViewSet, EmpViewSetDetail,  PositionViewSetDetail, PositionViewSet  # Импорт наборов представлений 
from django.conf.urls.static import static 

from django.conf import settings
from ListEmp import views


urlpatterns =  [ 
     # Вариант записи при использовании импорта from django.conf.urls import url (Django 1.10) 
     # Django 1.10 не понимает <int:id> и не сопоставляет URL. 
     # Перепишем маршруты через url() с regex       
     
      #  API для конкретного сотрудника (Просмотр, изменение, удаление) 
    url(r'^api/employee/(?P<id>\d+)/$', EmpViewSetDetail.as_view({'get': 'retrieve','put': 'update', 'delete': 'destroy'}), name='api-employ-detail'), 
     
    # API для конкретной должности сотрудника (Просмотр(СКОРЕЕ ВСЕГО НЕ НУЖЕН - УБРАТЬ 'get': 'retrieve' ), изменение, удаление) 
    url(r'^api/position/(?P<id>\d+)/$', PositionViewSetDetail.as_view({'get': 'retrieve','put': 'update', 'delete': 'destroy'}), name='api-position-detail'),  
     
    
    url(r'^api/employees/$', EmpViewSet.as_view({'get': 'list','post': 'create'}), name='api-employ-list'),  # API для списка сотрудников
    url(r'^api/positions/$', PositionViewSet.as_view({'get': 'list','post': 'create'}), name='api-positions-list'),  # API для списка должностей
    
   
    
    
    url(r'^$', EmpViewSet.as_view({'get': 'list','post': 'create'}), name='index'), 
    
    
    url('', views.get_category, name='get_category'),  #  Получаем категории для определения полей (для динамической подстановки в поле "Должность")
    url('get_positions/', views.get_positions, name='get_positions'),  #  Получаем должности (динамическая подстановка в поле "Должность")
    
        
    #  {% url 'update_card_employ' %}  так можно обратиться к ссылке  в любом месте на странице
    
     
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