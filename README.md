🚀 Pod Failure Prediction System

This project predicts if a Kubernetes pod will fail soon or if it is healthy using Machine Learning.
It has 3 parts:

⚙️ Machine Learning model

🌐 FastAPI backend

🖥️ Streamlit dashboard

Easy for anyone to test.

✨ Features

Predicts pod failure using ML

Clean Streamlit dashboard

FastAPI endpoint /predict

Dark Purple theme

Beginner-friendly structure

▶️ How to Run the Project
🟣 Run API
uvicorn api.main:app --reload


Open:

http://127.0.0.1:8000/docs

🟣 Run Dashboard
streamlit run app/dashboard.py

🧪 Sample JSON Input

Put this in API:

{
  "cpu_usage_pct": 75,
  "memory_usage_pct": 60,
  "memory_leak_rate": 0.08,
  "restart_count_24h": 1,
  "error_log_rate": 5,
  "request_latency_ms": 120,
  "replica_count": 3,
  "node_pressure_score": 0.50,
  "autoscaler_action": "scale_up",
  "prometheus_anomaly_score": 0.45,
  "previous_failures": 2,
  "deployment_uptime_hrs": 150
}

📁 Project Structure (Simple)
api/main.py        → FastAPI backend
app/dashboard.py   → Streamlit UI
src/train_model.py → Train the ML model
src/predict.py     → Test predictions
models/            → Saved model
assets/            → Screenshots
examples/          → Sample JSON inputs

🧠 Model Details

Algorithm → Logistic Regression

Preprocessing → StandardScaler + OneHotEncoder

Saved model → models/best_model.pkl

Train/test split → 80/20

🧾 License

MIT License

✍️ Author

Shahul Hussain
B.Tech CSE (AI)


