
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
     
     
     
    # url(r'^api/position/(?P<category>\d+)/(?P<id>\d+)/$', PositionViewSetDetail.as_view({'get': 'retrieve','put': 'update', 'delete': 'destroy'}), name='api-position-detail') 
    # url(r'^api/positions/(?P<category>\d+)/$', PositionViewSetDetail.as_view({'get': 'retrieve','put': 'update', 'delete': 'destroy'}), name='api-position-detail') 
       
     

    
    
    
    
    
    
    # url(r'^employ/(?P<id>\d+)/$', EmployView.as_view(), name='employ-detail'), # Просмотр карточки сотрудника
    url(r'^employ/new/$', EmpNewAdd,name='employ-new'),  # Переход на страницу "Добавление сотрудника" 
     url(r'^employ/add/$', EmployView.as_view(),name='employ-add'),  # Сохранение (добавление) нового сотрудника 
     
    
    
    
    

    
    
    
    url('get_positions/<int:id_category>', get_positions, name='get-positions'),  # Получаем список всех должностей (отсортированных по категориям)
    
    url(r'^get_categories/$', get_category,name='get-categories'),  # Получаем список всех категорий  
    
    
    
    
     
    url(r'^employlist/$', EmployView.as_view(),name='employ-list'),  # список Сотрудников  name='employ-list'      name='employ-list'
   
    

    url(r'^$', EmpViewSet.as_view({'get': 'list','post': 'create'}), name='index'), 
    
    
   #   url('', views.get_category, name='get_category'),  #  Получаем категории для определения полей (для динамической подстановки в поле "Должность")
   #   url('get_positions/', views.get_positions, name='get_positions'),  #  Получаем должности (динамическая подстановка в поле "Должность")
    
        
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