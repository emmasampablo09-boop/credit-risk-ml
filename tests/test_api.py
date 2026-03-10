from fastapi.testclient import TestClient
from app.main import app
from app.model import model  # 

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
        "ExternalRiskEstimate": 70,
        "AverageMInFile": 30,
        "MSinceOldestTradeOpen": 60,
        "NumSatisfactoryTrades": 5,
        "PercentTradesNeverDelq": 90,
        "MSinceMostRecentInqexcl7days": 0,
        "MaxDelq2PublicRecLast12M": 0,
        "MaxDelqEver": 0
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
        "ExternalRiskEstimate": 0,
        "AverageMInFile": 0,
        "MSinceOldestTradeOpen": 0,
        "NumSatisfactoryTrades": 0,
        "PercentTradesNeverDelq": 0,
        "MSinceMostRecentInqexcl7days": 0,
        "MaxDelq2PublicRecLast12M": 0,
        "MaxDelqEver": 0
    })
    assert response.status_code == 200

def test_predict_bajo_riesgo():
    response = client.post("/predict", json={
        "ExternalRiskEstimate": 100,
        "AverageMInFile": 100,
        "MSinceOldestTradeOpen": 200,
        "NumSatisfactoryTrades": 20,
        "PercentTradesNeverDelq": 100,
        "MSinceMostRecentInqexcl7days": 24,
        "MaxDelq2PublicRecLast12M": 0,
        "MaxDelqEver": 0
    })
    assert response.status_code == 200
    assert response.json()['riesgo'] == 'Low'

def test_predict_error_interno(monkeypatch):
    def modelo_roto(*args, **kwargs):
        raise Exception("modelo roto")
    
    monkeypatch.setattr(model, 'predict_proba', modelo_roto)
    
    response = client.post('/predict', json={
        "ExternalRiskEstimate": 70,
        "AverageMInFile": 80,
        "MSinceOldestTradeOpen": 120,
        "NumSatisfactoryTrades": 10,
        "PercentTradesNeverDelq": 85,
        "MSinceMostRecentInqexcl7days": 6,
        "MaxDelq2PublicRecLast12M": 1,
        "MaxDelqEver": 2
    })
    assert response.status_code == 500