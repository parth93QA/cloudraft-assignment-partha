from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_set_testdata():
    keys = ["abcd-1", "abcd-2", "xyza-1", "xyza-2"]
    values = ["abcd1", "abcd2", "xyza1", "xyza2"]
    for i in range(0, len(keys)):
        client.post("/key/set",json={"key": keys[i], "value": values[i]})


def test_server_status():
    response = client.get("/")
    assert response.status_code == 200

def test_set_key_in_kv():
    response = client.post(
        "/key/set",
        json={"key": "abc-1", "value": "abc1"},
    )
    assert response.status_code == 200

def test_set_second_key_in_kv():
    response = client.post(
        "/key/set",
        json={"key": "abc-2", "value": "abc2"},
    )
    assert response.status_code == 200

def test_set_third_key_in_kv():
    response = client.post(
        "/key/set",
        json={"key": "abc-3", "value": "abc3"},
    )
    assert response.status_code == 200


def test_set_key_in_kv_already_exists():
    response = client.post(
        "/key/set",
        json={"key": "abcd-1", "value": "abcd1"},
        
    )
    assert response.status_code == 200
    assert response.json() == {'message': 'Key abcd-1 already exists.'}  

def test_read_item_from_kv():
    response = client.get("/get/abcd-1")
    assert response.status_code == 200
    assert response.json() == {
       "value": "abcd1"
    }


def test_read_item_not_stored_in_kv():
    response = client.get("/items/abc")
    assert response.status_code == 404
    assert response.json() == {'detail': 'Not Found'}


def test_search_keys_by_prefix_and_suffix():
    response = client.get("/search?prefix=abc&suffix=-1")
    assert response.status_code == 200
    assert response.json() == {"message": "Either Prefix or Suffix can only be passed for the search endpoint."}

def test_search_by_prefix():

    response = client.get("/search?prefix=abc")
    assert response.status_code == 200
    assert response.json() == {
  "Matching Key List": [
   "abcd-1", "abcd-2", "abc-1", "abc-2", "abc-3"
  ]
}

    
def test_search_by_suffix():

    response = client.get("/search?suffix=-1")
    assert response.status_code == 200
    assert response.json() == {
  "Matching Key List": [
    "abcd-1", "xyza-1", "abc-1"
  ]
}