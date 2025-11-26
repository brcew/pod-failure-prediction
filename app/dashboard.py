import streamlit as st
import joblib
import pandas as pd

# Load model
model = joblib.load("models/best_model.pkl")

st.title("🔮 Pod Failure Prediction Dashboard")
st.write("Enter the pod metrics below to predict if the pod will fail.")

# Input fields
cpu = st.slider("CPU Usage %", 0, 100, 50)
memory = st.slider("Memory Usage %", 0, 100, 50)
leak = st.number_input("Memory Leak Rate", 0.0, 1.0, 0.05)
restarts = st.number_input("Restarts (24h)", 0, 10, 1)
errors = st.number_input("Error Log Rate", 0, 50, 5)
latency = st.number_input("Request Latency (ms)", 0, 500, 100)
replicas = st.number_input("Replica Count", 1, 10, 3)
pressure = st.slider("Node Pressure Score", 0.0, 1.0, 0.5)
autoscaler = st.selectbox("Autoscaler Action", ["scale_up", "scale_down", "none"])
anomaly = st.slider("Prometheus Anomaly Score", 0.0, 1.0, 0.5)
failures = st.number_input("Previous Failures", 0, 10, 2)
uptime = st.number_input("Deployment Uptime (hrs)", 0, 500, 100)

# Button
if st.button("Predict"):
    data = {
        "cpu_usage_pct": cpu,
        "memory_usage_pct": memory,
        "memory_leak_rate": leak,
        "restart_count_24h": restarts,
        "error_log_rate": errors,
        "request_latency_ms": latency,
        "replica_count": replicas,
        "node_pressure_score": pressure,
        "autoscaler_action": autoscaler,
        "prometheus_anomaly_score": anomaly,
        "previous_failures": failures,
        "deployment_uptime_hrs": uptime
    }

    df = pd.DataFrame([data])
    prediction = model.predict(df)[0]

    if prediction == 1:
        st.error("🚨 Pod is LIKELY to FAIL soon!")
    else:
        st.success("✅ Pod is HEALTHY!")
