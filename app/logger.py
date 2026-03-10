import logging
import os
from datetime import datetime
from pathlib import Path

# Ruta absoluta a la carpeta logs
ROOT = Path(__file__).resolve().parent.parent
LOGS_DIR = ROOT / 'logs'
LOGS_DIR.mkdir(exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(LOGS_DIR / 'api.log'),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)

def log_prediction(inputs: dict, resultado: dict):
    logger.info({
        'timestamp': datetime.now().isoformat(),
        'inputs':    inputs,
        'resultado': resultado
    })