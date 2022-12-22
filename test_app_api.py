from fastapi.testclient import TestClient
from app_api import app

client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}


def test_predict_positive():
    response = client.post("/predict/",
        json={"text": "I люблю машинное обучение!"}
    )
    json_data = response.json() 

    assert response.status_code == 200
    assert json_data['label'] == 'POSITIVE'


def test_predict_negative():
    response = client.post("/predict/",
        json={"text": "Я ненавижу машинное обучение!"}
    )
    json_data = response.json() 

    assert response.status_code == 200
    assert json_data['label'] == 'NEGATIVE'