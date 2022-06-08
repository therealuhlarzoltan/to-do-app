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
    xhr.onload = function() {
        if (xhr.status === 201) {
            form.reset()
            window.location.href='/'
        }
        else if (xhr.status === 200) {
            form.reset()
            window.location.href='/'
        }
        else if (xhr.status === 400)
        {
            form.reset()
        }
        else if (xhr.status === 403)
        {

        }
        else if (xhr.status === 404)
        {
            
        }
    }
    xhr.send(formData)
}

formElement = document.getElementById('form');

formElement.addEventListener('submit', handleCreationFormDidSubmit)