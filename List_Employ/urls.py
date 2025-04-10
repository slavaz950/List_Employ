


#from django.contrib import admin
from django.urls import path,include # type: ignore
#from .views import index, get_datalistemploy,ViewAPI


from ListEmp import views

urlpatterns = [
    
   # path('admin/', admin.site.urls),
    
   path('',views.index, name='index'),
    path('api_ListEmp/',views.ViewAPI.as_view(),name='api_ListEmp'), 
    
    path('card/',views.card_employ, name='card_employ'),    # <int:id>
    path('api_CardEmp/',views.CardAPI.as_view(),name='api_CardEmp')
    
    #
    
    
    #path('get-json/',views.get_datalistemploy, name='get-json'),
   #path('',views.ViewAPI.as_view(),name='index'),
    
    
    
 
     
    
    
]
