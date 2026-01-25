

const form = document.getElementById('AddEmployForm');  // Находим форму на html странице
const data = new FormData(form);                        // Собираем значения из всех полей ввода
console.log(data)

async function createEmploy(data) {
    const response = await fetch('{% url "api-employ-list" %}', {  // {% url "api-employ-list" %}      {% url "employ-list" %}
    method: 'POST',
    body: JSON.stringify(data), // FormData автоматически задаст заголовок Content-Type
  })
  console.log(response)
  .then(response => response.json())
  .then(result => console.log(result))

  //.catch(error => console.error('Ошибка:', error));
}

































/*

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

            // AJAX-запрос через fetch   
            // Ищем все должности которые относятся к выбранной категории     
            fetch(`/get_positions/${categoryId}/`)       
           
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
                        option.textContent = position.name_position;
                        positionSelect.appendChild(option);
                    });
                })
                .catch(error => {
                    console.error('Ошибка загрузки должностей:', error);
                    positionSelect.innerHTML = '<option value="">Ошибка загрузки</option>';
                });
        }

        */