
 //console.log(EmployListUrl);
 var apiUrl = "/api/employees/";  //  адрес API-ресурса

sendRequest();
async function sendRequest() {
  response = await fetch(apiUrl, {method: "GET"})  //  '/api/employees/'
  let data = await response.json(); // 

// Отрисовка таблицы сотрудников
    let tbody = document.querySelector('#employees-table tbody');
    tbody.innerHTML = '';  // Очищаем элемент tbody
    for(let i = 0; i < data.length; i++) {


      // Формируем очередную строку таблицы с кнопками для управления текущей записью
        let row = `<tr>  
                    <td>${i+1}</td>                     <!-- Формируем порядковый номер-->
                    <td>${data[i].fio}</td>             <!-- Значение поля "Ф.И.О" -->
                    <td>${data[i].gender_name}</td>     <!-- Значение поля "Пол" -->
                    <td>${data[i].age}</td>             <!-- Значение поля "Возраст" -->
                    <td>${data[i].positions_name}</td>  <!-- Значение поля "Должность" -->
                    <td>${data[i].category_name}</td>   <!-- Значение поля "Категория" -->
                    <td>  <!-- ФОРМИРУЕМ БЛОК КНОПОК НЕОБХОДИМЫХ ДЕЙСТВИЙ ДЛЯ ТЕКУЩЕЙ СТРОКИ -->
                        <button onclick="window.location.href= '/employ/card/${data[i].id}/'" class="btn btn-warning">Карточка</button>
                        <button onclick="window.location.href='/employ/update/${data[i].id}/'" class="btn btn-warning">Редактировать</button>
                        <button onclick="deleteEmployee(${data[i].id})" class="btn btn-danger">Удалить</button>
                    </td>
                  </tr>`;    
        tbody.insertAdjacentHTML('beforeend', row);
        // Вставка сформированного html-кода внутрь тега tbody

        //  .insertAdjacentHTML() — метод DOM, позволяющий вставить строку HTML‑кода 
        //  в указанное место относительно целевого элемента.

        // Первый параметр 'beforeend' — строка, задающая позицию вставки:
        //       - 'beforeend' означает: вставить HTML‑код внутрь целевого элемента, 
        //          сразу после его последнего дочернего элемента. То есть новый контент 
        //          добавится в конец содержимого <tbody>, но внутри него (не после <tbody>).

        // Второй параметр row — строка, содержащая HTML‑код, который нужно вставить. Предполагается, 
        // что переменная row содержит валидную HTML‑строку (например, <tr><td>Данные</td></tr>).
    }
}








/*

//  ПРЕЖНИЙ ВАРИАНТ 
  // -------------------------------------------------

  const table = createTable();  //Создаём таблицу для вывода данных    
  const posts = data;


console.log(response)
console.log(data)
console.log(table)
console.log(posts)

  for(let i = 0; i < posts.length; i++){// Извлекаем из массива все объекты (т.е. целевые данные)
   const post = posts [i];  // Определяем текуший объект, извлечённый из массива
   var row = createRow(post.id,post.fio,post.gender_name,post.age,post.positions_name,post.category_name)  // Формируем строку
   
   table.appendChild(row);   // Добавляем строку в таблицу  








 createButtonLink(post.id,"Карточка","http://127.0.0.1:8000/api/employ/"); 
 
console.log(table)
console.log(contentDiv)


}

contentDiv.appendChild(table);  // Добавляем таблицу в целевой элемент на странице

 */

//}







































/*

sendRequest(); // Получение данных с сервера

// Функция для получения данных с сервера
async function sendRequest() {
  response = await fetch("/api/employ/", { method: "GET"})
  let data = await response.json();

  console.log(data); // Для информации (удалить)

  const employees = data.employs;



document.addEventListener('DOMContentLoaded', () => {
    const tableBody = document.querySelector('#employeesTable tbody');

    // Функция добавления строки сотрудника в таблицу
    function addEmployeeRow(employees) {
        let row = `<tr>
                    <td>${employees.fio}</td>
                    <td>${employees.gender_name}</td>
                    <td>${employees.age}</td>
                    <td>${employees.positions_name}</td>
                    <td>${employees.category_name}</td>
                    <td><button onclick="showDetails(event)">Подробнее</button></td>
                  </tr>`;
        
        tableBody.insertAdjacentHTML('beforeend', row);
    };

    // Заполняем таблицу сотрудниками
    employees.forEach(addEmployeeRow);
});

// Обработчик события нажатия на кнопку "Подробнее"
function showDetails(event) {
    alert(`Вы нажали подробнее для записи 
	${event.target.parentNode.previousElementSibling.textContent}`);
}










} // Закрывающая скобка (ФИНАЛ)
*/