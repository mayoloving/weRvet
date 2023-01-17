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


@app.route("/pet/<id>/", methods=["POST","GET"])
def specs_pet(id):
    if request.method == "POST":
        # `POST /pet/{id}` with body containing some details as JSON.
        name = request.form.get("petname")
        ids = request.form.get("id")
        gender = request.form.get("gen")
        animaltype = request.form.get("animal")
        message = request.form.get("msg")

        db = get_db()
        new_pet = {
            "name": name,
            "id": ids,
            "gender": gender,
            "type": animaltype,
            "message": message
        }

        for key, value in new_pet.items():
            if value is None or value == "":
                return (f"{key} is null;enter again")
        try:
            result = list(db.pets_tb.find({"id": id}))
            return "the id already exists"
        except:
            db.pets_tb.insert_one(new_pet)
            return "Pet added successfully"

    else:
        # `GET /person/{id}` to return specific JSON object.
        db = get_db()
        result = list(db.pets_tb.find({"id": id}))
        return render_template('form.html', data = json.loads(json_util.dumps(result)))


@app.route("/pet/update/<id>/", methods=["POST"])
def update_pet(id):
    # `PUT /pet/{id}` same thing exactly, but updates existing pet.
    name = request.form.get("petname")
    gender = request.form.get("gen")
    animaltype = request.form.get("animal")
    message = request.form.get("msg")
    
    db = get_db()

    new_pet = {
            "name": name,
            "gender": gender,
            "type": animaltype,
            "message": message
        }

    for key, value in new_pet.items():
        if value is None or value == "":
            return (f"{key} is null;enter again")

    if not list(db.pets_tb.find({"id": id})):
        return "pet not here" ,404
    
    db.pets_tb.update_one({"id": id}, { "$set": new_pet})
    return "Pet successfully updated"


@app.route("/pet/delete/<id>/", methods=["POST"])
def delete_pet(id):
    # `DELETE /person/{id}` remove an entity from database.
    db = get_db()
    result = db.pets_tb.delete_one({"id": id})
    if result.deleted_count == 1:
        return "Pet deleted successfully"
    else:
        return "Pet not found"




if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)