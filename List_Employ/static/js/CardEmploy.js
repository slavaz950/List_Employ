 
// Получаем данные с сервера




// Вариант с извлечением идентификатора из Url-адреса из браузерной строки (Для информации)
const pathParts = window.location.pathname.split('/');
const varzero = pathParts[0];
const category = pathParts[1]; // "products"
const vartwo = pathParts[2];
const Id = pathParts[3];   // 
const varfour = pathParts[4];
const varfive = pathParts[5];
console.log(varzero)
console.log(category)
console.log(vartwo)
console.log(Id)
console.log(varfour)
console.log(varfive)




    
// Вариант с передачей адреса из браузерной строки
const Url =  window.location.href;

//async function getEmployDetail(id) {
async function getEmployDetail(Url) {    
    const response = await fetch(Url, {
        method:"GET",
        headers: {"Accept": "application/json"}
    });
    if (response.ok === true) {
       let  data = await response.json(); // Получаем данные с сервера в формате json
   // }
    
    const post = data.employs;


    console.log(data)  // ДЛЯ ИНФОРМАЦИИ
    console.log(data.employs)  // ДЛЯ ИНФОРМАЦИИ
 
   

 // post.id,post.fio,post.gender_name,post.age,post.positions_name,post.category_name //  Корректные данные


// Вывод данных на страницу
const contentDiv = document.getElementById("result");

const FIODiv = document.getElementById("result-fio");
FIODiv.appendChild(document.createTextNode('Ф.И.О.:       ' + '' + '' + '' + '' + '' + '' + '' + '' + post.FIO)); // post.fio

const genderDiv = document.getElementById("result-gender");
genderDiv.appendChild(document.createTextNode('Пол:       ' + '' + '' + '' + '' + '' + '' + '' + '' + post.gender));  // post.gender_name

const ageDiv = document.getElementById("result-age");
ageDiv.appendChild(document.createTextNode('Возраст:       ' + '' + '' + '' + '' + '' + '' + '' + '' + post.age));  // post.age
  
 
  // Связываем данные с div-контейнером
  contentDiv.appendChild(FIODiv);
  contentDiv.appendChild(genderDiv);
  contentDiv.appendChild(ageDiv);
  

  return  contentDiv;  // Результат
 }
}