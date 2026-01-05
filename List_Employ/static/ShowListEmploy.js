

sendRequest(); // Получение данных с сервера

// Функция для получения данных с сервера
async function sendRequest() {
  response = await fetch("/api/employ/", { method: "GET"})
  let data = await response.json();

  console.log(data); // Для информации (удалить)

  const employees = data.employs;



   employees.fio,
	employees.gender_name,
	employees.age,
	employees.positions_name,
	employees.category_name



document.addEventListener('DOMContentLoaded', () => {
    const tableBody = document.querySelector('#employeesTable tbody');

    // Функция добавления строки сотрудника в таблицу
    function addEmployeeRow(employeeData) {
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
