

document.getElementById('AddEmployForm').addEventListener('submit', function(event) {
    event.preventDefault(); // Отменяем стандартную отправку формы

    const form = document.querySelector('#AddEmployForm');
    const formData = new FormData(form); // Создаем экземпляр объекта FormData

console.log(formData)

// Проверка содержимого FormData (Для отладки)
  console.log('Содержимое FormData:');
  for (let [key, value] of formData.entries()) {
  console.log(`${key}: ${value}`);
  }
    fetch('api/employees/', { // Задаём адрес API-ресурса
        method: 'POST',
        headers: {'Content-Type': 'application/json',
        },
        body:JSON.stringify(Object.fromEntries(formData)),
    })
    .then(response => response.json())
    .then(location.href = '/employlist/')  // В случае успешного создания сотрудника, переходим к списку сотрудников
   }
)
 
;

