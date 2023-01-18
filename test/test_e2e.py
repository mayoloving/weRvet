import requests
import json
# import pytest

#======================================================================================================

base_url = "http://localhost:5000"

#==============================/===============================
def test_get_request():
    response = requests.get(base_url + "/")
    assert response.status_code == 200
    # assert response.json() == {"items": ["item1", "item2", "item3"]}
    
#==============================/pet===============================
def test_get_pet_request():
    response = requests.get(base_url + "/pet")
    assert response.status_code == 200
    # assert response.json() == {"items": ["item1", "item2", "item3"]}
    
# def test_post_pet_request():
#     data = {
#             "name": "doggo",
#             "id": "12",
#             "gender": "M",
#             "type": "doggo",
#             "message": "doggo"
#         }
#     headers = {"Content-Type": "application/json"}
#     response = requests.post(base_url + "/pet", data=json.dumps(data), headers=headers)
#     assert response.status_code == 201
#     assert response.json() == {"message": "Pet created successfully."}
    
# #==============================/pet/<id>/===============================
# def test_get_petid_request():
#     response = requests.get(base_url + "/pet/<id>")
#     assert response.status_code == 200
#     assert response.json() == {"items": ["item1", "item2", "item3"]}

# def test_put_petid_request():
#     data = {
#             "name": "doggo",
#             "gender": "F",
#             "type": "doggo",
#             "message": "doggo"
#         }
#     headers = {"Content-Type": "application/json"}
#     response = requests.put(base_url + "/pet/<id>", data=json.dumps(data), headers=headers)
#     assert response.status_code == 200
#     assert response.json() == {"message": "Item updated"}

# def test_delete_petid_request():
#     response = requests.delete(base_url + "/pet/<id>")
#     assert response.status_code == 200
#     assert response.json() == {"message": "Item deleted"}
