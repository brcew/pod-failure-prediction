🚀 Pod Failure Prediction System

Predict Kubernetes pod failures using Machine Learning + FastAPI + Streamlit.

🌟 Overview

This project predicts if a Kubernetes pod is healthy or likely to fail soon based on system metrics such as CPU, memory usage, restart count, node pressure, etc.

It includes:

⚙️ Machine Learning model (Logistic Regression)

🌐 FastAPI backend (/predict endpoint)

🖥️ Streamlit Dashboard

🌍 Live Demo (Global Links)
🔵 Dashboard (Streamlit UI)

👉 https://pod-failure-prediction-1.onrender.com

🟣 API Documentation (FastAPI Swagger UI)

👉 https://pod-failure-prediction-1.onrender.com/docs

Both links work anywhere globally 🌎
(First open may take 30–60 sec because free Render plan sleeps.)

▶️ How to Run Locally
🟣 Start API
uvicorn api.main:app --reload


Open in browser:
👉 http://127.0.0.1:8000/docs

🟣 Start Dashboard
streamlit run app/dashboard.py

🔧 Sample JSON Input

Use this in Swagger UI → /predict:

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

📁 Project Structure
pod-failure-prediction/
├── api/
│   └── main.py
├── app/
│   └── dashboard.py
├── models/
│   └── best_model.pkl
├── src/
│   ├── train_model.py
│   ├── predict.py
│   ├── load_data.py
│   └── eda.py
├── examples/
│   └── predict_sample.json
├── assets/
│   └── dashboard.png
├── requirements.txt
├── Dockerfile
├── start.sh
└── README.md

🧠 Model Details

Algorithm: Logistic Regression

Preprocessing:

StandardScaler

OneHotEncoder

Dataset split: 80% train, 20% test

Model stored at: models/best_model.pkl

📜 License

MIT License

✍️ Author

Shahul Hussain
B.Tech CSE (AI)


