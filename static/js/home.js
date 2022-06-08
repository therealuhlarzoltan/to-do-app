function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}


function getUserId() {
    const id = JSON.parse(document.getElementById('user-id').textContent)
    return id
}


function formatTask(element) {
   var li = document.createElement('li')
   li.dataset.name = `${element['task']}`
   li.dataset.created = `${element['created']}`
   if (element['priority']) {
        li.dataset.priority = `${element['priority']}`
   }
   else {
        li.dataset.priority = '0'
   }
   if (element['due']) {
        li.dataset.due = `${element['due']}`
   } else {
       li.dataset.due = '0'
   }
   
   var str = `<div class="ms-2 me-auto"><div><span><i class="fa-regular fa-circle" data-id='${element['id']}'data-completed='${element['completed']}'></i></span><a class='mx-2' href="/edit-task/${element['id']}" style="text-decoration:none;color:black;">${element['task']}</a></div>`
   if (element['list']) {
    str +=  `<small><a href="/list/${element['list']['id']}" style="text-decoration:none;color:black;">${element['list']['list']}</a></small></div>`
   } 
   else {
       str += '</div>'
   }
   li.classList.add("list-group-item")
   li.classList.add('d-flex')
   li.classList.add('justifiy-content-between')
   li.classList.add('align-items-start')
   li.setAttribute('id', element['id'])
   if (element['priority'] === 1) {
       str += '<span><i class="fa-solid fa-exclamation"></i></span>'
   }
   else if (element['priority'] === 2) {
       str  += '<span><i class="fa-solid fa-exclamation"></i><i class="fa-solid fa-exclamation"></i></span>'
   }
   else if (element['priority'] === 3) {
       str += '<span><i class="fa-solid fa-exclamation"></i><i class="fa-solid fa-exclamation"></i><i class="fa-solid fa-exclamation"></i></span>'
   }
   li.innerHTML = str
   return li
    
}

function displayTasks(response) {
    parent = document.getElementById('todo-list')
    var i;
    for (i=0; i<response.length; i++) {
        var task_obj = response[i]
        current = formatTask(task_obj)
        parent.appendChild(current)
    }
}


function loadTasks() {
    const xhr = new XMLHttpRequest()
    const responseType = 'json'
    const user = getUserId()
    const url = `/api/user/${user}/`
    const method = 'GET'
    xhr.responseType = responseType
    xhr.open(method, url)
    xhr.setRequestHeader("HTTP_X_REQUESTED_WITH", "XMLHttpRequest")
    xhr.setRequestHeader("X-Requested-With", "XMLHttpRequest")
    xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'))
    xhr.onload = function() {
        const serverResponse = xhr.response
        displayTasks(serverResponse)
    }
    xhr.send()


}


function completeTask(element) {
    id = element.dataset.id
    completed = element.dataset.completed
    const xhr = new XMLHttpRequest()
    const responseType = 'json'
    const url = `/api/complete-task/${id}`
    const method = 'POST'
    xhr.open(method, url)
    xhr.setRequestHeader("HTTP_X_REQUESTED_WITH", "XMLHttpRequest")
    xhr.setRequestHeader("X-Requested-With", "XMLHttpRequest")
    xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'))
    xhr.onload = function() {
        const serverResponse = xhr.response
        const responseArray = serverResponse.split(":")
        const response = responseArray[1].slice(0, -1)
        
        if (response == 'true') {
        element.classList.remove('fa-regular')
        element.classList.add('fa-solid')
        element.dataset.completed = response
        }
        else if (response == 'false') {
            element.classList.remove('fa-solid')
            element.classList.add('fa-regular')
            element.dataset.completed = response  
        }
        const timeout = 2500
        setTimeout(() => {
            if (element.dataset.completed == 'true') {
            li = document.getElementById(element.dataset.id)
            li.remove()}
        }, timeout); 
    }
    xhr.send()

    
    

}


const objectComparisonByPriorityCallback = (arrayItemA, arrayItemB) => {
  if (arrayItemA.dataset.priority < arrayItemB.dataset.priority) {
    return 1
  }

  if (arrayItemA.dataset.priority > arrayItemB.dataset.priority) {
    return -1
  }

  return 0
}


const objectComparisonByNameCallback = (arrayItemA, arrayItemB) => {
  if (arrayItemA.dataset.name.toLowerCase() < arrayItemB.dataset.name.toLowerCase()) {
    return -1
  }

  if (arrayItemA.dataset.name.toLowerCase() > arrayItemB.dataset.name.toLowerCase()) {
    return 1
  }

  return 0
}


