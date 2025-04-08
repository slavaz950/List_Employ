// Функция для создания HTML таблицы из JSON данных
function createTableFromJson(jsonData, tableId) {
  // Получаем ссылку на элемент таблицы
  const table = document.getElementById(tableId);

  // Если данные отсутствуют, выходим из функции
  if (!jsonData || jsonData.length === 0) {
    table.innerHTML = '<p>Нет данных для отображения.</p>';
    return;
  }

  // Получаем ключи первого объекта для создания заголовков таблицы
  const columns = Object.keys(jsonData[0]);
  let headerRow = '<tr>';
  columns.forEach(column => headerRow += `<th>${column}</th>`);
  headerRow += '</tr>';
  table.innerHTML = headerRow;

  // Создаем строки таблицы на основе JSON данных
  jsonData.forEach(item => {
    let row = '<tr>';
    columns.forEach(column => row += `<td>${item[column]}</td>`);
    row += '</tr>';
    table.innerHTML += row;
  });
}

// Пример использования:
// JSON данные (замените на свои данные)
const data = [
  { "name": "Иван", "age": 30, "city": "Москва" },
  { "name": "Мария", "age": 25, "city": "Санкт-Петербург" }
];

// Вызываем функцию для создания таблицы
createTableFromJson(data, "myTable");
