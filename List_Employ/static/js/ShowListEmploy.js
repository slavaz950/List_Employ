
const contentDiv = document.getElementById("result"); // Переменная contentDiv определяет элемент в котором будем работать
    
  var requestURL = "/api/employ/";   // URL ресурса где хранится JSON
  var url = "http://127.0.0.1:8000/api/employ/";




sendRequest();
async function sendRequest() {
  response = await fetch("/api/employ/", {method: "GET"})
  let data = await response.json(); // Получаем данные с сервера в формате
  console.log(data);
  console.log(data.employs);

  const table = createTable();  //Создаём таблицу для вывода данных
  const posts = data.employs;

  for(let i = 0; i < posts.length; i++){// Извлекаем из массива все объекты (т.е. целевые данные)
   const post = posts [i];  // Определяем текуший объект, извлечённый из массива
   var row = createRow(post.id,post.fio,post.gender_name,post.age,post.positions_name,post.category_name)  // Формируем строку
   
   table.appendChild(row);   // Добавляем строку в таблицу  



/*
function createButtonLink(idValue,buttonName,Url) {
  var id_rec = idValue;  // Запоминаем идентификатор записи
  var link_card = Url + id_rec + '/' + ';';   // Формируем ссылку на целевую страницу (Карточка сотрудника)

  const link = document.createElement("a");       
  link.href = link_card
  link.textContent = buttonName;
  link.target = '_blank'; 


  return link;    // Результат
}
*/

 createButtonLink(post.id,"Карточка","http://127.0.0.1:8000/api/employ/"); 
 





  //const buttonColumn = document.createElement("a");   // Создание кнопки (ссылки)

 // const button = createButtonLink(post.id,"Кнопка","http://127.0.0.1:8000/api/employ/")  // Формируем кнопку
  // В качестве параметров передаём в функцию:
  //    - Идентификатор записи на которую будем ссылаться
  //    - Наименование кнопки (Имя которое будет отображаться на странице (то что будет видеть пользователь))
  //    - Основа для URL-ссылки, из которой будет формироваться целевой адрес страницы

}

contentDiv.appendChild(table);  // Добавляем таблицу в целевой элемент на странице

   
  // console.log(posts.length);

  //};
   

}














































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