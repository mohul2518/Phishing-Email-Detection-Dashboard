import pandas as pd
import joblib

from pathlib import Path

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score, classification_report


# --------------------------------
# File paths
# --------------------------------

BASE_DIR = Path(__file__).resolve().parent.parent

DATA_FILE = (
    BASE_DIR
    / "data"
    / "phishing_email_dataset.csv"
)

MODEL_FILE = (
    BASE_DIR
    / "models"
    / "phishing_model.pkl"
)


# --------------------------------
# Load dataset
# --------------------------------

print("Loading dataset...")

df = pd.read_csv(DATA_FILE)

print("Dataset loaded successfully!")
print("Number of records:", len(df))


# --------------------------------
# Prepare text
# --------------------------------

df["text"] = (
    df["sender"].fillna("")
    + " "
    + df["subject"].fillna("")
    + " "
    + df["body"].fillna("")
    + " "
    + df["urls"].fillna("")
    + " "
    + df["attachment"].fillna("")
)


X = df["text"]
y = df["label"]


# --------------------------------
# Split dataset
# --------------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)


print("Training records:", len(X_train))
print("Testing records:", len(X_test))


# --------------------------------
# Create ML pipeline
# --------------------------------

model = Pipeline(
    [
        (
            "tfidf",
            TfidfVectorizer(
                lowercase=True,
                stop_words="english",
                ngram_range=(1, 2)
            )
        ),
        (
            "classifier",
            LogisticRegression(
                max_iter=1000
            )
        )
    ]
)


# --------------------------------
# Train model
# --------------------------------

print("\nTraining model...")

model.fit(X_train, y_train)

print("Model training completed!")


# --------------------------------
# Evaluate model
# --------------------------------

predictions = model.predict(X_test)

accuracy = accuracy_score(
    y_test,
    predictions
)

print("\n========== MODEL RESULTS ==========")

print(
    f"Accuracy: {accuracy:.2f}"
)

print("\nClassification Report:")

print(
    classification_report(
        y_test,
        predictions,
        target_names=[
            "Legitimate",
            "Phishing"
        ]
    )
)


# --------------------------------
# Save model
# --------------------------------

joblib.dump(
    model,
    MODEL_FILE
)

print("===================================")
print("Model saved successfully!")
print("Location:", MODEL_FILE)