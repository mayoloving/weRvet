from flask import Flask, render_template, request, jsonify
# from datetime import datetime
from pymongo import MongoClient
import os

app = Flask(__name__)
# app.secret_key = "yotam"

def get_db():
    client = MongoClient(host='test_mongodb', port=27017, username='root', password='pass12345', authSource='admin')

    db = client["pets_db"]
    return db


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/metrics", methods=["GET"])
# `GET /metrics` use later, for monitoring.
def metrics():
    return render_template('index.html')


@app.route("/pet", methods=["GET"])
# `GET /pet` to get a JSON array of pet ids.
def fetch_pets_ids():
    db = get_db()
    _animals = db.pets_tb.find()
    animals = [{"name": animal["name"], "id": animal["id"], "gender": animal["gender"], "type": animal["type"], "message": animal["message"]} for animal in _animals]
    return jsonify({"animals":animals})
    # return render_template('index.html')


@app.route("/pet/<id>", methods=["POST","GET","DELETE","PUT"])
def specs_pet(id):
    if request.method == "POST":
        # `POST /pet/{id}` with body containing some details as JSON.
        name = request.form["petname"]
        ids = request.form["id"]
        gender = request.form["gen"]
        animaltype = request.form["animal"]
        message = request.form["msg"]
        return render_template('form.html')

    elif request.method == "GET":
        # `GET /pet/{id}` to return specific JSON object.
        return render_template('form.html')

    elif request.method == "DELETE":
        # `DELETE /pet/{id}` remove an entity from database.
        return render_template('index.html')

    else:
        # `PUT /pet/{id}` same thing exactly, but updates existing pet.
        return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)