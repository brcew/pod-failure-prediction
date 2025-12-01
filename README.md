# 🚀 Pod Failure Prediction System

A full Machine Learning + FastAPI + Streamlit project that predicts whether a Kubernetes pod will fail soon or stay healthy.

🔗 **LIVE DEMO (Render Deployment)**  
👉 https://pod-failure-prediction-1.onrender.com  

Anyone in the world can open this link and use your project.

---

## 📌 What This Project Does (Simple Explanation)

This system takes pod metrics like:

- CPU usage
- Memory usage
- Restart count
- Autoscaler action
- Node pressure
- Anomaly score  
…and predicts:

```
1 → Pod will FAIL soon  
0 → Pod is HEALTHY  
```

---

# ✨ Features

- ✔ Machine Learning model (Logistic Regression pipeline)  
- ✔ FastAPI backend  
- ✔ Streamlit dashboard (dark purple theme)  
- ✔ Hosted & globally accessible on Render  
- ✔ Clean folder structure  
- ✔ Easy for beginners to understand  
- ✔ Real-time prediction  

---

# ▶️ How to Run Locally (if someone wants to)

### 🟣 Start API
```
uvicorn api.main:app --reload
```

Now open API docs:  
👉 http://127.0.0.1:8000/docs

---

### 🟣 Start Dashboard
```
streamlit run app/dashboard.py
```

---

# 🧪 Sample JSON Input (Working Example)

Anyone can send this to `/predict`:

```json
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
```

---

# 📁 Project Structure (simple & clear)

```
pod-failure-prediction/
│── api/
│   └── main.py            → FastAPI backend
│── app/
│   └── dashboard.py       → Streamlit dashboard
│── src/
│   ├── train_model.py     → Trains ML model
│   └── predict.py         → Test predictions
│── models/
│   └── best_model.pkl     → Saved ML model
│── data/
│   └── dataset.csv        → Dataset (optional)
│── assets/
│   └── dashboard.png      → Screenshot
│── examples/
│   └── predict_sample.json
│── .streamlit/
│   └── config.toml        → Dark purple theme
│── Dockerfile             → Deployment
│── README.md              → Project documentation
```

---

# 🧠 Model Details

- Algorithm → Logistic Regression  
- Preprocessing → StandardScaler + OneHotEncoder  
- Saved pipeline → `models/best_model.pkl`  
- Train/Test → 80/20 split  
- Evaluation → accuracy, F1, precision, recall, ROC-AUC 

---

# 🔥 Deployment (Render)

Your global public URL:  
👉 https://pod-failure-prediction-1.onrender.com

Uses:

- Dockerfile  
- Render Web Service  
- Port exposed = 10000  
- Automatically runs FastAPI  

---

# 🧾 License

MIT License

---

# ✍️ Author

**Shahul Hussain**  
B.Tech CSE (AI)

---

# ⭐ If you like the project, give a ⭐ on GitHub!
