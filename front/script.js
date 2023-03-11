

function set_div_content(content){
    var div = document.getElementsByClassName('json')[0]
    div.textContent = content
}

var xhr = new XMLHttpRequest()

xhr.open('GET', 'http://127.0.0.1:8000/contact/contact/')
xhr.onload = () => {
    const response =  xhr.responseText
    set_div_content(response)
    console.log(response)
}
xhr.send();