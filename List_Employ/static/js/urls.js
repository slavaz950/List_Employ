
//<script type="text/javascript">



var EmployCardUrl = "{% url 'employ-card' %}";       // Переход на страницу "Карточка сотрудника" 
var EmployUpdateUrl = "{% url 'employ-update' %}";   // Переход на страницу "Изменение данных о сотруднике" 
var EmploySaveUrl = "{% url 'employ-save' %}";       // Сохранение (обновление) данных сотрудника" 
var EmployDeleteUrl = "{% url 'employ-delete' %}";   // Удаление сотрудника
var EmployNewUrl = "{% url 'employ-new' %}";         // Переход на страницу "Добавление сотрудника" 
var EmployAddUrl = "{% url 'employ-add' %}";         // Сохранение (добавление) нового сотрудника

// Динамические значения в selectе при выборе должности
var GetPositionsdUrl = "{% url 'get-positions' %}";  // Получаем список всех должностей (отсортированных по категориям)  
var GetCategoriesUrl = "{% url 'get-categories' %}"; //  Получаем список всех категорий 

var EmployListUrl = "{% url 'employ-list' %}";       //  список Сотрудников   
//var EmployCardUrl = 'employ-card'; 
//var EmployCardUrl = 'employ-card';
//var EmployCardUrl = 'employ-card';  




//</script>



// Доступ к этим значениям возможен в любом месте JS-кода
// console.log(EmployCardUrl); // Выводит URL для перехода на страницу "Карточка сотрудника" 



/*

// ОБРАЗЕЦ
window.djangoUrls = {
        'home': "{% url 'home' %}",
        'about': "{% url 'about' %}",
        'contact': "{% url 'contact' %}"
    };

    */



    // ПОТЕСТИТЬ ЭТОТ ВАРИАНТ И ВЫБРАТЬ ОПТИМАЛЬНЫЙ
// Объявляем объект с маршрутами
    window.djangoUrls = { // Прописываем все маршруты используемые в проекте
		'employ-card': "{% url 'employ-card' %}",  // Переход на страницу "Карточка сотрудника" 
		'employ-update': "{% url 'employ-update' %}", // Переход на страницу "Изменение данных о сотруднике" 
		'employ-save': "{% url 'employ-save' %}",   // Сохранение (обновление) данных сотрудника" 
		'employ-delete': "{% url 'employ-delete' %}", // Удаление сотрудника
		'employ-new': "{% url 'employ-new' %}",    // Переход на страницу "Добавление сотрудника" 
		'employ-add': "{% url 'employ-add' %}",    // Сохранение (добавление) нового сотрудника 
		'get-positions': "{% url 'get-positions' %}", // Получаем список всех должностей (отсортированных по категориям)
		'get-categories': "{% url 'get-categories' %}", //  Получаем список всех категорий 
		'employ-list': "{% url 'employ-list' %}",    //  список Сотрудников 
		
        
    };


    // ДОСТУП К ССЫЛКАМ ЭТОГО ВАРИАНТА ???