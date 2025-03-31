


#from django.contrib import admin
from django.urls import path # type: ignore
#from .views import index


from ListEmp import views

urlpatterns = [
    
   # path('admin/', admin.site.urls),
    
    path('',views.index, name='index'),
    
    
    
    
]
