// ИЗМЕНЕНИЕ ДОЛЖНОСТИ

// Обрабатываем нажатие кнопки "Сохранить"
document.getElementById('formUpdatePosition').addEventListener('submit', function(event) {
    event.preventDefault(); // Отменяем стандартную отправку формы


  // Определяем адрес API-ресурса
  const pathParts = window.location.pathname.split('/');  
  const id = pathParts[3];   // Получаем идентификатор записи
  const APIUrl = 'api/position/' + id + '/';  // Формируем ссылку на API-ресурс

  const form = document.querySelector('#formUpdatePosition');  // Ищем на странице элемент formUpdatePosition
  const formData = new FormData(form); // Создаем экземпляр объекта FormData и передаём ему элемент

  const categoryVal = formData.get('category');     // Получаем текущее значение идентификатора Категории
  sessionStorage.setItem('returnCategory', categoryVal);

  response =  fetch(APIUrl, {  // Задаём адрес API-ресурса для отправки запроса
    method:"PUT",              // Указываем HTTP-метод
    headers: {'Content-Type': 'application/json'  // Указываем тип передаваемого контента
    },  
   body:JSON.stringify(Object.fromEntries(formData)) // преобразуем объект formData в строку формата JSON
   // Метод Object.fromEntries() создаёт новый объект из списка пар ключ-значение  (formData)
 }) 
    .then(response => response.json())    // Получаем ответ от сервера
    .then(location.href = '/positions/')  // Переходим на страницу со списком сотрудников
  }
)
;
