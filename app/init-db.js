db = db.getSiblingDB("pets_db");
db.pets_tb.drop()

db.pets_tb.insertMany([
    {
        "name": "blanco",
        "id": 1,
        "gender": "M",
        "type": "dog",
        "message": "he is cute"
    },
    {
        "name": "rexy",
        "id": 2,
        "gender": "F",
        "type": "cat",
        "message": "wowza"
    }
]);