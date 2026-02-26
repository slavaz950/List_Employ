// СПИСОК ДОЛЖНОСТЕЙ


// Функция для загрузки данных
async function getPositionList(id) {   

  //let UrlAPI = '' ;  // Очищаем переменную
  UrlAPI = 'api/positions/' + id + '/'; // Формируем ссылку для получения данных
console.log(id)
  response = await fetch(UrlAPI);      // Запрашиваем данные на сервере
  const data = await response.json();  // Получаем ответ от сервера

  let tbody = document.querySelector('#positions-table tbody'); // Ищем на странице элемент positions-table tbody
  tbody.innerHTML = '';                                         // Очищаем элемент tbody
    for(let i = 0; i < data.length; i++) {                      // Перебираем полученные данные
      // Формируем очередную строку таблицы с кнопками для управления текущей записью
        let row = `<tr>  
                    <td class="table-bordered border-primary">${i+1}</td>                     <!-- Формируем порядковый номер-->
                    <td class="table-bordered border-primary">${data[i].name_position}</td>  <!-- Значение поля "Должность" -->
                    <td class="table-bordered border-primary">${data[i].category_name}</td>   <!-- Значение поля "Категория" -->
                    <td style="text-align: center; vertical-align: top;">  <!-- ФОРМИРУЕМ БЛОК КНОПОК НЕОБХОДИМЫХ ДЕЙСТВИЙ ДЛЯ ТЕКУЩЕЙ СТРОКИ -->
                        <button onclick="window.location.href='/position/update/${data[i].id}/'" class="btn btn-outline-primary"">Редактировать</button>
                        <button onclick="deletePosition(${data[i].id})" class="btn btn-outline-danger">Удалить</button>
                    </td>
                  </tr>`; 
        // Вставка сформированного html-кода внутрь тега tbody              
        tbody.insertAdjacentHTML('beforeend', row);  
    }
  }