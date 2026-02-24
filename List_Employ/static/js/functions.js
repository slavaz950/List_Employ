


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
  const buttonColumn2 = document.createElement("a");   // Создание кнопки (ссылки)
  const buttonColumn3 = document.createElement("a");   // Создание кнопки (ссылки)



  const buttonView = createButtonLink(postId,"Просмотр","http://127.0.0.1:8000/employ/card/")  // Формируем кнопку
  const buttonChange = createButtonLink(postId,"Изменить","http://127.0.0.1:8000/employ/update/")
  const buttonDelete = createButtonLink(postId,"Удалить","http://127.0.0.1:8000/employ/delete/")



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
  buttonColumn.appendChild(buttonView);                                    // Добавляем кнопку
  buttonColumn2.appendChild(buttonChange);
  buttonColumn3.appendChild(buttonDelete);



  // Связываем строку с ячейками
  row.appendChild(FIOColumn);
  row.appendChild(genderColumn);
  row.appendChild(ageColumn);
  row.appendChild(positionColumn);
  row.appendChild(categoryColumn);
  row.appendChild(buttonColumn);
  row.appendChild(buttonColumn2);
  row.appendChild(buttonColumn3);


  //thead.appendChild(tbody);  //////////////////////////////////////////

  return row;  // Результат
 
}











/*

// ФУНКЦИЯ ДЛЯ ФОРМИРОВАНИЯ КНОПКИ
function createButton(idValue,buttonName,Url) {
  var link = Url + idValue + '/' + ';';   // Формируем ссылку на целевую страницу 

  const button = document.createElement("button");        
  button.textContent = buttonName; 

  //button.href = link_card
  //button.target = '_blank';


  button.addEventListener('click', function() {
    window.open(link, '_blank');  // '_blank' — новая вкладка
   });



  return button;    // Результат
}

*/











// ФУНКЦИЯ ДЛЯ ФОРМИРОВАНИЯ КНОПКИ

// Используем <a> с CSS‑стилями (ссылка как кнопка)
// Создаётся обычная ссылка (<a>), но с помощью CSS она выглядит как кнопка.


// В качестве параметров передаём: 
//   - Идентификатор записи
//   - Имя кнопки (которое будет отображаться на самой кнопке)
//   - Основа для URL-адреса для формирования целевого адреса


function createButtonLink(idValue,buttonName,Url) {
  var id_rec = idValue;  // Запоминаем идентификатор записи
  var link_card = Url + id_rec + '/' ;   // Формируем ссылку на целевую страницу (Карточка сотрудника)  + ';'

  const link = document.createElement("a");       
  link.href = link_card
  link.textContent = buttonName;
  link.target = '_self'; 

// Возможные значения target
//  _blank: открытие html-документа в новом окне или вкладке браузера
//  _self: открытие html-документа в том же фрейме (или окне)
//  _parent: открытие документа в родительском фрейме, если ссылка расположена во внутреннем фрейме
//  _top: открытие html-документа на все окно браузера



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






// Обработчик удаления сотрудника  
async function deleteEmployee(id) {
    const confirmed = confirm('Вы уверены, что хотите удалить данного сотрудника?');
    if(confirmed){
        const response = await fetch(`api/employee/${id}/`, {method:'DELETE'});   
        if(response.status === 204){
            location.reload(); // обновляем список после удаления (Аналогично кнопке "Обновить" в браузере)
        }else{
            console.error(`Ошибка удаления сотрудника ${await response.text()}`);
        }
    }
}



// Обработчик удаления должности  api/countpos/${id}/     category
async function deletePosition(id) {
  // Перед удалением, для выполнения дальнейших операций (в случае успеха), необходимо сохранить текущее значение select
  const selectElement = document.getElementById('category');
  const currentCategory = selectElement.value; // Получаем текущее значение select

  const apiInfo = 'api/countpos/' + id + '/'  // Формируем запрос для определения количества сотрудников с удаляемой должностью
  console.log(apiInfo) //
  const info = await fetch(apiInfo)  // Отправляем запрос
  console.log(info)  //
  let count = await info.json();  // Получаем ответ
console.log(count);
  
  const value = Object.values(count)[0];  // Извлекаем единственное значение —  объект имеет один ключ
  console.log(value); // Выводим извлечённое значение

 // console.log(count)  //
  if(value == 0){ //  Если сотрудников с такой должностью нет, то производим удаление этой должности      
    const confirmed = confirm('Вы уверены, что хотите удалить эту должность?');
    if(confirmed){
        const response = await fetch(`api/position/${id}/`, {method:'DELETE'});   
        if(response.status === 204){

          // После успешного удаления сохраняем значение в sessionStorage
         sessionStorage.setItem('returnCategory', currentCategory);
         getPositionList(currentCategory)   // Обновляем данные на странице

           // location.reload(); // обновляем список после удаления (Аналогично кнопке "Обновить" в браузере)  ПОХОЖЕ НЕ НУЖНА СТРОКА
        }else{
            console.error(`Ошибка удаления должности ${await response.text()}`);
        }
    }
  }else{  // Если кто-то из сотрудников занимает удаляемую должность. Выводим информационное сообщение
    alert('Вы не можете удалить эту должность, так как есть сотрудники принятые на эту должность. Количество сотрудников с такой должностью = ' + value);
  }  




}

