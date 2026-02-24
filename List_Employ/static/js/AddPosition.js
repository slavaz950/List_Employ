

document.getElementById('AddPositionForm').addEventListener('submit', function(event) {
    event.preventDefault(); // Отменяем стандартную отправку формы

    const form = document.querySelector('#AddPositionForm');
    const formData = new FormData(form); // Создаем экземпляр объекта FormData

console.log(formData)

 

const categoryVal = formData.get('category');     // Получаем текущее значение идентификатора Категории
const positionVal = formData.get('name_position');     // Получаем текущее значение поля "Должность"
const currentCategory = categoryVal; // Получаем значение select для передачи в sessionStorage (для реализации перехода к списку Должностей)

console.log(categoryVal)
console.log(positionVal)
console.log(currentCategory)

//sessionStorage.setItem('returnCategory', categoryVal);

/*
// Проверка содержимого FormData (Для отладки)
  console.log('Содержимое FormData:');
  for (let [key, value] of formData.entries()) {
  console.log(`${key}: ${value}`);
  }
*/
    const APIUrl = 'api/positions/' + categoryVal + '/';
console.log(APIUrl)

    fetch(APIUrl, { // Задаём адрес API-ресурса    /api/positions/4/
        method: 'POST'  ,
        headers: {'Content-Type': 'application/json',
        },
        body:JSON.stringify(Object.fromEntries(formData)),
    })


    .then(async response => {


        
      // Данные для информации
      console.log('Status:', response.status);   ///////////////////
      console.log('OK:', response.ok);        /////////////////

     //   const rawText = await response.text();
//console.log(rawText);

   //   const json = await response.json()
        if (!response.ok) {   // Если HTTP-ответ вернулся с ошибкой
      console.log('Rabotaet not response OK');
      

/*

       // Читаем JSON из тела ответа (асинхронно). Получаем данные для необработанных ошибок  
        const errorData = json;
        console.log('Rabotaet errorData')

        console.log(errorData) /////////////////////////
console.log('Rabotaet errorData')

            console.error('Error data:', errorData); /////////////////
            let message = errorData.detail || errorData.error || 'Неизвестная ошибка'  ;      
           console.log(message)
           console.log(response.status)

*/


            switch (response.status) {
                case 409:  // Обрабатываем статусный код 409
                    alert(`ОШИБКА: Должность ${positionVal} - уже существует в базе данных!`);
                    break;
                case 400:  // Обрабатываем статусный код 400
                    alert(`ОШИБКА:  Данные отсутствуют либо они некорректны.`);
                    break;
                default:  // Обрабатываем остальные статусные коды. Получаем статусный код. Детальную информацию берём из переменной message
                    alert(`Ошибка ${response.status}: ${message}`);
            }
      }
      // Если HTTP-ответ вернулся со статусом OK — возвращаем JSON для следующего .then()
      return response.json();
    })
    .then(data => {
      if (data) {
        console.log('Success:', data);        // Отображаем в консоли добавленные в БД данные
        alert('Должность успешно добавлена!'); // Информационное сообщение

        // После успешного удаления сохраняем значение в sessionStorage
        // sessionStorage.setItem('returnCategory', categoryVal);
        // getPositionList(categoryVal)   // Обновляем данные на странице
         location.href = '/positions/';      // Переходим на страницу со списком сотрудников
          }
        })
     });


