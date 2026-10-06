import joblib
from pathlib import Path


# --------------------------------
# Model path
# --------------------------------

BASE_DIR = Path(__file__).resolve().parent.parent

MODEL_FILE = (
    BASE_DIR
    / "models"
    / "phishing_model.pkl"
)


# --------------------------------
# Load model
# --------------------------------

model = joblib.load(MODEL_FILE)


# --------------------------------
# Predict email
# --------------------------------

def predict_email(
    sender,
    subject,
    body,
    urls=None,
    attachment=""
):
    if urls is None:
        urls = []

    # Combine email information
    text = (
        (sender or "")
        + " "
        + (subject or "")
        + " "
        + (body or "")
        + " "
        + " ".join(urls)
        + " "
        + (attachment or "")
    )

    # Prediction
    prediction = model.predict([text])[0]

    # Probability
    probabilities = model.predict_proba([text])[0]

    phishing_probability = probabilities[1]

    legitimate_probability = probabilities[0]

    if prediction == 1:
        classification = "PHISHING"
    else:
        classification = "LEGITIMATE"

    return {
        "prediction": int(prediction),
        "classification": classification,
        "phishing_probability": round(
            float(phishing_probability) * 100,
            2
        ),
        "legitimate_probability": round(
            float(legitimate_probability) * 100,
            2
        )
    }


# --------------------------------
# Test model
# --------------------------------

if __name__ == "__main__":

    result = predict_email(
        sender="security-alert@account-check.invalid.test",
        subject="URGENT: Verify Your Account Immediately",
        body=(
            "Your account requires immediate verification. "
            "Please verify your account information immediately."
        ),
        urls=[
            "http://198.51.100.10/verify-account"
        ],
        attachment="security_update.exe"
    )

    print("\n========== ML PREDICTION ==========")

    print(
        "Prediction:",
        result["classification"]
    )

    print(
        "Phishing Probability:",
        f"{result['phishing_probability']}%"
    )

    print(
        "Legitimate Probability:",
        f"{result['legitimate_probability']}%"
    )