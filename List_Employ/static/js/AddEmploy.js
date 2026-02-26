// ДОБАВЛЕНИЕ НОВОГО СОТРУДНИКА

// Обрабатываем нажатие кнопки "Сохранить"
document.getElementById('AddEmployForm').addEventListener('submit', function(event) {
    event.preventDefault(); // Отменяем стандартную отправку формы

    const form = document.querySelector('#AddEmployForm');
    const formData = new FormData(form); // Создаем экземпляр объекта FormData

    // Получаем значения полей для вывода информационных сообщений
    // (В случае попытки повторного ввода одного и того же сотрудника)
    const fio = formData.get('fio'); // Получаем значение поля "Ф.И.О" 
    const age = formData.get('age'); // Получаем значение поля "Возраст" 

  /*  
  // Проверка содержимого FormData (Для отладки)
  console.log('Содержимое FormData:');
  for (let [key, value] of formData.entries()) {
  console.log(`${key}: ${value}`);
  } */

    fetch('api/employees/', { // Задаём адрес API-ресурса
        method: 'POST',
        headers: {'Content-Type': 'application/json',
        },
        body:JSON.stringify(Object.fromEntries(formData)),
    })
    .then(async response => {
        if (!response.ok) {  // Если в ответе вернулась ошибка. Анализируем её
            switch (response.status) {
                case 409:  // Если статусный код ошибки 409. Выводим информационное сообщение
                    alert(`ОШИБКА: Сотрудник ${fio} возраст которого ${age} года(лет) - уже существует!`);
                    break;  // Выход из switch. Чтобы не выполнялось следующее действие
                case 400:   // Если статусный код ошибки 400. Выводим информационное сообщение
                    alert(`ОШИБКА:  Данные отсутствуют либо они некорректны.`);
                    break;
                default:  // Если ошибки нет в числе обработанных выводим пользователю информацию об этой ошибке
                    alert(`Ошибка ${response.status}`);
            }   
      }
      // Если ответ вернулся со статусом OK — возвращаем JSON для следующего .then()
      return response.json();
    })
    .then(data => {
      if (data) {
        console.log('Success:', data);  // Выводим в консоль данные которые были добавлены в базу данных
        alert('Сотрудник успешно добавлен!');  // Пользователь получает информацию о том что операция завершена успешно
        location.href = '/employlist/'; // Переходим на страницу со списком сотрудников
      }
    })
}
  );