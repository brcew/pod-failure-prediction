from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd

app = FastAPI()

# Load model
model = joblib.load("models/best_model.pkl")

# Define input schema
class PodData(BaseModel):
    cpu_usage_pct: float
    memory_usage_pct: float
    memory_leak_rate: float
    restart_count_24h: int
    error_log_rate: int
    request_latency_ms: float
    replica_count: int
    node_pressure_score: float
    autoscaler_action: str
    prometheus_anomaly_score: float
    previous_failures: int
    deployment_uptime_hrs: float

@app.get("/")
def home():
    return {"message": "Pod Failure Prediction API is Live!"}

@app.post("/predict")
def predict(data: PodData):

    df = pd.DataFrame([data.dict()])

    prediction = model.predict(df)[0]

    status = "Pod is likely to FAIL soon ❗" if prediction == 1 else "Pod is Healthy ✔️"

    return {
        "prediction": int(prediction),
        "status": status
    }
