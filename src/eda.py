import pandas as pd

# Load dataset
df = pd.read_csv("data/pod_failure_prediction_dataset.csv")

print("\n===== BASIC INFO =====")
print(df.info())

print("\n===== FIRST 5 ROWS =====")
print(df.head())

print("\n===== SUMMARY STATISTICS =====")
print(df.describe())

print("\n===== CHECK FOR MISSING VALUES =====")
print(df.isnull().sum())

print("\n===== TARGET DISTRIBUTION =====")
print(df["predicted_pod_failure"].value_counts())
