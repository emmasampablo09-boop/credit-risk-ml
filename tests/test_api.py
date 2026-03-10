from fastapi.testclient import TestClient
from app.main import app
from app.model import model

client = TestClient(app)

def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"

def test_metrics():
    response = client.get("/metrics")
    assert response.status_code == 200
    assert "auc" in response.json()

def test_predict_valido():
    response = client.post("/predict", json={
        "NetFractionRevolvingBurden": 50,
        "ExternalRiskEstimate": 70,
        "AverageMInFile": 80,
        "PercentTradesWBalance": 60,
        "MSinceOldestTradeOpen": 120,
        "NumSatisfactoryTrades": 10,
        "PercentInstallTrades": 40,
        "MSinceMostRecentInqexcl7days": 6
    })
    assert response.status_code == 200
    assert 'probabilidad' in response.json()
    assert 'riesgo' in response.json()

def test_predict_invalido():
    response = client.post("/predict", json={
        "ExternalRiskEstimate": -999
    })
    assert response.status_code == 422

def test_predict_edge_case():
    response = client.post("/predict", json={
        "NetFractionRevolvingBurden": 0,
        "ExternalRiskEstimate": 0,
        "AverageMInFile": 0,
        "PercentTradesWBalance": 0,
        "MSinceOldestTradeOpen": 0,
        "NumSatisfactoryTrades": 0,
        "PercentInstallTrades": 0,
        "MSinceMostRecentInqexcl7days": 0
    })
    assert response.status_code == 200

def test_predict_bajo_riesgo():
    response = client.post("/predict", json={
        "NetFractionRevolvingBurden": 10,
        "ExternalRiskEstimate": 100,
        "AverageMInFile": 100,
        "PercentTradesWBalance": 20,
        "MSinceOldestTradeOpen": 200,
        "NumSatisfactoryTrades": 20,
        "PercentInstallTrades": 80,
        "MSinceMostRecentInqexcl7days": 24
    })
    assert response.status_code == 200
    assert response.json()['riesgo'] == 'Low'

def test_predict_error_interno(monkeypatch):
    def modelo_roto(*args, **kwargs):
        raise Exception("modelo roto")
    
    monkeypatch.setattr(model, 'predict_proba', modelo_roto)
    
    response = client.post('/predict', json={
        "NetFractionRevolvingBurden": 50,
        "ExternalRiskEstimate": 70,
        "AverageMInFile": 80,
        "PercentTradesWBalance": 60,
        "MSinceOldestTradeOpen": 120,
        "NumSatisfactoryTrades": 10,
        "PercentInstallTrades": 40,
        "MSinceMostRecentInqexcl7days": 6
    })
    assert response.status_code == 500
