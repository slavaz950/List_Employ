 
// Получаем данные с сервера



getEmployDetail()
// ФУНУЦИЯ ДЛЯ ПОЛУЧЕНИЯ ДАННЫХ ДЛЯ "КАРТОЧКИ СОТРУДНИКА" 
async function getEmployDetail() {  
  const pathParts = window.location.pathname.split('/');  // В скобках указываем разделитель (что считать окончанием каждой из частей)
  const Id = pathParts[3];   // Получаем идентификатор записи
  const UrlAPI = 'http://127.0.0.1:8000/api/employee/' + Id + '/'; // Формируем ссылку для получения данных

  response = await fetch(UrlAPI, {method:"GET"})  // Запрашиваем данные на сервере
  let  data = await response.json(); // Получаем данные с сервера в формате json
   
// Обновляем значение заголовка страницы
  document.title = data.fio + ' - ' + 'Личная карточка' ;



 /* 
//  Формируем ссылку для кнопки "Изменить карточку сотрудника"
  const Url = 'http://127.0.0.1:8000/employ/update/' + Id + '/'; // Формируем ссылку для получения данных
 // const Url = {% url 'employ-update'  id   %}; // Формируем ссылку для получения данных

  const form = document.getElementById('"changeCard"')
  form.action = Url;  // Меняем action
  console.log('Новый action:', form.action);   // Можно проверить результат

*/

// Вывод данных на страницу
const contentDiv = document.getElementById("result");

const FIODiv = document.getElementById("result-fio");
FIODiv.appendChild(document.createTextNode('Ф.И.О.:       ' + '' + '' + '' + '' + '' + '' + '' + '' + data.fio)); 

const genderDiv = document.getElementById("result-gender");
genderDiv.appendChild(document.createTextNode('Пол:       ' + '' + '' + '' + '' + '' + '' + '' + '' + data.gender_name)); 

const ageDiv = document.getElementById("result-age");
ageDiv.appendChild(document.createTextNode('Возраст:       ' + '' + '' + '' + '' + '' + '' + '' + '' + data.age));  
  
  // Связываем данные с div-контейнером
  contentDiv.appendChild(FIODiv);
  contentDiv.appendChild(genderDiv);
  contentDiv.appendChild(ageDiv);
  

  return  contentDiv;  // Результат
 }
//}