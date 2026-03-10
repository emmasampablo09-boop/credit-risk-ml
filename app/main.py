from fastapi import FastAPI, HTTPException
from app.model import model, FEATURES, METRICS
import pandas as pd
from app.schemas import ClienteInput
from app.logger import log_prediction

app = FastAPI(title='Credit Risk API ', 
              description='Predice el riesgo crediticio de un cliente usando un modelo LightGBM entrenado.', 
              version='1.0.0'
              )


## GET /HEALTH
@app.get('/health')
def health():
    return {'status': 'ok', "modelo": "LightGBM", "version": "1.0.0"}

## get / METRICS
@app.get('/metrics')
def get_metrics():
    return METRICS


### post / predict
@app.post('/predict')
def predict(cliente: ClienteInput):
    try:
        datos = pd.DataFrame([cliente.model_dump()])
        prob = model.predict_proba(datos[FEATURES])[0][1]
        riesgo = "High" if prob >= 0.5 else "Low"
        resultado = {"probabilidad": round(float(prob), 4), 
            "riesgo": riesgo
        }
        log_prediction(cliente.model_dump(), resultado)

        return resultado
    except Exception as e:
        raise HTTPException(status_code=500, detail=F"Error al procesar la predicción: {str(e)}")
    