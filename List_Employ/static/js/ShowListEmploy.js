// СПИСОК СОТРУДНИКОВ
 
 var apiUrl = "/api/employees/";  //  адрес API-ресурса

getEmployList();
async function getEmployList() {
  response = await fetch(apiUrl, {method: "GET"})  // Запрашиваем данные на сервере
  let data = await response.json(); // Получаем объект от сервера

// Отрисовка таблицы сотрудников
    let tbody = document.querySelector('#employees-table tbody'); // Ищем на странице элемент employees-table tbody
    tbody.innerHTML = '';  // Очищаем элемент tbody
    for(let i = 0; i < data.length; i++) { // Перебираем полученные данные
      // Формируем очередную строку таблицы с кнопками для управления текущей записью
        let row = `<tr>  
                    <td class="table-bordered border-primary">${i+1}</td>                     <!-- Формируем порядковый номер-->
                    <td class="table-bordered border-primary">${data[i].fio}</td>             <!-- Значение поля "Ф.И.О" -->
                    <td class="table-bordered border-primary">${data[i].gender_name}</td>     <!-- Значение поля "Пол" -->
                    <td class="table-bordered border-primary">${data[i].age}</td>             <!-- Значение поля "Возраст" -->
                    <td  class="table-bordered border-primary">${data[i].positions_name}</td>  <!-- Значение поля "Должность" -->
                    <td class="table-bordered border-primary">${data[i].category_name}</td>   <!-- Значение поля "Категория" -->
                    <td style="text-align: center; vertical-align: top;">  <!-- ФОРМИРУЕМ БЛОК КНОПОК НЕОБХОДИМЫХ ДЕЙСТВИЙ ДЛЯ ТЕКУЩЕЙ СТРОКИ -->
                        <button onclick="window.location.href= '/employ/card/${data[i].id}/'" class="btn btn-outline-primary">Карточка</button>
                        <button onclick="window.location.href='/employ/update/${data[i].id}/'" class="btn btn-outline-primary"">Редактировать</button>
                        <button onclick="deleteEmployee(${data[i].id})" class="btn btn-outline-danger">Удалить</button>
                    </td>
                  </tr>`;                   
        // Вставка сформированного html-кода внутрь тега tbody         
        tbody.insertAdjacentHTML('beforeend', row);
    }
}
