

const form = document.getElementById('AddEmployForm');  // Находим форму на html странице
const data = new FormData(form);                        // Собираем значения из всех полей ввода


async function createEmploy(data) {
    const response = await fetch('{% url "employ-list" %}', {  // {% url "api-employ-list" %}
    method: 'POST',
    body: JSON.stringify(data), // FormData автоматически задаст заголовок Content-Type
  })
  .then(response => response.json())
  .then(result => console.log(result))
  //.catch(error => console.error('Ошибка:', error));
}





// Функция динамической загрузки значений полей

function loadPositions() {
            const categoryId = document.getElementById('CategorySelect').value;
            const positionSelect = document.getElementById('PositionSelect');


            console.log(categoryId)
console.log(positionSelect)

console.log(categoryId)

            // Очищаем второй select
            positionSelect.innerHTML = '<option value="">Выберите должность</option>';
          
            // Проверяем существует ли такая категория в базе данных
            if (!categoryId) { // Если категория не существует выходим из функции
                return;
            }

            // AJAX-запрос через fetch   `api/positions/?category_id=${categoryId}`
            // Ищем все должности которые относятся к выбранной категории      `api/positions/?category_id=${categoryId}`
            fetch(`get_positions/?category_id=${categoryId}`)       //  http://127.0.0.1:8000/api/positions/         api/positions/${categoryId}/
           // fetch(`/employ/new/api/positions/?category_id=${categoryId}`)
           // fetch(`http://127.0.0.1:8000/api/positions/${categoryId}/`)
                .then(response => {
                    if (!response.ok) {
                        throw new Error('Ошибка сервера');
                    }
                    return response.json();
                })
                .then(data => {
                    if (data.length === 0) {  // Защита от пустых ответов (проверяем длинну data)
                        const option = document.createElement('option');
                        option.value = '';
                        option.textContent = 'Нет должностей';
                        positionSelect.appendChild(option);
                        return;
                    }

                    data.forEach(position => {  // Формируем список должностей
                        const option = document.createElement('option');
                        option.value = position.id;
                        option.textContent = position.name;
                        positionSelect.appendChild(option);
                    });
                })
                .catch(error => {
                    console.error('Ошибка загрузки должностей:', error);
                    positionSelect.innerHTML = '<option value="">Ошибка загрузки</option>';
                });
        }