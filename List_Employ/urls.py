
#from django.contrib import admin # В контексте данного проекта не используется
#from django.urls import path # Определение маршрутов (URL-адресов) для более свежих версий Django (Django 2.0+)
from django.conf.urls import url, include # Определение маршрутов (URL-адресов) для старых версий Django (например Django 1.10)
from django.conf.urls.static import static 
from django.conf import settings
from ListEmp.views import *

urlpatterns =  [ 
     # Вариант записи при использовании импорта from django.conf.urls import url (Django 1.10) 
    url('', include('ListEmp.urls')),      # Маршруты для html-страниц
    url('api/', include('ListEmp.api.urls')) # Маршруты для API   
]
    
# обработку статических файлов (только для разработки):     
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])