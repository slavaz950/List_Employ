 
 
//getEmployForUpdate()
// ФУНКЦИЯ ДЛЯ ПОЛУЧЕНИЯ ДАННЫХ ДЛЯ "ИЗМЕНЕНИЯ КАРТОЧКИ СОТРУДНИКА" 




const form = document.getElementById('UpdateEmployForm');  // Находим форму на html странице
const data = new FormData(form);                        // Собираем значения из всех полей ввода
console.log(data)





async function getEmployForUpdate() {  
  const pathParts = window.location.pathname.split('/');  // В скобках указываем разделитель (что считать окончанием каждой из частей)
  const Id = pathParts[3];   // Получаем идентификатор записи
  const Url = 'http://127.0.0.1:8000/api/employee/' + Id + '/'; // Формируем ссылку для получения данных

  response = await fetch(Url, {
    method:"PUT",
  //  headers: {'Content-Type': 'application/json'
   // },
    body: data   // FormData автоматически устанавливает Content-Type
  
  })  // Запрашиваем данные на сервере
  let  data = await response.json(); // Получаем данные с сервера в формате json
   
  


 };