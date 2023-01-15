from flask import Flask, render_template, request
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
import os
# from flask_mysqldb import MySQL
import mysql.connector



app = Flask(__name__)
app.secret_key = "yotam"


# app.config['MYSQL_HOST'] = 'localhost'
# app.config['MYSQL_USER'] = 'root'
# app.config['MYSQL_PASSWORD'] = ''
# app.config['MYSQL_DB'] = 'flask'
 
# mysql = MySQL(app)


@app.route("/")
def home():
    if not os.path.isfile(f"templates/general.txt"):
        file = open(f"templates/general.txt", 'a')
        # cursor = mysql.connection.cursor()
        # cursor.execute(''' CREATE TABLE general(name, message) ''')
        # mysql.connection.commit()
        # cursor.close()
    return render_template('index.html')

@app.route("/<room>")
def rooms(room):
    if not os.path.isfile(f"templates/{room}.txt"):
        file = open(f"templates/{room}.txt", 'a')
        # cursor = mysql.connection.cursor()
        # cursor.execute(''' CREATE TABLE {room}(name, message) ''')
        # mysql.connection.commit()
        # cursor.close()
    return render_template('index.html')


@app.route("/api/chat/<room>", methods=["POST","GET"])
def post_chat(room):
    if request.method == "POST":
        name = request.form["username"]
        message = request.form["msg"]
        file = open(f"templates/{room}.txt", 'a')
        file.write(f"{datetime.now()} >> {name}:{message}\n")
        # cursor = mysql.connection.cursor()
        # cursor.execute(''' INSERT INTO {room} VALUES(%s,%s)''',(name,message))
        # mysql.connection.commit()
        # cursor.close()
        return message
    else:
        return render_template(f"{room}.txt")


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=80)