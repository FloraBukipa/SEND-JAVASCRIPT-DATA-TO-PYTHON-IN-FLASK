# SEND-JAVASCRIPT-DATA-TO-PYTHON-IN-FLASK
To send data from JavaScript to Python, you need to use a server-side application (like a Python web framework e.g Flask or Django) to receive an HTTP request (Fetch call) from your client-side JavaScript code. The data is commonly sent in JSON format. 
Key Technologies
•	JavaScript (Client-Side): Used to capture data and send the request using the fetch API 
•	Python (Server-Side): Used with a web framework like Flask or Django to set up an API endpoint that listens for the request and processes the data. 
Step-by-Step Example Using Flask
This is a common and straightforward method for web applications. 
1. Set up the Python Server (Flask) 
First, ensure you have Flask installed (pip install Flask). Create a Python file (e.g., app.py) to run your server and define a route to receive the data. 
Python code (App.py)
from flask import Flask, render_template, jsonify, request
from flask_cors import CORS 
import json
import mysql.connector

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return render_template('index.html')
conn = mysql.connector.connect(
    host="localhost",
    user = "root",
    password="",
    port =3306,
    database="webdev"
    )
@app.route('/users')
def get_users():
    sql="SELECT * FROM login"
    cursor = conn.cursor()
    cursor.execute(sql)

    records = cursor.fetchall()

    return jsonify(records)

@app.route('/register', methods = ['POST'])
def create_users():
    if request.is_json:
        data = request.get_json()
        print(json.dumps(data))

        name = data["name"]
        email = data["email"]
        password = data["password"]

    if name and email and password:

        sql = "INSERT INTO login (name, email, password) VALUES (%s,%s,%s)"
        values = (name, email, password)
        cursor = conn.cursor()
        cursor.execute(sql,values)
        conn.commit()

        return jsonify({"message": "Data received successfully!"}), 200
    else:
        return jsonify({"message": "Empty Fields Not Accepted"}), 400

if __name__ =='__main__':
    app.run(debug=True)
2. Create HTML Page
HTML(index.html)
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sending Data to Python Backend</title>
    <style>
        /* Basic styling to approximate the look in the image */
        body {
            font-family: Arial, sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            margin: 0;
            background-color: #f4f4f4;
        }

        .form-container {
            background-color: white;
            padding: 40px;
            border-radius: 8px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            width: 350px;
        }

        h2, h3 {
            text-align: left;
            margin-bottom: 5px;
            color: #333;
        }

        h2 {
            font-size: 1.5em;
        }

        h3 {
            font-size: 1.1em;
            color: #555;
            margin-bottom: 20px;
        }

        .form-group {
            margin-bottom: 20px;
        }

        label {
            display: block;
            font-size: 0.9em;
            color: #666;
            margin-top: 5px;
        }

        input[type="text"],
        input[type="email"],
        input[type="password"] {
            width: 100%;
            padding: 10px;
            border: 1px solid #ccc;
            border-radius: 4px;
            box-sizing: border-box; /* Important for padding/border not adding to total width */
            font-size: 1em;
        }

        button {
            background-color: #007bff; /* Blue button color */
            color: white;
            padding: 10px 20px;
            border: none;
            border-radius: 4px;
            cursor: pointer;
            font-size: 1em;
        }

        button:hover {
            background-color: #0056b3;
        }
    </style>
</head>
<body>
    <div class="form-container">
        <h2>SENDING DATA FROM FRONTEND TO PYTHON BACKEND</h2>
        <h3>JAVASCRIPT TO PYTHON</h3>
            <div class="form-group">
                <input type="text" id="name" name="name" value="MUTIU GBANGBA SEPOTOYON" required>
                <label for="name">Name</label>
            </div>

            <div class="form-group">
                <input type="email" id="email" name="email" value="mutiu@gmail.com" required>
                <label for="email">Email</label>
            </div>
            <div class="form-group">
                <input type="password" id="password" name="password" value="********" required>
                <label for="password">Password</label>
            </div>
            <button type="submit" id="register">Submit</button>  
    </div>
<script src="register.js"></script>
    </body>
</html>

3. JavaScript Page
JAVASCRIPT (register.js)
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

