import joblib
from pathlib import Path

# Ruta al modelo guardado
ROOT       = Path(__file__).resolve().parent.parent
MODEL_PATH = ROOT / 'models' / 'lightgbm_best.pkl'

# Features que usa el modelo
FEATURES = [
    'ExternalRiskEstimate',
    'AverageMInFile',
    'MSinceOldestTradeOpen',
    'NumSatisfactoryTrades',
    'PercentTradesNeverDelq',
    'MSinceMostRecentInqexcl7days',
    'MaxDelq2PublicRecLast12M',
    'MaxDelqEver'
]

# Métricas del modelo entrenado
METRICS = {
    'auc':  0.7897,
    'gini': 0.5795,
    'ks':   0.4373
}


# Cargar modelo
def load_model():
    model = joblib.load(MODEL_PATH)
    print(f'Modelo cargado desde {MODEL_PATH}')
    return model

model = load_model()