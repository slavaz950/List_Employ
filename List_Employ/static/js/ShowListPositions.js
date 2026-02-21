
/*

// Обработчик который срабатывает когда страница полностью загружена (DOMContentLoaded)
document.addEventListener('DOMContentLoaded', function() {  
 
 // const categorySelect = document.querySelector('#category');
 // const selectElement = document.getElementById('category');    
 // const messagesContainer = document.getElementById('messagesContainer');
const selectElement = document.querySelector('#category');








})  ///////////////

*/

//console.log(222222)



// getPositionList()
// Функция для загрузки данных
async function getPositionList(id) {    // id

  const selectElement = document.getElementById('category');
  console.log(selectElement)  ///////////////////////
  const categoryId = selectElement.value;
console.log(selectElement.value)
  console.log(categoryId)  /////////////
console.log(id)

let UrlAPI = '' ;  // Очищаем переменную
UrlAPI = 'api/positions/' + id + '/'; // Формируем ссылку для получения данных
console.log(UrlAPI)  /////////////

    response = await fetch(UrlAPI); 
    const data = await response.json();  

  
    let tbody = document.querySelector('#positions-table tbody');
    tbody.innerHTML = '';  // Очищаем элемент tbody
    for(let i = 0; i < data.length; i++) {

      

     // console.log(data[i].id)
     // console.log(data[i].name_position)
      console.log(data[i].category)  // Идентификатор категории
     // console.log(data[i].category_name)


      // Формируем очередную строку таблицы с кнопками для управления текущей записью
        let row = `<tr>  
                    <td>${i+1}</td>                     <!-- Формируем порядковый номер-->
                    <td>${data[i].name_position}</td>  <!-- Значение поля "Должность" -->
                    <td>${data[i].category_name}</td>   <!-- Значение поля "Категория" -->
                    <td>  <!-- ФОРМИРУЕМ БЛОК КНОПОК НЕОБХОДИМЫХ ДЕЙСТВИЙ ДЛЯ ТЕКУЩЕЙ СТРОКИ -->
                        <button onclick="window.location.href='/position/update/${data[i].id}/'" class="btn btn-outline-primary"">Редактировать</button>
                        <button onclick="deletePosition(${data[i].id})" class="btn btn-outline-danger">Удалить</button>
                    </td>
                  </tr>`;    
        tbody.insertAdjacentHTML('beforeend', row);
       
    }

  }
    
