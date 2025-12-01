import app

def test_prediction():
    client = app.app.test_client()
    response = client.get("/predict?value=5")

    assert response.status_code == 200
    assert response.json["prediction"] == 10
