// УДАЛЕНИЕ ЗАПИСЕЙ ИЗ БД


// Обработка удаления сотрудника  
async function deleteEmployee(id) {
    const confirmed = confirm('Вы уверены, что хотите удалить данного сотрудника?');
    if(confirmed){
        const response = await fetch(`api/employee/${id}/`, {method:'DELETE'});   
        if(response.status === 204){  // Если запись успешно удалена
            location.reload(); // обновляем список после удаления (Аналогично кнопке "Обновить" в браузере)
        }else{
            console.error(`Ошибка удаления сотрудника ${await response.text()}`);
        }
    }
}


// Обработка удаления должности  
async function deletePosition(id) {
  // Перед удалением, для выполнения дальнейших операций (в случае успеха), необходимо сохранить текущее значение select
  const selectElement = document.getElementById('category');
  const currentCategory = selectElement.value; // Получаем текущее значение select

  const apiInfo = 'api/countpos/' + id + '/'  // Формируем запрос для определения количества сотрудников с удаляемой должностью
  const info = await fetch(apiInfo)  // Отправляем запрос
  let count = await info.json();  // Получаем ответ
  
  const value = Object.values(count)[0];  // Извлекаем единственное значение —  объект имеет один ключ

  if(value == 0){ //  Если сотрудников с такой должностью нет, то производим удаление этой должности      
    const confirmed = confirm('Вы уверены, что хотите удалить эту должность?');
    if(confirmed){
        const response = await fetch(`api/position/${id}/`, {method:'DELETE'});  // Отправляем запрос (Удаление записи (DELETE)) 
        if(response.status === 204){   // Если запись успешно удалена
         sessionStorage.setItem('returnCategory', currentCategory);   // сохраняем значение в sessionStorage (для обновления страницы) 
         getPositionList(currentCategory)   // Обновляем данные на странице
        }else{
            console.error(`Ошибка удаления должности ${await response.text()}`);
        }
    }
  }else{  // Если кто-то из сотрудников занимает удаляемую должность. Выводим информационное сообщение
    alert('Вы не можете удалить эту должность, так как есть сотрудники принятые на эту должность. Количество сотрудников с такой должностью = ' + value);
  }  
}

