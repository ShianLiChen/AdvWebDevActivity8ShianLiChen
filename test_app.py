# test_app.py
import app


def test_hello():
    client = app.app.test_client()
    response = client.get('/hello')
    assert response.status_code == 200
    assert response.get_json() == {"message": "Hello, World!"}


def test_echo():
    client = app.app.test_client()
    payload = {"msg": "ping"}
    response = client.post('/echo', json=payload)
    assert response.status_code == 201
    assert response.get_json() == payload


def test_update():
    client = app.app.test_client()
    payload = {"item": "test"}
    response = client.put('/update', json=payload)
    assert response.status_code == 200
    assert response.get_json() == {"updated": True, "item": "test"}


def test_remove():
    client = app.app.test_client()
    payload = {"item": "test"}
    response = client.delete('/remove', json=payload)
    assert response.status_code == 200
    assert response.get_json() == {"deleted": True, "item": "test"}
