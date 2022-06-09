function handleCreationFormDidSubmit(event) {
    event.preventDefault()
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
        if (xhr.status === 201) {
            form.reset()
            if (url === '/api/create-task/') {
                window.location.href = '/'
            }
            else if (url === '/api/create-list/') {
                window.location.href = '/lists'
            }
            else {
                window.location.href = '/'
            }
        }
        else if (xhr.status === 400)
        {
           alert(serverResponse['message'])
        }
        else if (xhr.status === 500) {
            alert('Internal Server Error! Please try again later.')
        }
    }
    xhr.send(formData)
}

formElement = document.getElementById('form');

formElement.addEventListener('submit', handleCreationFormDidSubmit)