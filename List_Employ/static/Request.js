



function Post_Request(url, data, cb) {  // Передаём url и данные, которые необходимо передать
	const xhr = new XMLHttpRequest();  // Инициализируем новый объект
	xhr.open("POST", url);  // Связываем метод POST и эндпоинт
	
	xhr.addEventListener('load', () => {
		const response = JSON.parse(xhr.responseText);
		cb(response);
	});
	
	xhr.setRequestHeader("Content-Type","application/json;charset=UTF-8");
	
	 // Обрабатываем ошибки
	   xhr.addEventListener('error', () => {
		   consolr.log('error');
	   });
	
	
	 // Передаём тело запроса в формате JSON
	   xhr.send(JSON.stringify(body));
   }   // По сути это конец функции
	



function Get_Request(url, cb) {   // Передаём url
	const xhr = new XMLHttpRequest();  // Инициализируем новый объект
	// console.log(xhr); // Просмотр всех возможных свойств и методов
	Http.open("GET", url);  // Связываем метод GET и эндпоинт
	// на xhr вызываем метод addEventListener и передаём в него load, далее идёт обработчик события
	xhr.addEventListener('load',  () => {
		console.log('request loaded');  // здесь действия обработчика события
	
	const response = JSON.parse(xhr.responseText);
		console.log(response); // Проверка результата обработки JSON
		
	cb(response);  // Вызываем наш callback и передаём ответ от сервера внутри события load 
		// так как данные получаем в json мы этот ответ переводим в обычный массив
	});
	// load - это событие когда мы успешно получили данные от сервера
	
	 xhr.addEventListener('error', () => {
	 console.log('error');   // здесь действия обработчика события
 });
 // Ошибка может быть если у нас что-то не так с адресом 
 
 
 
	
	
	//xhr.responseType = "json"  // Указываем что должно быть преобразовано в объект JavaScript
	xhr.send();    // Отправляем запрос
	
	//  console.log(xhr.responseText)  // просмотра ответа от сервера
	
	
}








/*

function Post_Request(url, data) {  // Передаём url и данные, которые необходимо передать
	const Http = new XMLHttpRequest();  // Инициализируем новый объект
	Http.open("POST", url);  // Связываем метод POS и эндпоинт
	Http.setRequestHeader("Content-Type","application/json");
	Http.send(JSON.stringify(data));  // Преобразуем JS объект в JSON и отправляем на сервер
	var result = Http.upload.onload = function (e) { // Делаем проверку (Отправлены ли данные)
		console.log("Данные загружены успешно.");
	} 
	return result;
}



function Get_Request(url) {   // Передаём url
	const Http = new XMLHttpRequest();  // Инициализируем новый объект
	Http.open("GET", url);  // Связываем метод GET и эндпоинт
	Http.responseType = "json"  // Указываем что должно быть преобразовано в объект JavaScript
	Http.send();    // Отправляем запрос
	
	Http.onload = function() {
		var json = Http.response;  // Сохраняем ответ на наш запрос
	}
	return json;
}

*/