const objectComparisonByCreationDateCallback = (arrayItemA, arrayItemB) => {
    const d1 = new Date(arrayItemA.dataset.created)
    const d2 = new Date(arrayItemB.dataset.created)
    if (d1 < d2) {
        return -1
    }

    if (d1 > d2) {
        return 1
    }

    return 0
}


const objectComparisonByDueDateCallback = (arrayItemA, arrayItemB) => {

    if (arrayItemA.dataset.due === '0' && arrayItemB.dataset.due != '0') {
        return 1
    }
    if (arrayItemA.dataset.due != '0' && arrayItemB.dataset.due === '0') {
        return -1
    }
    if (arrayItemA.dataset.due === '0' && arrayItemB.dataset.due === '0') {
        return 0
    }
    const d1 = new Date(arrayItemA.dataset.due)
    const d2 = new Date(arrayItemB.dataset.due)
    if (d1 < d2) {
        return -1
    }

    if (d1 > d2) {
        return 1
    }

    return 0
}


function handleSortButtonClicked(event) {
    event.preventDefault()
    const sortMethod = event.target.innerHTML.toLowerCase()
    if (sortMethod === 'created') {
        sortByCreated()
    }
    else if (sortMethod === 'name') {
        sortByName()
    }
    else if (sortMethod === 'due to') {
        sortByDue()
    }
    else if (sortMethod === 'priority') {
        sortByPriority()
    }

}


function sortByCreated() {
    const lis = [...document.getElementById('todo-list').getElementsByTagName('li')]
    lis.sort(objectComparisonByCreationDateCallback)
    list = document.getElementById('todo-list')
    list.innerHTML = ''
    lis.forEach(li => {
        list.appendChild(li)
    })

}


function  sortByName() {
    const lis = [...document.getElementById('todo-list').getElementsByTagName('li')]
    lis.sort(objectComparisonByNameCallback)
    list = document.getElementById('todo-list')
    list.innerHTML = ''
    lis.forEach(li => {
        list.appendChild(li)
    })
}


function sortByDue() {
    const lis = [...document.getElementById('todo-list').getElementsByTagName('li')]
    lis.sort(objectComparisonByDueDateCallback)
    list = document.getElementById('todo-list')
    list.innerHTML = ''
    lis.forEach(li => {
        list.appendChild(li)
    })
}


function sortByPriority() {
    const lis = [...document.getElementById('todo-list').getElementsByTagName('li')]
    lis.sort(objectComparisonByPriorityCallback)
    list = document.getElementById('todo-list')
    list.innerHTML = ''
    lis.forEach(li => {
        list.appendChild(li)
    })
}


function formatDate(date) {
    if (date) {
        var d = new Date(date),
            month = '' + (d.getMonth() + 1),
            day = '' + d.getDate(),
            year = d.getFullYear();

        if (month.length < 2) 
            month = '0' + month;
        if (day.length < 2) 
            day = '0' + day;

        return [year, month, day].join('-');
    }
    else {
        var d = new Date(),
            month = '' + (d.getMonth() + 1),
            day = '' + d.getDate(),
            year = d.getFullYear();

        if (month.length < 2) 
            month = '0' + month;
        if (day.length < 2) 
            day = '0' + day;

        return [year, month, day].join('-');
    }
}


function checkExpiredDueDate(element) {
    var dateToCheck = element.dataset.due
    if (dateToCheck != '0') {
        dateToCheck = formatDate(dateToCheck)
        const today = formatDate()
        if (dateToCheck < today) {
            element.childNodes[0].childNodes[0].childNodes[1].style.color = 'red'
        }
    }
}


function markExpiredTasks() {
    const lis = [...document.getElementById('todo-list').getElementsByTagName('li')]
    lis.forEach(li => {
        checkExpiredDueDate(li)
    })
}



    document.addEventListener('DOMContentLoaded', function() {
        loadTasks()
        const checkCircles = document.getElementsByClassName('fa-circle')
        const timeout = 200
        setTimeout(() => {
            Array.prototype.forEach.call(checkCircles, function(element) {
                element.addEventListener('click', function() {
                    completeTask(element)
                })
            })
        }, timeout);
        const newReminderButton = document.getElementById('new-reminder-button')
        newReminderButton.addEventListener('click', function() {
            window.location.href = '/new-task'
        })
        const sortButtons = document.querySelectorAll('.dropdown-item')
        sortButtons.forEach(button => {
            button.addEventListener('click', handleSortButtonClicked)
        })
        setTimeout(() => {
            markExpiredTasks()
        }, timeout);
    })