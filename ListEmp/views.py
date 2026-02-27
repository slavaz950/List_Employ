
from django.shortcuts import  render # Объединяет шаблон HTML с данными контекста и возвращает объект HttpResponse с отрисованным содержимым

     
# СОТРУДНИКИ   
  
# Переход на страницу со списком сотрудников
def ListEmp(request):
    # Просто возвращаем рендеринг шаблона add_employ.html
    return render(request, 'ListEmp/show_listEmploy.html')


# Переход на страницу добавления нового сотрудника
def EmpNewAdd(request):
    # Просто возвращаем рендеринг шаблона add_employ.html
    return render(request, 'ListEmp/add_employ.html')


# Переход на страницу просмотра карточки сотрудника
def EmpCardView(request,id):
    # Просто возвращаем рендеринг шаблона card_employ.html
    return render(request, 'ListEmp/card_employ.html')
   
    
# Переход на страницу изменения сотрудника 
def employUpdateView(request,id):
    return render(request, 'ListEmp/update_card_employ.html')  # Отображаем HTML-шаблон с указанными данными
 
 
 # ---------------------------------------------------------------------------------------------------
 
 # ДОЛЖНОСТИ
 
 # Переход на страницу со списком должностей
def ListPositions(request):
    # Просто возвращаем рендеринг шаблона add_employ.html
    return render(request, 'ListEmp/show_listPosition.html')

 
 
# Переход на страницу добавления новой должности
def NewAddPositions(request):
    # Просто возвращаем рендеринг шаблона add_employ.html
    return render(request, 'ListEmp/add_positions.html')
 
 
 # Переход на страницу изменения должности 
def UpdateViewPositions(request,id):
    return render(request, 'ListEmp/update_positions.html')  # Отображаем HTML-шаблон с указанными данными
 
 
          