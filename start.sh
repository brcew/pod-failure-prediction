#!/bin/bash
uvicorn api.main:app --host 0.0.0.0 --port 8000 &
streamlit run app/dashboard.py --server.address 0.0.0.0 --server.port 8501
