 
// Получаем данные с сервера




// Вариант с извлечением идентификатора из Url-адреса из браузерной строки (Для информации)
// Разбивает Url-адрес по частям
const pathParts = window.location.pathname.split('/');  // В скобках указываем разделитель (что считать окончанием каждой из частей)

const Id = pathParts[3];   // Идентификатор

console.log(Id)
//console.log(varfour)
//console.log(varfive)

//console.log(pathParts)


 //  /api/employee/4/   


// Вариант с передачей адреса из браузерной строки


const UrlTEST =  window.location.href;

    //  ' + '' + '' + '' + '' + '' + '' + '' + '' + post.gender

//const Url =  'api/employee/' + Id + '/';

const Url = 'http://127.0.0.1:8000/api/employee/' + Id + '/';


console.log(UrlTEST)
console.log(Url)



getEmployDetail()
///async function getEmployDetail(id) {
async function getEmployDetail() {    
     response = await fetch(Url, {method:"GET"})
     let  data = await response.json(); // Получаем данные с сервера в формате json
     const employ = data;

//for(let i = 0; i < posts.length; i++){// Извлекаем из массива все объекты (т.е. целевые данные)
  // const post = posts [i];  // Определяем текуший объект, извлечённый из массива
  // var row = createRow(post.id,post.fio,post.gender_name,post.age,post.positions_name,post.category_name) 



    console.log(data)  // ДЛЯ ИНФОРМАЦИИ
   // console.log(data.employs)  // ДЛЯ ИНФОРМАЦИИ
 
  // console.log(posts.FIO)
console.log(employ.fio)
console.log(employ.gender_name)
console.log(employ.age)

console.log()
console.log()

console.log(data.fio)
console.log(data.gender_name)
console.log(data.age)

// Обновляем значение заголовка страницы
document.title = 'Личная карточка   -   ' + data.fio;


// Вывод данных на страницу
const contentDiv = document.getElementById("result");

const FIODiv = document.getElementById("result-fio");
FIODiv.appendChild(document.createTextNode('Ф.И.О.:       ' + '' + '' + '' + '' + '' + '' + '' + '' + data.fio)); 

const genderDiv = document.getElementById("result-gender");
genderDiv.appendChild(document.createTextNode('Пол:       ' + '' + '' + '' + '' + '' + '' + '' + '' + data.gender_name)); 

const ageDiv = document.getElementById("result-age");
ageDiv.appendChild(document.createTextNode('Возраст:       ' + '' + '' + '' + '' + '' + '' + '' + '' + data.age));  
  
  // Связываем данные с div-контейнером
  contentDiv.appendChild(FIODiv);
  contentDiv.appendChild(genderDiv);
  contentDiv.appendChild(ageDiv);
  

  return  contentDiv;  // Результат
 }
//}