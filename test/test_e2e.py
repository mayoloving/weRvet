import requests
import json
# import pytest

#======================================================================================================

base_url = "http://localhost:5000"

#==============================/===============================
def test_get_request():
    response = requests.get(base_url + "/")
    assert response.status_code == 200
    # print(response.content)
    
#==============================/pet===============================
def test_get_pet_request():
    response = requests.get(base_url + "/pet")
    assert response.status_code == 200
    json_response = json.loads(response.text)
    print(json_response)
    # print(response.content)
    
def test_post_pet_request():
    file = open("/home/yotambenz/Desktop/portfolio-yotambenz/weRvet/test/sanity.json", "r")
    json_input = file.read()
    request_json = json.loads(json_input)
    print(request_json)

    response = requests.post(base_url + "/pet", request_json)
    print(response.content)
    assert response.status_code == 200
    
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
#     response = requests.put(base_url + "/pet/12", )
#     assert response.status_code == 200
    
#     data = response.json()
#     print(data)


# def test_delete_petid_request():
#     response = requests.delete(base_url + "/pet/12")
#     print(response.status_code)
#     assert response.status_code == 200
