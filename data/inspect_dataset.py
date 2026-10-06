import pandas as pd
from pathlib import Path


# Find our dataset
DATA_FILE = Path(__file__).parent / "phishing_email_dataset.csv"


# Load dataset
df = pd.read_csv(DATA_FILE)


print("\n========== DATASET INFORMATION ==========\n")

print("Number of rows:", len(df))
print("Number of columns:", len(df.columns))

print("\nColumns:")
print(df.columns.tolist())

print("\nFirst 5 records:")
print(df.head())

print("\nMissing values:")
print(df.isnull().sum())

print("\nLabel distribution:")
print(df["label"].value_counts())

print("\nLabel meaning:")
print("0 = Legitimate")
print("1 = Phishing")