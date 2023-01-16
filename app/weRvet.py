from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient
from bson import json_util
import json
import os


app = Flask(__name__)

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


@app.route("/pet/<id>/", methods=["POST","GET","DELETE","PUT"])
def specs_pet(id):
    if request.method == "POST":
        # `POST /pet/{id}` with body containing some details as JSON.
        name = request.form["petname"]
        ids = request.form["id"]
        gender = request.form["gen"]
        animaltype = request.form["animal"]
        message = request.form["msg"]

        db = get_db()
        new_pet = {
            "name": name,
            "id": ids,
            "gender": gender,
            "type": animaltype,
            "message": message
        }
        db.pets_tb.insert_one(new_pet)
        return "Pet added successfully"

    elif request.method == "GET":
        # `GET /person/{id}` to return specific JSON object.
        db = get_db()
        result = list(db.pets_tb.find({"id": id}))
        return render_template('form.html', data = json.loads(json_util.dumps(result)))


    elif request.method == "DELETE":
        # `DELETE /pet/{id}` remove an entity from database.
        db = get_db()
        db.pets_tb.delete_one({"id": id})
        return "Pet successfully deleted"

    else:
        # `PUT /pet/{id}` same thing exactly, but updates existing pet.
        name = request.form["petname"]
        ids = request.form["id"]
        gender = request.form["gen"]
        animaltype = request.form["animal"]
        message = request.form["msg"]

        db = get_db()
        # update_pet = {
        #     "name": name,
        #     "id": ids,
        #     "gender": gender,
        #     "type": animaltype,
        #     "message": message
        # }
        # db.pets_tb.update_one(update_pet)
        # return "Pet updated successfully"

        new_values = { "$set": {"name": name,"id": ids, "gender": gender, "type": animaltype, "message": message}}
        db.pets_tb.update_one({"id": int(id)}, new_values)
        return "Pet successfully updated"

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)