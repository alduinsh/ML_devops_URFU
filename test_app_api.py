from fastapi.testclient import TestClient
from app_api import app

client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}


def test_predict_normal():
    response = client.post("/predict/",
        json={"text": "я люблю машинное обучение!"}
    )
    json_data = response.json() 

    assert response.status_code == 200
    assert json_data['label'] == 'neutral'


def test_predict_insult():
    response = client.post("/predict/",
        json={"text": "скотина! что сказать"}
    )
    json_data = response.json() 

    assert response.status_code == 200
    assert json_data['label'] == 'toxic'


def test_predict_threat():
    response = client.post("/predict/",
        json={"text": "расстрелять к чёртовой матери"}
    )
    json_data = response.json() 

    assert response.status_code == 200
    assert json_data['label'] == 'toxic'


def test_predict_obscenity():
    response = client.post("/predict/",
        json={"text": "в очко тебе 👎👎👎по больше"}
    )
    json_data = response.json() 

    assert response.status_code == 200
    assert json_data['label'] == 'toxic'