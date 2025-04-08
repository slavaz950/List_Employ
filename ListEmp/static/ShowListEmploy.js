//var  result = document.getElementById('result');





//async function addUser() {
////	return `<li>Фамилия: ${data.posts.age}, Пол: ${data.posts.gender}</li>`;
//}
/*
async function ShowEmployApi(){
	const response = await fetch('/api_ListEmp/');
	//var data = JSON.parse(response);
	const data = await response.json();
	console.log(data);
	//return response;
	//console.log(data.gender);
}

*/









async function ShowEmployApi() {
	await fetch('/api_ListEmp/', {
		method: 'GET',
	}).then(response => response.json().then(
	data => {
		 content = data;
		console.log(data);
		//var content = JSON.parse(data);
		//console.log(content);
		//console.log(result);
	
	}))}  // Дежурные скобки (пока отладка перемещаем с места на место)


	
		//var  result = document.getElementById('result');
		`<p> Тестовый объект </p>`
       //console.log(result);

		result.innerText = `${content.posts.gender}`;
        console.log(result);


		result.innerHTML = '';
		data.posts.forEach(user => {
			result.innerHTML += addUser(user);
	});


// }))}  // Дежурные скобки (пока отладка перемещаем с места на место)








document.addEventListener('DOMContentLoaded',(e)  => {
	ShowEmployApi();
})