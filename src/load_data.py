import pandas as pd

# Load the dataset
df = pd.read_csv("data/pod_failure_prediction_dataset.csv")

# Show the first 5 rows
print("Dataset Loaded Successfully!")
print(df.head())

# Show shape (rows, columns)
print("Shape:", df.shape)

# Show column names
print("\nColumns:")
print(df.columns)
