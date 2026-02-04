// Загрузка данных из backend
document.addEventListener('DOMContentLoaded', function() {
    loadPositions();
    loadEmployees();
});


//--------------------------------------------------------------------------------------
// Функция загрузки списка должностей
async function loadPositions() {
    const response = await fetch('/api/positions/');
    if (!response.ok) throw new Error("Ошибка загрузки данных");
    const data = await response.json();
    
    // Отрисовка таблицы должностей
    let tbody = document.querySelector('#positions-table tbody');
    tbody.innerHTML = '';
    for(let i = 0; i < data.length; i++) {
        let row = `<tr>
                    <td>${i+1}</td>
                    <td>${data[i].name}</td>
                    <td>${data[i].category}</td>
                    <td>
                        <button onclick="editPosition(${data[i].id})" class="btn btn-warning">Редактировать</button>
                        <button onclick="deletePosition(${data[i].id})" class="btn btn-danger">Удалить</button>
                    </td>
                  </tr>`;
        tbody.insertAdjacentHTML('beforeend', row);
    }
}


//-----------------------------------------------------------------------------------
// Функция загрузки списка сотрудников
async function loadEmployees() {
    const response = await fetch('/api/employees/');
    if (!response.ok) throw new Error("Ошибка загрузки данных");
    const data = await response.json();
    
    // Отрисовка таблицы сотрудников     employees-table
    let tbody = document.querySelector('#employees-table tbody');
    tbody.innerHTML = '';
    for(let i = 0; i < data.length; i++) {
        let row = `<tr>
                    <td>${i+1}</td>
                    <td>${data[i].fio}</td>
                    <td>${data[i].gender_name}</td>
                    <td>${data[i].age}</td>
                    <td>${data[i].positions_name}</td>
                    <td>${data[i].category_name}</td>
                    <td>
                        <button onclick="editEmployee(${data[i].id})" class="btn btn-warning">Редактировать</button>
                        <button onclick="deleteEmployee(${data[i].id})" class="btn btn-danger">Удалить</button>
                    </td>
                  </tr>`;
        tbody.insertAdjacentHTML('beforeend', row);
    }
}


/*

//-------------------------------------------------------------------------------------
// Загрузка данных из backend
document.addEventListener('DOMContentLoaded', function() {
    loadPositions();
    loadEmployees();
});

// Функция загрузки списка должностей
async function loadPositions() {
    const response = await fetch('/api/positions/');
    if (!response.ok) throw new Error("Ошибка загрузки данных");
    const data = await response.json();
    console.log(data)
    console.log(data[i].name)

    // Отрисовка таблицы должностей
    let tbody = document.querySelector('#positions-table tbody');
    tbody.innerHTML = '';
    for(let i = 0; i < data.length; i++) {
        let row = `<tr>
                    <td>${i+1}</td>
                    <td>${data[i].name}</td>
                    <td>${data[i].category}</td>
                    <td>
                        <button onclick="editPosition(${data[i].id})" class="btn btn-warning">Редактировать</button>
                        <button onclick="deletePosition(${data[i].id})" class="btn btn-danger">Удалить</button>
                    </td>
                  </tr>`;
        tbody.insertAdjacentHTML('beforeend', row);
    }
}

// Функция загрузки списка сотрудников
async function loadEmployees() {
    const response = await fetch('/api/employees/');
    if (!response.ok) throw new Error("Ошибка загрузки данных");
    const data = await response.json();
    
    // Отрисовка таблицы сотрудников  (ТАБЛИЧКУ ПОПРАВИЛ НО НУЖНО ПРОВЕРЯТЬ)
    let tbody = document.querySelector('#employees-table tbody');
    tbody.innerHTML = '';
    for(let i = 0; i < data.length; i++) {
        let row = `<tr>      
                    <td>${i+1}</td>
                    <td>${data[i].fio}</td>
                    <td>${data[i].gender_name}</td>
                    <td>${data[i].age}</td>
                    <td>${data[i].positions_name}</td>
                    <td>${data[i].category_name}</td>
                    <td>
                        <button onclick="editEmployee(${data[i].id})" class="btn btn-warning">Редактировать</button>
                        <button onclick="deleteEmployee(${data[i].id})" class="btn btn-danger">Удалить</button>
                    </td>
                  </tr>`;
        tbody.insertAdjacentHTML('beforeend', row);
    }
}

*/


