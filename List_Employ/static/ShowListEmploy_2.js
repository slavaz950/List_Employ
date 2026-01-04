//var targetContent = document.getElementById('result');

//function addListFIO(FIO) {
//	return `<li>Фамилия: ${data.posts.FIO}, Пол: ${data.posts.gender}</li>`;
//}

async function ShowEmployApi() {
	await fetch('api_ListEmp/', {
		method: 'GET',
	}).then(response => response.json().then(
	data => {
		console.log(data);
document.querySelector('result').innerHTML = `<table></table>`
let title = document.createElement(`tr`)
title.innerHTML = `
	<th>ФИО</th>
	<th>Пол</th>
	<th>Возраст</th>
	<th>Должность</th>
	<th>Категория</th>`

document.querySelector('table').append(title)
`${data.gender}`
for(let i=0; i<posts.length; i++) {
	let row = document.createElement(`tr`)
	row.innerHTML = `
	<td>${data.FIO}</td>
	<td>${data.gender}</td>
	<td>${data.posts.age}</td>
	<td>${data.posts.name_position}</td>
	<td>${data.posts.name_category}</td>`

	document.querySelector('table').append(row)
 }

 
}
	
	))

	//)
	}

//document.addEventListener('DOMContentLoaded', (e)   => {
//	ShowEmployApi();
//})