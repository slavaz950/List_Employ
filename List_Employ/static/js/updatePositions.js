
document.getElementById('formUpdatePosition').addEventListener('submit', function(event) {
    event.preventDefault(); // Отменяем стандартную отправку формы

//async function editEmploy() {
  // Определяем адрес API-ресурса
  const pathParts = window.location.pathname.split('/');  // В скобках указываем разделитель (что считать окончанием каждой из частей)
  const id = pathParts[3];   // Получаем идентификатор записи
  const APIUrl = 'api/position/' + id + '/';
console.log(id);
console.log(APIUrl);





const form = document.querySelector('#formUpdatePosition');
    const formData = new FormData(form); // Создаем экземпляр объекта FormData
console.log(formData)

const categoryVal = formData.get('category');     // Получаем текущее значение идентификатора Категории
sessionStorage.setItem('returnCategory', categoryVal);

  // Проверка содержимого FormData (Для отладки)
  console.log('Содержимое FormData:');
  for (let [key, value] of formData.entries()) {
  console.log(`${key}: ${value}`);
  }

  const response =  fetch(APIUrl, {  
    method:"PUT",
    headers: {'Content-Type': 'application/json'  
    },  
   body:JSON.stringify(Object.fromEntries(formData)) // преобразуем объект formData в строку формата JSON
   // Метод Object.fromEntries() создаёт новый объект из списка пар ключ-значение  (formData)
 }) 
 //;

    .then(response => response.json())
    .then(location.href = '/positions/')  // Переходим на страницу со списком сотрудников


    
 //if (response.ok) {
 // location.href = '/employlist/';
 
  }
//}
)
;




/*

// ФУНКЦИЯ ДЛЯ "ИЗМЕНЕНИЯ КАРТОЧКИ СОТРУДНИКА" 

async function editEmploy() {
  // Определяем адрес API-ресурса
  const pathParts = window.location.pathname.split('/');  // В скобках указываем разделитель (что считать окончанием каждой из частей)
  const id = pathParts[3];   // Получаем идентификатор записи
  const APIUrl = 'api/employee/' + id + '/';

  const form = document.getElementById("formUpdateEmploy");  // Находим форму на html странице
  const formData = new FormData(form);                        // Собираем значения из всех полей ввода

  // Проверка содержимого FormData (Для отладки)
  console.log('Содержимое FormData:');
  for (let [key, value] of formData.entries()) {
  console.log(`${key}: ${value}`);
  }

  const response = await fetch(APIUrl, {  
    method:"PUT",
    headers: {'Content-Type': 'application/json'  
    },  
   body:JSON.stringify(Object.fromEntries(formData)) // преобразуем объект formData в строку формата JSON
   // Метод Object.fromEntries() создаёт новый объект из списка пар ключ-значение  (formData)
 }) 
 //;

    .then(response => response.json())
    .then(location.href = '/employlist/')  // В случае успешного создания сотрудника, переходим к списку сотрудников


 //if (response.ok) {
  location.href = '/employlist/';
 
  }
//}
;

*/