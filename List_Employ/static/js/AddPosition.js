// ДОБАВЛЕНИЕ ДОЛЖНОСТИ

// Обрабатываем нажатие кнопки "Сохранить"
document.getElementById('AddPositionForm').addEventListener('submit', function(event) {
    event.preventDefault(); // Отменяем стандартную отправку формы

    const form = document.querySelector('#AddPositionForm'); // Ищем на целевой странице элемент AddPositionForm
    const formData = new FormData(form); // Создаем экземпляр объекта FormData и передаём ему найденный элемент

    const categoryVal = formData.get('category');       // Получаем текущее значение идентификатора Категории
    const positionVal = formData.get('name_position');  // Получаем текущее значение поля "Должность"
   // const currentCategory = categoryVal; // Получаем значение select для передачи в sessionStorage (для реализации перехода к списку Должностей)


//sessionStorage.setItem('returnCategory', categoryVal); // 
    sessionStorage.setItem('returnCategory', categoryVal); //

    const APIUrl = 'api/positions/' + categoryVal + '/';  // Формируем адрес API-ресурса

    fetch(APIUrl, {                                    // Задаём адрес API-ресурса для отправки запроса 
        method: 'POST'  ,                              // Указываем HTTP-метод
        headers: {'Content-Type': 'application/json',  // Указываем тип передаваемого контента
        },
        body:JSON.stringify(Object.fromEntries(formData)),   // Передаём добавляемые данные
    })
    .then(async response => {
        if (!response.ok) {   // Если HTTP-ответ вернулся с ошибкой. Анализируем его
            switch (response.status) {
                case 409:  // Обрабатываем статусный код 409
                    alert(`ОШИБКА: Должность ${positionVal} - уже существует в базе данных!`);
                    break;
                case 400:  // Обрабатываем статусный код 400
                    alert(`ОШИБКА:  Данные отсутствуют либо они некорректны.`);
                    break;
                default:  // Обрабатываем остальные статусные коды. Получаем статусный код. 
                    alert(`Ошибка ${response.status}`);
            }
      }
      // Если HTTP-ответ вернулся со статусом OK — возвращаем JSON для следующего .then()
      return response.json();
    })
    .then(data => {
      if (data) {
        console.log('Success:', data);        // Отображаем в консоли добавленные в БД данные
        alert('Должность успешно добавлена!'); // Информационное сообщение
        location.href = '/positions/';      // Переходим на страницу со списком сотрудников
          }
        })
     });


