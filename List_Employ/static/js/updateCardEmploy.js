 
 
//getEmployForUpdate()
// ФУНКЦИЯ ДЛЯ ПОЛУЧЕНИЯ ДАННЫХ ДЛЯ "ИЗМЕНЕНИЯ КАРТОЧКИ СОТРУДНИКА" 



//document.getElementById("formUpdateEmploy").addEventListener('onclick', function(e) {
   // e.preventDefault();

async function editEmploy() {
  
 // }) 

  const pathParts = window.location.pathname.split('/');  // В скобках указываем разделитель (что считать окончанием каждой из частей)
  const id = pathParts[3];   // Получаем идентификатор записи
  //const Url =
  const APIUrl = 'api/employee/' + id + '/';



const form = document.getElementById("formUpdateEmploy");  // Находим форму на html странице
  console.log(form)
  const formData = new FormData(form);                        // Собираем значения из всех полей ввода


// Проверка содержимого FormData (Для отладки)
console.log('Содержимое FormData:');
for (let [key, value] of formData.entries()) {
  console.log(`${key}: ${value}`);
}


  console.log(formData)
console.log(APIUrl)


////try{
 const response = await fetch(APIUrl, {  //await
    method:"PUT",
    headers: {'Content-Type': 'application/json'  // БЕЗ ЭТОЙ СТРОКИ ОШИБКУ ВЫДАЁТ. Возможно потому что FormData работает не как нужно.
    },  
  // body:JSON.stringify(formData)   // FormData автоматически устанавливает Content-Type
   body:JSON.stringify(Object.fromEntries(formData))
 }) ;

 if (response.ok) {
 // alert('Данные обновлены');
  location.href = '/employlist/';
 //} else {
 // throw new Error('Ошибка сервера: ${response.statusText}');
  }





/*

if(response.status === 200) {   // Если обновление данных сотрудника прошло успешно   
  location.href = '/employlist/';  //"window.location.href='/employlist/'"
}else{  
   }
  
*/


};