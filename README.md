# 🚀 Pod Failure Prediction System

![Dashboard Screenshot](assets/dashboard.png)

**Elevator pitch:** Predicts whether a Kubernetes pod will fail soon (1) or is healthy (0) using runtime metrics. FastAPI + Streamlit UI.

---

## ✨ Features
- Predict pod failure using a saved ML pipeline
- REST API (FastAPI) with Pydantic validation
- Interactive Streamlit dashboard for demo
- Clean project structure and dark theme

---

## ▶ Quick start (run locally)

```bash
# clone
git clone https://github.com/brcew/pod-failure-prediction.git
cd pod-failure-prediction

# create and activate virtualenv (Windows)
python -m venv venv
venv\Scripts\activate

# install
pip install -r requirements.txt

# Run API (new terminal)
uvicorn api.main:app --reload

# Run dashboard (new terminal)
streamlit run app/dashboard.py
