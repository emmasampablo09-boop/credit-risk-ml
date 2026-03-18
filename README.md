# Credit Risk ML System 

End-to-end machine learning system for credit default prediction using the HELOC dataset, deployed as a production REST API.


## Live API 
https://credit-risk-ml-production-e815.up.railway.app/docs

## Model Results
| Metric | Value |
|--------|-------|
| AUC-ROC | 0.7899 |
| Gini | 0.5795 |
| KS | 0.4373 |
| Test Coverage | 100% |

## Tech Stack 
| Area | Tools |
|------|-------|
| ML | LightGBM, XGBoost, scikit-learn |
| Tuning | Optuna |
| MLOps | MLflow |
| API | FastAPI, Pydantic |
| Testing | pytest |
| Deploy | Docker, Railway |

## Features Description

| Feature | Description |
|---------|-------------|
| `NetFractionRevolvingBurden` | Net fraction of revolving debt burden |
| `ExternalRiskEstimate` | External credit risk score |
| `AverageMInFile` | Average months on credit file |
| `PercentTradesWBalance` | Percentage of trades with balance |
| `MSinceOldestTradeOpen` | Months since oldest trade opened |
| `NumSatisfactoryTrades` | Number of satisfactory trades |
| `PercentInstallTrades` | Percentage of installment trades |
| `MSinceMostRecentInqexcl7days` | Months since most recent inquiry (excl. last 7 days) |

## Feature Selection

The original HELOC dataset contains 23 features. Through correlation analysis and multicollinearity reduction, 8 features were selected maintaining competitive model performance:

- Removed features with low correlation to target (< 0.10)
- Eliminated redundant pairs with inter-feature correlation > 0.85
- Final model retains **AUC-ROC 0.79** with only 8 features vs 23

## Structure of Project
credit-risk-ml/
├── app/
│   ├── main.py              # API endpoints (health, metrics, predict)
│   ├── model.py             # Model loading and feature definitions
│   ├── schemas.py           # Pydantic input validations
│   └── logger.py            # Request logging
├── models/
│   └── lightgbm_best.pkl    # Trained LightGBM model
├── notebooks/
│   ├── 01_EDA.ipynb         # Exploratory data analysis
│   ├── 02_Modeling.ipynb    # Model training and evaluation
│   └── mlruns/              # MLflow experiment tracking
├── tests/
│   └── test_api.py          # Unit tests (100% coverage)
├── Dockerfile               # Container configuration
├── requirements.txt         # Project dependencies
└── README.md


## API Endpoints
| Endpoint | Method | Description |
|----------|--------|-------------|
| / | GET | Project info |
| /health | GET | API status |
| /metrics | GET | Model metrics |
| /predict | POST | Default probability |


## Predict Example
"""
json
{
    "NetFractionRevolvingBurden": 50,
    "ExternalRiskEstimate": 70,
    "AverageMInFile": 80,
    "PercentTradesWBalance": 60,
    "MSinceOldestTradeOpen": 120,
    "NumSatisfactoryTrades": 10,
    "PercentInstallTrades": 40,
    "MSinceMostRecentInqexcl7days": 6
}
"""

## Predict Response Example
"""
json
{
    "probabilidad": 0.2341,
    "riesgo": "Low"
}
"""

## Author
Emmanuel Sampablo
