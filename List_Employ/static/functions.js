


// Функция для создания таблицы
function createTable() {
  const table = document.createElement("table");              // Создание таблицы
  
  const thead = document.createElement("thead");               // Создание заголовочной части таблицы
  const headerRow = document.createElement("tr");              // Создание строки таблицы (в данном случае строки-заголовка)
  const FIOColumnHeader = document.createElement("th");        // Создание ячейки для заголовка "Ф.И.О"
  const genderColumnHeader = document.createElement("th");     // Создание ячейки для заголовка "Пол"
  const ageColumnHeader = document.createElement("th");        // Создание ячейки для заголовка "Возраст"
  const positionColumnHeader = document.createElement("th");   // Создание ячейки для заголовка "Должность"
  const categoryColumnHeader = document.createElement("th");   // Создание ячейки для заголовка "Категория"
  //const buttonColumnHeader = document.createElement("th");     // Формируем ячейку для кнопки
 // buttonColumnHeader.classList.add('special-cell');            // Добавляем новый класс для текущей ячейки (кнопки) 
                                                               // (чтобы сбросить всё форматирование которое есть у других ячеек)
                                                               // Это сделано для того чтоб границы этой ячейки не отображались 
                                                               
  // Установка заголовков для ячеек "шапки" таблицы
  FIOColumnHeader.appendChild(document.createTextNode("Ф.И.О."));         // Шапка таблицы. Заголовок для столбца "Ф.И.О." 
  genderColumnHeader.appendChild(document.createTextNode("Пол"));         // Шапка таблицы. Заголовок для столбца "Пол"
  ageColumnHeader.appendChild(document.createTextNode("Возраст"));        // Шапка таблицы. Заголовок для столбца "Возраст"
  positionColumnHeader.appendChild(document.createTextNode("Должность")); // Шапка таблицы. Заголовок для столбца "Должность"
  categoryColumnHeader.appendChild(document.createTextNode("Категория")); // Шапка таблицы. Заголовок для столбца "Категория"
 // buttonColumnHeader.appendChild(document.createTextNode(""));            // Столбец под кнопки (Резервируем место)

  // Связываем строки с ячейками
  headerRow.appendChild(FIOColumnHeader);
  headerRow.appendChild(genderColumnHeader);
  headerRow.appendChild(ageColumnHeader);
  headerRow.appendChild(positionColumnHeader);
  headerRow.appendChild(categoryColumnHeader);
  //headerRow.appendChild(buttonColumnHeader);

  //thead.appendChild(headerRow)

  table.appendChild(thead);      // 

  table.appendChild(headerRow);      // Добавляем сформированную строку в таблицу

  return table;    // Результат
}








// Функция для создания одной строки для таблицы
function createRow(postId,postFIO,postGender,postAge,postPosition,postCategory) {

  const row = document.createElement("tr");        // Создание строки
  const FIOColumn = document.createElement("td");        //  Создание ячейки "Ф.И.О"
  const genderColumn = document.createElement("td");     // Создание для ячейки  "Пол"
  const ageColumn = document.createElement("td");        // Создание ячейки "Возраст"
  const positionColumn = document.createElement("td");   // Создание ячейки "Должность"
  const categoryColumn = document.createElement("td");   // Создание ячейки "Категория"
  const buttonColumn = document.createElement("a");   // Создание кнопки (ссылки)

  const button = createButtonLink(postId,"Кнопка","http://127.0.0.1:8000/api/employ/")  // Формируем кнопку
  // В качестве параметров передаём в функцию:
  //    - Идентификатор записи на которую будем ссылаться
  //    - Наименование кнопки (Имя которое будет отображаться на странице (то что будет видеть пользователь))
  //    - Основа для URL-ссылки, из которой будет формироваться целевой адрес страницы
  
  // Вставка значений в ячееки  таблицы
  FIOColumn.appendChild(document.createTextNode(postFIO));   
  genderColumn.appendChild(document.createTextNode(postGender));
  ageColumn.appendChild(document.createTextNode(postAge));
  positionColumn.appendChild(document.createTextNode(postPosition));
  categoryColumn.appendChild(document.createTextNode(postCategory));
  buttonColumn.appendChild(button);                                    // Добавляем кнопку

  // Связываем строку с ячейками
  row.appendChild(FIOColumn);
  row.appendChild(genderColumn);
  row.appendChild(ageColumn);
  row.appendChild(positionColumn);
  row.appendChild(categoryColumn);
  row.appendChild(buttonColumn);


  //thead.appendChild(tbody);  //////////////////////////////////////////

  return row;  // Результат
 
}









// ФУНКЦИЯ ДЛЯ ФОРМИРОВАНИЯ КНОПКИ

// Используем <a> с CSS‑стилями (ссылка как кнопка)
// Создаётся обычная ссылка (<a>), но с помощью CSS она выглядит как кнопка.


// В качестве параметров передаём: 
//   - Идентификатор записи
//   - Имя кнопки (которое будет отображаться на самой кнопке)
//   - Основа для URL-адреса для формирования целевого адреса


function createButtonLink(idValue,buttonName,Url) {
  var id_rec = idValue;  // Запоминаем идентификатор записи
  var link_card = Url + id_rec + '/' + ';';   // Формируем ссылку на целевую страницу (Карточка сотрудника)

  const link = document.createElement("a");       
  link.href = link_card
  link.textContent = buttonName;
  link.target = '_blank'; 


/*

  // Стилизуем как кнопку
  link.style.display = 'inline-block';
  link.style.padding = '10px 15px';
  link.style.backgroundColor = '#007bff';
  link.style.color = 'white';
 // link.style.textDecoration = 'none';
  link.style.borderRadius = '4px';
  link.style.margin = '5px';

*/

  
  return link;    // Результат
}



//--------------------------------------------
// ДЛЯ ИНТЕГРАЦИИ В КОД
// Вставляем в документ
//document.body.appendChild(link);

