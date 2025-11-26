import joblib
import pandas as pd

# Load the trained model
model = joblib.load("models/best_model.pkl")
print("Model loaded successfully!\n")

def get_user_input():
    print("Enter pod metrics:\n")

    data = {
        "cpu_usage_pct": float(input("CPU Usage %: ")),
        "memory_usage_pct": float(input("Memory Usage %: ")),
        "memory_leak_rate": float(input("Memory Leak Rate: ")),
        "restart_count_24h": int(input("Restart Count (24h): ")),
        "error_log_rate": int(input("Error Log Rate: ")),
        "request_latency_ms": float(input("Request Latency (ms): ")),
        "replica_count": int(input("Replica Count: ")),
        "node_pressure_score": float(input("Node Pressure Score: ")),
        "autoscaler_action": input("Autoscaler Action (scale_up / scale_down / none): "),
        "prometheus_anomaly_score": float(input("Prometheus Anomaly Score: ")),
        "previous_failures": int(input("Previous Failures: ")),
        "deployment_uptime_hrs": float(input("Deployment Uptime (hours): "))
    }

    return pd.DataFrame([data])


# Get user input
df = get_user_input()

# Predict
prediction = model.predict(df)[0]

print("\nPrediction Result:")
if prediction == 1:
    print("⚠️ Pod is LIKELY to FAIL soon!")
else:
    print("✅ Pod is Healthy.")
