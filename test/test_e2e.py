import requests
import json
from bson import json_util
# import pytest

#======================================================================================================

base_url = "http://localhost:5000"

#==============================/===============================
def test_get_request():
    response = requests.get(base_url + "/")
    assert response.status_code == 200
    # print(response.content)
    # assert response.json() == {"items": ["item1", "item2", "item3"]}
    
#==============================/pet===============================
def test_get_pet_request():
    response = requests.get(base_url + "/pet")
    assert response.status_code == 200
    json_response = json.loads(response.text)
    print(json_response)
    # print(response.content)
    
def test_post_pet_request():
    payload = {
            "petname": "doggo",
            "id": "12",
            "gen": "M",
            "animal": "doggo",
            "msg": "doggo"
        }
    request_json = json.loads(payload)
    print(request_json)
    # response = requests.post(base_url + "/pet", data=json.dumps(payload))
    # assert response.status_code == 200
    # # data = response.json()
    # # assert data["petname"] == payload["petname"]
    # # print(data)
    # assert response.headers["Content-Type"] == "application/json"
    # assert response.json() == {"message": "Pet created successfully.", "id": "12"}
    
# #==============================/pet/<id>/===============================
def test_get_petid_request():
    response = requests.get(base_url + "/pet/2")
    assert response.status_code == 200
    print(response.content)


# def test_put_petid_request():
#     payload = {
#             "petname": "doggo",
#             "gen": "M",
#             "animal": "doggo",
#             "msg": "doggo"
#         }
#     response = requests.put(base_url + "/pet/3", data=json.loads(json_util.dumps(payload)))
#     assert response.status_code == 200
    
#     data = response.json()
#     print(data)


# def test_delete_petid_request():
#     response = requests.delete(base_url + "/pet/3")
#     print(response.status_code)
#     assert response.status_code == 200
