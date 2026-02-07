 

getEmployDetail()
// ФУНУЦИЯ ДЛЯ ПОЛУЧЕНИЯ ДАННЫХ ДЛЯ "КАРТОЧКИ СОТРУДНИКА" 
async function getEmployDetail() {  
  const pathParts = window.location.pathname.split('/');  // В скобках указываем разделитель (что считать окончанием каждой из частей)
  const Id = pathParts[3];   // Получаем идентификатор записи
  const UrlAPI = 'http://127.0.0.1:8000/api/employee/' + Id + '/'; // Формируем ссылку для получения данных

  response = await fetch(UrlAPI, {method:"GET"})  // Запрашиваем данные на сервере
  let  data = await response.json(); // Получаем данные с сервера в формате json
   
// Обновляем значение заголовка страницы
  document.title = data.fio + ' - ' + 'Личная карточка' ;

 let tbody = document.querySelector('#employees-card-table tbody');
    tbody.innerHTML = '';  // Очищаем элемент tbody
  //  for(let i = 0; i < data.length; i++) {


      // Формируем очередную строку таблицы с кнопками для управления текущей записью
        let content = `<tr>  
                    
                    <td><b>Ф.И.О</b></td><td>${data.fio}</td>             <!-- Значение поля "Ф.И.О" -->
                    </tr>  <!-- Переходим на следующуюстроку -->
                    <td><b>Пол</b></td>      <td>${data.gender_name}</td>     <!-- Значение поля "Пол" -->
                    </tr>  <!-- Переходим на следующуюстроку -->
                    <td><b>Возраст</b></td><td>${data.age}</td>             <!-- Значение поля "Возраст" -->
                    </tr>  <!-- Переходим на следующуюстроку -->

                    <br><br> <!-- Делаем отступ -->

                    <td>  <!-- ФОРМИРУЕМ БЛОК КНОПОК НЕОБХОДИМЫХ ДЕЙСТВИЙ ДЛЯ ТЕКУЩЕЙ СТРОКИ -->
                       
                        <button onclick="window.location.href='/employ/update/${data.id}/'" class="btn btn-warning">Изменить карточку сотрудника</button>
                        <button onclick="window.location.href='/employlist/'" class="btn btn-warning">Вернуться к списку сотрудников</button>
                     
                    </td>
                  </tr>`;    
        tbody.insertAdjacentHTML('beforeend', content);

return  tbody;  // Результат
 }




/*


 /* 
//  Формируем ссылку для кнопки "Изменить карточку сотрудника"
  const Url = 'http://127.0.0.1:8000/employ/update/' + Id + '/'; // Формируем ссылку для получения данных
 // const Url = {% url 'employ-update'  id   %}; // Формируем ссылку для получения данных

  const form = document.getElementById('"changeCard"')
  form.action = Url;  // Меняем action
  console.log('Новый action:', form.action);   // Можно проверить результат

/*

// Вывод данных на страницу    card-employee
//const contentDiv = document.getElementById("result");
const contentDiv = document.getElementById("card-employee");

//const IdDiv = document.getElementById("result-id");
//IdDiv.appendChild(document.createTextNode('Ф.И.О.:       ' + '' + '' + '' + '' + '' + '' + '' + '' + data.id)); 

const FIODiv = document.getElementById("result-fio");
FIODiv.appendChild(document.createTextNode('Ф.И.О.:       ' + '' + '' + '' + '' + '' + '' + '' + '' + data.fio)); 

const genderDiv = document.getElementById("result-gender");
genderDiv.appendChild(document.createTextNode('Пол:       ' + '' + '' + '' + '' + '' + '' + '' + '' + data.gender_name)); 

const ageDiv = document.getElementById("result-age");
ageDiv.appendChild(document.createTextNode('Возраст:     ' + data.age));  
  
  // Связываем данные с div-контейнером
  //contentDiv.appendChild(IdDiv);
  contentDiv.appendChild(FIODiv);
  contentDiv.appendChild(genderDiv);
  contentDiv.appendChild(ageDiv);

  



const ButtonBlock = document.getElementById("button-block");

 


const butChangeCard = "<button onclick='window.location.href= '/employ/update/${data[i].id}/' class='btn btn-warning'>Изменить карточку сотрудника</button>";

const butBackListEmployees = "<button onclick='window.location.href= '/employlist/' class='btn btn-warning'>Изменить карточку сотрудника</button>";



ButtonBlock.insertAdjacentHTML('afterend', butChangeCard);
ButtonBlock.insertAdjacentHTML('afterend', butBackListEmployees);

*/
 //ButtonBlock.appendChild(butChangeCard);
 // ButtonBlock.appendChild(butBackListEmployees);

 //<button onclick="window.location.href= '/employ/update/${data[i].id}/'" class="btn btn-warning">Изменить карточку сотрудника</button>
  //        <button onclick="window.location.href='/employlist/'" class="btn btn-warning">Вернуться к списку сотрудников</button>

  

//  return  contentDiv;  // Результат
// }
//}


