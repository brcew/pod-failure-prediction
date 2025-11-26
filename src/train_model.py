import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

# 1. Load dataset
df = pd.read_csv("data/pod_failure_prediction_dataset.csv")

# 2. Drop columns we cannot use
df = df.drop(columns=["pod_id", "timestamp"])

# 3. Separate features and target
X = df.drop(columns=["predicted_pod_failure"])
y = df["predicted_pod_failure"]

# 4. Identify columns
categorical_cols = ["autoscaler_action"]
numerical_cols = [col for col in X.columns if col not in categorical_cols]

# 5. Preprocessing setup
preprocessor = ColumnTransformer(
    transformers=[
        ("num", StandardScaler(), numerical_cols),
        ("cat", OneHotEncoder(handle_unknown="ignore"), categorical_cols)
    ]
)

# 6. Build ML Pipeline
model = Pipeline(steps=[
    ("preprocessor", preprocessor),
    ("classifier", LogisticRegression(max_iter=300))
])

# 7. Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# 8. Train model
model.fit(X_train, y_train)

# 9. Predict
y_pred = model.predict(X_test)

# 10. Evaluate
print("\n===== MODEL PERFORMANCE =====")
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Precision:", precision_score(y_test, y_pred))
print("Recall:", recall_score(y_test, y_pred))
print("F1 Score:", f1_score(y_test, y_pred))

# 11. Save model permanently
import joblib
joblib.dump(model, "models/best_model.pkl")

print("\nModel saved successfully as models/best_model.pkl")
