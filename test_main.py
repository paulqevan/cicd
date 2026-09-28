import pytest
from fastapi.testclient import TestClient
from main import app, calcul_cout

client = TestClient(app)


def test_calcul_cout():
    assert calcul_cout(100, 0.2) == 20.0


def test_calcul_cout_negatif():
    with pytest.raises(ValueError):
        calcul_cout(-1)


def test_endpoint_cout():
    r = client.get("/cout", params={"kwh": 100})
    assert r.status_code == 200
    assert r.json()["cout_eur"] == 25.0


def test_calcul_cout_heures_creuses():
    assert calcul_cout(100, 0.2, heures_creuses=True) == 16.0


def test_endpoint_cout_negatif():
    r = client.get("/cout", params={"kwh": -5})
    assert r.status_code == 400


def test_endpoint_heures_creuses():
    r = client.get("/cout", params={"kwh": 100, "heures_creuses": True})
    assert r.json()["cout_eur"] == 20.0
