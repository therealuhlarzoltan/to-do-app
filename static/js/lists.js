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


function handleSortButtonClicked(event) {
    event.preventDefault()
    const sortMethod = event.target.innerHTML.toLowerCase()
    if (sortMethod === 'created') {
        sortByCreated()
    }
    else if (sortMethod === 'name') {
        sortByName()
    }
}



function sortByCreated() {
    const lis = [...document.getElementById('all-lists').getElementsByTagName('li')]
    lis.sort(objectComparisonByCreationDateCallback)
    list = document.getElementById('all-lists')
    list.innerHTML = ''
    lis.forEach(li => {
        list.appendChild(li)
    })

}


function  sortByName() {
    const lis = [...document.getElementById('all-lists').getElementsByTagName('li')]
    lis.sort(objectComparisonByNameCallback)
    list = document.getElementById('all-lists')
    list.innerHTML = ''
    lis.forEach(li => {
        list.appendChild(li)
    })
}


document.addEventListener('DOMContentLoaded', function() {
    const sortButtons = document.querySelectorAll('.dropdown-item')
    sortButtons.forEach(button => {
        button.addEventListener('click', handleSortButtonClicked)
    })
    const newListButton = document.getElementById('new-list-button')
    newListButton.addEventListener('click', function() {
        window.location.href = '/new-list'
    })
})