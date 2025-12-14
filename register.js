//alert('Yo');

const btnSubmit = document.getElementById("register");

let success = document.getElementById("alertSuccess");

btnSubmit.addEventListener('click', async function (e){
e.preventDefault();

let name = document.getElementById('name');

let email = document.getElementById('email');

let password = document.getElementById('password');

//DON'T USE FORM DATA - NOT ACCEPTED
const dataToSend = {
    name: name.value,
    email: email.value,
    password:password.value
};

fetch('http://127.0.0.1:5000/register', { // Replace with your API endpoint
    method: 'POST',
    headers: {
        'Content-Type': 'application/json'
    },
    body: JSON.stringify(dataToSend)
})
.then(response => response.json()) // Parse the JSON response from the API
.then(data => {
	alert('Success' + JSON.stringify(data));
    console.log('Success:', data);
})
.catch(error => {
    console.error('Error:', error);
});



})