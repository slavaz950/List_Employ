
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
     url(r'^employ/update/(?P<id>\d+)/$', employUpdateView,name='employ-update'),  # Переход на страницу "Изменение данных о сотруднике" 
   #  url(r'^employ/update-save/(?P<id>\d+)/$', employUpdateSave,name='employ-save'),  # Сохранение после обновления данных сотрудника 
   #  url(r'^employ/delete/(?P<id>\d+)/$', employDelete,name='employ-delete'),  # Удаление сотрудника
    
    # EmployViewDetail.as_view()
    
    
    url(r'^employ/new/$', EmpNewAdd,name='employ-new'),  # Переход на страницу "Добавление сотрудника" 
    # url(r'^employ/add/$', EmployView.as_view() ,name='employ-add'),  # Сохранение (добавление) нового сотрудника   EmployView.as_view()    add_employ
     
    
    
    url('^get_positions/<int:category>/', get_positions, name='get-positions'),  # Получаем список всех должностей (отсортированных по категориям)

    
    url(r'get_positions/(?P<category>\d+)/$', get_positions, name='get-positions'),  # Получаем список всех должностей (отсортированных по категориям)
    url(r'^get_categories/$', get_category,name='get-categories'),  # Получаем список всех категорий  
    
     
    url(r'^employlist/$', ListEmp ,name='employ-list'),  # список Сотрудников  name='employ-list'      name='employ-list'  EmployView.as_view()
   
    
     
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