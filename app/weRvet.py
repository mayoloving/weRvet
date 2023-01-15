from flask import Flask, render_template, request
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
import os



app = Flask(__name__)
app.secret_key = "yotam"


@app.route("/")
def home():
    return render_template('index.html')

@app.route("/metrics")
def metrics():
    return render_template('index.html')

@app.route("/pet")
def pets_ids():
    return render_template('index.html')


@app.route("/pet/<id>", methods=["POST","GET","DELETE","PUT"])
def specs_pet(id):
    if request.method == "POST":
        # `POST /pet/{id}` with body containing some details as JSON.
        return render_template('index.html')

    elif request.method == "GET":
        # `GET /pet/{id}` to return specific JSON object.
        return render_template('index.html')

    elif request.method == "DELETE":
        # `DELETE /pet/{id}` remove an entity from database.
        return render_template('index.html')

    else:
        # `PUT /pet/{id}` same thing exactly, but updates existing pet.
        return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)# , host="0.0.0.0", port=80