// Добавляем новую должность
document.getElementById('add-position-form').onsubmit = async event => {
    event.preventDefault(); // предотвращаем отправку формы стандартным способом
    let positionName = document.getElementById('position-name').value.trim();
    let category = document.getElementById('position-category').value.trim();
    if(!positionName || !category){
        alert('Заполните все поля!');
        return false;
    }
    try{
        const response = await fetch('/api/add_position/', {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({name: positionName, category})
        });
        
        if(response.status === 201){ // статус успешного создания объекта
            location.reload(); // перезагружаем страницу
        } else {
            console.error(await response.text());
        }
    } catch(err){
        console.error(err.message);
    }
};

// Обработчик удаления должности
async function deletePosition(id) {
    const confirmed = confirm('Вы уверены, что хотите удалить данную должность?');
    if(confirmed){
        const response = await fetch(`/api/delete_position/${id}/`, {method:'DELETE'});
        if(response.status === 204){
            location.reload(); // обновляем список после удаления
        }else{
            console.error(`Ошибка удаления должности ${await response.text()}`);
        }
    }
}

// Редактирование должности
async function editPosition(id) {
    const positionData = prompt('Введите новое название:', '');
    if(positionData !== null){
        const response = await fetch(`/api/edit_position/${id}/`, {
            method:'PUT',
            headers:{'Content-Type':'application/json'},
            body:JSON.stringify({name:positionData})
        });
        if(response.status === 200){
            location.reload(); // обновление страницы
        }else{
            console.error(`Ошибка обновления должности ${await response.text()}`);
        }
    }
}

// Аналогично для функций сотрудников addEmployee(), deleteEmployee(), editEmployee()

// Функциональность добавления новых сотрудников аналогична вышеописанной



// Аналогично для функций сотрудников addEmployee(), deleteEmployee(), editEmployee()

// Функциональность добавления новых сотрудников аналогична вышеописанной






//===========================================================

// Добавляем новую должность
document.getElementById('add-position-form').onsubmit = async event => {
    event.preventDefault(); // предотвращаем отправку формы стандартным способом
    let positionName = document.getElementById('position-name').value.trim();
    let category = document.getElementById('position-category').value.trim();
    if(!positionName || !category){
        alert('Заполните все поля!');
        return false;
    }
    try{
        const response = await fetch('/api/add_position/', {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({name: positionName, category})
        });
        
        if(response.status === 201){ // статус успешного создания объекта
            location.reload(); // перезагружаем страницу (Аналогично кнопке "Обновить" в браузере)
        } else {
            console.error(await response.text());
        }
    } catch(err){
        console.error(err.message);
    }
};

// Обработчик удаления должности  (ПЕРЕРАБОТАТЬ )
async function deleteEmployee(id) {
    const confirmed = confirm('Вы уверены, что хотите удалить данную должность?');
    if(confirmed){
        const response = await fetch(`/api/delete_position/${id}/`, {method:'DELETE'});
        if(response.status === 204){
            location.reload(); // обновляем список после удаления (Аналогично кнопке "Обновить" в браузере)
        }else{
            console.error(`Ошибка удаления должности ${await response.text()}`);
        }
    }
}

// Редактирование должности  (ПЕРЕРАБОТАТЬ) +++++++++++++++++++++++++++
async function editEmployee(id) {
    const positionData = prompt('Введите новое название:', '');
    if(positionData !== null){
        const response = await fetch(`/api/edit_position/${id}/`, {
            method:'PUT',
            headers:{'Content-Type':'application/json'},
            body:JSON.stringify({name:positionData})
        });
        if(response.status === 200){
            location.reload(); // обновление страницы (Аналогично кнопке "Обновить" в браузере)
            location.href = 'pages/contact.html'; // Переход на целевую страницу
            location.assign('/products/item.html'); // Переход на целевую страницу (и добавление в историю браузера(пользователь сможет вернуться нажав "Назад")) 
            location.replace('путь_к_странице.html'); // Переходит на новую страницу, но не добавляет её в историю браузера. Пользователь не сможет вернуться назад через кнопку «Назад».
        

        }else{
            console.error(`Ошибка обновления должности ${await response.text()}`);
        }
    }
}