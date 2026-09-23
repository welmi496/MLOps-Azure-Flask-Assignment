import pytest

from app import app


@pytest.fixture()
def client():
    app.config.update(TESTING=True)
    return app.test_client()


def test_health(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.get_json()["status"] == "healthy"


def test_valid_prediction(client):
    response = client.post(
        "/predict",
        json={
            "sepal_length": 5.1,
            "sepal_width": 3.5,
            "petal_length": 1.4,
            "petal_width": 0.2,
        },
    )
    body = response.get_json()
    assert response.status_code == 200
    assert body["class_name"] == "setosa"
    assert 0 <= body["confidence"] <= 1


def test_missing_feature(client):
    response = client.post("/predict", json={"sepal_length": 5.1})
    assert response.status_code == 400
    assert response.get_json()["error"] == "Missing required fields"
