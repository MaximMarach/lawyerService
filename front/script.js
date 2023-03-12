function create_user(event){
    var user = get_data_form()
    console.log(user)
    let response = fetch('http://127.0.0.1:8000/contact/contact/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json;charset=utf-8'
            },
        body: JSON.stringify(user)
    });
    console.log(response.JSON)
}

function get_data_form(){
    var inputs = document.getElementsByClassName('field')
    var data = []
    
    for(let i = 0; i < inputs.length; i++){
        data.push(inputs[i].value)
    } 
    
    user = {
        first_name: data[0],
        second_name: data[1],
        email: data[2],
        phone_number: data[3],
        description: data[4]
    };

    return user
}

var form = document.getElementsByClassName('decor')[0];
form.addEventListener("submit", create_user)















// fetch("http://127.0.0.1:8000/contact/contact/")
//   .then((response) => response.json())
//   .then((data) => console.log(data));


// let user = {
//     first_name: 'John',
//     second_name: 'Smith',
//     email: 'smith@mail.ru',
//     phone_number: '+37529292929',
//     description: 'Небольшие проблемы с ГАИ'
// };

// let response = fetch('http://127.0.0.1:8000/contact/contact/', {
//     method: 'POST',
//     headers: {
//       'Content-Type': 'application/json;charset=utf-8'
//     },
//     body: JSON.stringify(user)
//   });
  
//   let result = response.json;
