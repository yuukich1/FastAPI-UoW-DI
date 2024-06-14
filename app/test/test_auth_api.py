from fastapi.testclient import TestClient
import pytest
from app.config import fake
from app.main import app

import time
client = TestClient(app)

def test_registration():
    username = fake.user_name()
    email = fake.email(domain='gmail.com')
    password = fake.password()
    response = client.post('/auth/registration', json={'username': username, 'email': email, 'password': password})
    assert response.status_code == 201
    json = response.json()
    assert json['email'] == email
    assert json['username'] == username

def test_login():
    time.sleep(1)
    response = client.post('/auth/login', data={'username': 'string', 'password': 'string'},
                           headers={"Content-Type": "application/x-www-form-urlencoded"} )
    assert response.status_code == 200
    assert response.json()['type'] == 'bearer'

def test_failed_login():
    time.sleep(1)
    response = client.post('/auth/login', data={'username': 'string', 'password': 'zxc'},
                           headers={"Content-Type": "application/x-www-form-urlencoded"})
    assert response.status_code == 401
