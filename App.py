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

