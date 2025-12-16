import os
import logging
import pandas as pd
from typing import List, Dict, Any

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

import mlflow.pyfunc

# --------------------------------------------------
# Logging
# --------------------------------------------------
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# --------------------------------------------------
# Constants
# --------------------------------------------------
MODEL_DIR = os.getenv("MODEL_DIR", "/app/model")

# --------------------------------------------------
# Load model at startup
# --------------------------------------------------
try:
    logger.info(f"🔍 Loading model from: {MODEL_DIR}")
    model = mlflow.pyfunc.load_model(MODEL_DIR)
    logger.info("✅ Model loaded successfully")
except Exception as e:
    logger.exception("❌ Failed to load model")
    raise RuntimeError(f"Model loading failed: {e}")

# --------------------------------------------------
# FastAPI app
# --------------------------------------------------
app = FastAPI(
    title="ML Model Inference API",
    version="1.0.0",
    description="Production ML inference service (Databricks → GitHub → ECR)"
)

# --------------------------------------------------
# Request / Response Schemas
# --------------------------------------------------
class PredictRequest(BaseModel):
    inputs: List[Dict[str, Any]]

class PredictResponse(BaseModel):
    predictions: List[Any]

# --------------------------------------------------
# Health check
# --------------------------------------------------
@app.get("/health")
def health():
    return {"status": "ok"}

# --------------------------------------------------
# Prediction endpoint
# --------------------------------------------------
@app.post("/predict", response_model=PredictResponse)
def predict(request: PredictRequest):
    try:
        if not request.inputs:
            raise ValueError("Input list is empty")

        df = pd.DataFrame(request.inputs)
        logger.info(f"📥 Received {len(df)} records")

        preds = model.predict(df)

        return {"predictions": preds.tolist()}

    except Exception as e:
        logger.exception("❌ Prediction failed")
        raise HTTPException(status_code=400, detail=str(e))
