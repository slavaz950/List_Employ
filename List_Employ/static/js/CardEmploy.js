// КАРТОЧКА СОТРУДНИКА 

getEmployDetail()

// Функция для получения данных для "Карточки сотрудника"
async function getEmployDetail() { 
  // Разбираем на части текущий url-адрес для получения актуального идентификатора 
  const pathParts = window.location.pathname.split('/');  // В скобках указываем разделитель (что считать окончанием каждой из частей)
  const Id = pathParts[3];                                // Получаем идентификатор записи
  const UrlAPI = 'api/employee/' + Id + '/';              // Формируем ссылку для получения данных

  response = await fetch(UrlAPI, {method:"GET"})  // Запрашиваем данные на сервере
  let  data = await response.json(); // Получаем данные с сервера в формате json
   
// Обновляем значение заголовка страницы
  document.title = data.fio + ' - ' + 'Личная карточка' ;

 let card = document.querySelector('#employees-card'); // Ищем на текущей странице элемент employees-card
    card.innerHTML = '';  // Очищаем элемент employees-card
   
  // Формируем блок с целевыми данными  
  let content = `<div class="card" style="width: 18rem;">
                          <ul class="list-group list-group-flush m-6">
                              <li class="list-group-item"><b>Ф.И.О:</b>&emsp;${data.fio}</li>  
                              <li class="list-group-item"><b>Пол:</b>&emsp;${data.gender_name}</li>
                              <li class="list-group-item"><b>Возраст:</b>&emsp;${data.age}</li>
                          </ul>
                        </div>
                        <br>
                        <button onclick="window.location.href='/employ/update/${data.id}/'" class="btn btn-outline-primary">Изменить карточку сотрудника</button>
                        <button onclick="window.location.href='/employlist/'" class="btn btn-outline-primary">Вернуться к списку сотрудников</button>`;    
        card.insertAdjacentHTML('beforeend', content);

return  card;  // Возвращаем блок с целевыми данными
 }

