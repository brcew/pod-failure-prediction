#!/bin/bash

# Run Streamlit dashboard
streamlit run app/dashboard.py --server.port=$PORT --server.address=0.0.0.0

