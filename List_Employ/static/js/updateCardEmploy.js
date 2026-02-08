 
 
//getEmployForUpdate()
// ФУНКЦИЯ ДЛЯ ПОЛУЧЕНИЯ ДАННЫХ ДЛЯ "ИЗМЕНЕНИЯ КАРТОЧКИ СОТРУДНИКА" 



editEmploy()

async function editEmploy() {
  const form = document.getElementById('UpdateEmployForm');  // Находим форму на html странице
  const formData = new FormData(form);                        // Собираем значения из всех полей ввода
  console.log(formData)

  const pathParts = window.location.pathname.split('/');  // В скобках указываем разделитель (что считать окончанием каждой из частей)
  const Id = pathParts[3];   // Получаем идентификатор записи
  const Url = 'api/employee/Id/'
  response = await fetch(Url, {
    method:"PUT",
    //headers: {'Content-Type': 'application/json'},
    body:JSON.stringify(formData)   // FormData автоматически устанавливает Content-Type
  });  // Запрашиваем данные на сервере

if(response.status === 200) {   // Если обновление данных сотрудника прошло успешно   
  location.href = '/employlist/';  //"window.location.href='/employlist/'"
}else{  
   }
  
 };