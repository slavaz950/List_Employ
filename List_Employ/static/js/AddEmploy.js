

document.getElementById('AddEmployForm').addEventListener('submit', function(event) {
    event.preventDefault(); // Отменяем стандартную отправку формы

    const form = document.querySelector('#AddEmployForm');
    const formData = new FormData(form); // Создаем экземпляр объекта FormData

console.log(formData)
const fio = formData.get('fio'); // 
const age = formData.get('age');     // 



// Проверка содержимого FormData (Для отладки)
  console.log('Содержимое FormData:');
  for (let [key, value] of formData.entries()) {
  console.log(`${key}: ${value}`);
const value0 = value[0]


  }



 // try{         



    fetch('api/employees/', { // Задаём адрес API-ресурса
        method: 'POST',
        headers: {'Content-Type': 'application/json',
        },
        body:JSON.stringify(Object.fromEntries(formData)),
    })

    .then(async response => {

      // Данные для информации
      console.log('Status:', response.status);   ///////////////////
      console.log('OK:', response.ok);        /////////////////




        if (!response.ok) {
      
       // Читаем JSON из тела ответа (асинхронно). Получаем данные для необработанных ошибок  
       // const errorData = await response.json();
         //   console.error('Error data:', errorData); /////////////////
          //  let message = errorData.detail || errorData.error || 'Неизвестная ошибка'  ;      
           
            switch (response.status) {
                case 409:
                    alert(`ОШИБКА: Сотрудник ${fio} возраст которого ${age} года(лет) - уже существует!`);
                    break;
                case 400:
                    alert(`ОШИБКА:  Данные отсутствуют либо они некорректны.`);
                    break;
                default:
                    alert(`Ошибка ${response.status}: ${message}`);
            }
            // Бросаем ошибку, чтобы перейти в .catch()
           // throw new Error(`${response.status}: ${message}`);
      }
      // Если OK — возвращаем JSON для следующего .then()
      return response.json();
    })
    .then(data => {
      if (data) {
        console.log('Success:', data);
        alert('Сотрудник успешно добавлен!');
         location.href = '/employlist/'; // Переходим на страницу со списком сотрудников
      }
    })
//} catch (error) {
 //console.error('Unexpected error in fetch:', error);
 // alert('Произошла непредвиденная ошибка при отправке данных.');
}

   // }
  );