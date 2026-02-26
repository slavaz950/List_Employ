// ИЗМЕНЕНИЕ КАРТОЧКИ СОТРУДНИКА

// Обрабатываем нажатие кнопки "Сохранить"
document.getElementById('formUpdateEmploy').addEventListener('submit', function(event) {
    event.preventDefault(); // Отменяем стандартную отправку формы


    // Определяем адрес API-ресурса
    const pathParts = window.location.pathname.split('/'); 
    const id = pathParts[3];                     // Получаем идентификатор записи
    const APIUrl = 'api/employee/' + id + '/';   // Формируем адрес API-ресурса

    const form = document.querySelector('#formUpdateEmploy');  // Ищем на стоанице элемент formUpdateEmploy
    const formData = new FormData(form); // Создаем экземпляр объекта FormData и передаём ему найденный элемент

// const 
    response =  fetch(APIUrl, {  // Задаём адрес API-ресурса для отправки запроса
    method:"PUT",                // Указываем HTTP-метод
    headers: {'Content-Type': 'application/json'  // Указываем тип передаваемого контента
    },  
    body:JSON.stringify(Object.fromEntries(formData)) // преобразуем объект formData в строку формата JSON
   // Метод Object.fromEntries() создаёт новый объект из списка пар ключ-значение  (formData)
 }) 
    .then(response => response.json())      // Получаем ответ от сервера
    .then(location.href = '/employlist/')  // В случае успешного изменения карточки сотрудника, переходим к списку сотрудников
  }
)
;
