# Model Card — Pod Failure Predictor

This file explains the ML model used in this project.

## Model Name
Logistic Regression (simple and good for beginners)

## What the Model Does
It tries to guess:
- 1 → Pod will FAIL soon
- 0 → Pod is healthy

## What Data It Used
It uses pod metrics like:
- CPU %
- Memory %
- Restarts
- Autoscaler action
- Anomaly score

## How Good the Model Is
You can add your accuracy here later.

## Limitations
It is trained on a small dataset.
