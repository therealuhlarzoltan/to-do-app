function handleEditFormDidSubmit(event) {
   // event.preventDefault()
    const form = event.target
    const formData = new FormData(form)
    const url = form.getAttribute('action')
    const method = form.getAttribute('method')
    const xhr = new XMLHttpRequest()
    const responseType = "json"
    xhr.responseType = responseType
    xhr.open(method, url)
    xhr.setRequestHeader("HTTP_X_REQUESTED_WITH", "XMLHttpRequest")
    xhr.setRequestHeader("X-Requested-With", "XMLHttpRequest")
    xhr.onload = function () {
         const serverResponse = xhr.response
         if (xhr.status === 200) {
             form.reset()
             if (url.includes(`${'/api/edit-task/'}`)) {
                 window.location.href = '/'
             }
             else if (url.includes(`${'/api/edit-list/'}`)) {
                 window.location.href = '/lists'
             }
         }
         else if (xhr.status === 400)
         {
             if (url.includes(`${'/api/edit-task/'}`)) {
                 //alert('Invalid task.')
             }
             else if (url.includes(`${'/api/edit-list/'}`)) {
                 alert('Invalid list.')
             }
         }
         else if (xhr.status === 403)
         {
             alert(serverResponse['message'])
         }
         else if (xhr.status === 404)
         {
            alert(serverResponse['message']) 
         }
    }
    xhr.send(formData)
}


function handleDeleteFormDidSubmit(event) {
    event.preventDefault()
    const form = event.target
    const url = form.getAttribute('action')
    const method = form.getAttribute('method')
    const xhr = new XMLHttpRequest()
    const responseType = "json"
    xhr.responseType = responseType
    xhr.open(method, url)
    xhr.setRequestHeader("HTTP_X_REQUESTED_WITH", "XMLHttpRequest")
    xhr.setRequestHeader("X-Requested-With", "XMLHttpRequest")
    xhr.onload = function () {
        const serverResponse = xhr.response
        if (xhr.status === 200) {
            form.reset()
            if (url.includes(`${'/api/delete-task/'}`)) {
                window.location.href = '/'
            }
            else if (url.includes(`${'/api/delete-list/'}`)) {
                window.location.href = '/lists'
            }
        }
        else if (xhr.status === 400)
        {
            form.reset()
            alert(serverResponse['message'])
        }
        else if (xhr.status === 403)
        {
            alert(serverResponse['message'])
        }
        else if (xhr.status === 404)
        {
            alert(serverResponse['message'])
        }
    }
    xhr.send(formData)
}


formElement = document.getElementById('form');

formElement.addEventListener('submit', handleEditFormDidSubmit)

deleteFormElement = document.getElementById('delete-form')
deleteFormElement.addEventListener('submit', handleDeleteFormDidSubmit)