


#from django.contrib import admin
from django.urls import path,include # type: ignore
#from .views import index, get_datalistemploy,ViewAPI


from ListEmp import views

urlpatterns = [
    
   # path('admin/', admin.site.urls),  # В данном проекте этот маршрут не используется
    
   # Маршруты для "Списка сотрудников" 
    path('',views.index, name='index'),
    path('api_ListEmp/',views.ViewAPI.as_view(),name='api_ListEmp'), # Список сотрудников
    
    # Маршруты для "Личной карточки сотрудника" 
    path('card/',views.card_employ, name='card_employ'),    
    path('api_CardEmp/',views.CardAPI.as_view(),name='api_CardEmp'),    # Карточка сотрудника 
    
    
    # Маршруты для "Списка должностей"
    path('positions/',views.list_positions, name='positions'),   
    path('api_Position/',views.Get_positionsAPI.as_view(),name='api_Position'),    # Список должностей
    
    # Маршруты для изменения "Списка должностей"
    path('change_position/',views.update_positions, name='change_position')   
   # path('api_ChangePosition/',views.Get_positionsAPI.as_view(),name='api_Position')
    
]
