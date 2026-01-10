

const form = document.getElementById('AddEmployForm');  // Находим форму на html странице
const data = new FormData(form);                        // Собираем значения из всех полей ввода


async function createEmploy(data) {
    const response = await fetch('{% url "employ-list" %}', {
    method: 'POST',
    body: JSON.stringify(data), // FormData автоматически задаст заголовок Content-Type
  })
  .then(response => response.json())
  .then(result => console.log(result))
  //.catch(error => console.error('Ошибка:', error));
}