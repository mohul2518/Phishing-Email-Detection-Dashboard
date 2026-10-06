# Phishing Email Detection Dashboard

## 1. Introduction

Phishing emails are messages designed to deceive users into revealing
sensitive information or interacting with potentially harmful content.

This project provides a dashboard that analyzes email characteristics
and identifies potential phishing indicators.

## 2. Objective

The objective of the project is to develop an educational cybersecurity
system capable of analyzing:

- Sender information
- Email content
- URLs
- Attachments
- Machine-learning patterns

The system produces a risk score and explains the indicators detected.

## 3. Detection Approach

The system uses two complementary approaches.

### Rule-Based Analysis

The system checks for predefined security indicators such as:

- Suspicious sender patterns
- Urgency language
- Credential requests
- Financial requests
- Threatening language
- Suspicious URLs
- Potentially risky attachment extensions

### Machine Learning

A machine-learning model uses TF-IDF text features and Logistic Regression
to classify email text into phishing or legitimate categories.

## 4. Risk Engine

The risk engine combines the rule-based analysis and machine-learning
result to calculate a final risk score.

The final result includes:

- Risk score
- Risk classification
- Security findings
- Recommendations
- Machine-learning prediction

## 5. Dashboard

The Streamlit dashboard allows users to:

1. Enter email information.
2. Analyze the email.
3. View the risk score.
4. View individual security signals.
5. View ML prediction probabilities.
6. Review detected findings.
7. Review security recommendations.
8. View analysis history.

## 6. Technology Stack

- Python
- FastAPI
- Streamlit
- Scikit-learn
- Pandas
- Joblib
- Pytest

## 7. Safety

The project uses synthetic and fictional data for educational and
authorized cybersecurity analysis.

Suspicious URLs are analyzed statically and are not automatically visited.

Attachments are analyzed using filenames and extensions rather than
executing files.