# verify_setup.py
import sklearn, lightgbm, xgboost, mlflow, pandas
print("✅ scikit-learn:", sklearn.__version__)
print("✅ LightGBM:", lightgbm.__version__)
print("✅ XGBoost:", xgboost.__version__)
print("✅ MLflow:", mlflow.__version__)
print("✅ pandas:", pandas.__version__)