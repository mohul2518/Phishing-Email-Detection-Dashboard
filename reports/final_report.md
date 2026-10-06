# PHISHING EMAIL DETECTION DASHBOARD

## 1. Abstract

Phishing emails are a common cybersecurity threat where attackers
try to trick users into revealing sensitive information or clicking
on suspicious links.

This project develops a Phishing Email Detection Dashboard that
analyzes emails and identifies possible phishing indicators.

The system checks different parts of an email, including the sender,
email content, URLs, and attachments. It uses two approaches:
rule-based analysis and machine learning.

The machine-learning part uses TF-IDF to convert email text into
features and Logistic Regression to classify emails as legitimate
or phishing.

The rule-based system checks for indicators such as urgent language,
credential requests, financial requests, suspicious URLs, and risky
attachment types.

The results from these analyses are combined to produce a risk score
and risk classification. The system also provides detected findings
and security recommendations.

The project uses a Streamlit dashboard for the user interface and
FastAPI for the backend.

This project is developed for educational and authorized
cybersecurity analysis using synthetic data.
## 2. Introduction

Phishing is a type of cyber attack in which attackers use deceptive
emails to trick users into providing sensitive information or
interacting with suspicious content.

Phishing emails may contain suspicious sender addresses, urgent
messages, requests for passwords or payment information, suspicious
URLs, or risky attachments.

This project demonstrates how these different indicators can be
analyzed using a combination of rule-based techniques and machine
learning.

## 3. Problem Statement

Users may find it difficult to identify phishing emails manually
because phishing messages can use different types of deceptive
techniques.

Therefore, there is a need for a system that can examine multiple
parts of an email and provide an understandable indication of
potential risk.

This project addresses this problem by developing a dashboard that
analyzes sender information, email content, URLs, attachments, and
machine-learning patterns.
## 4. Objectives

The main objectives of this project are:

1. To analyze sender information for suspicious characteristics.

2. To analyze email content for phishing-related language.

3. To perform static analysis of URLs.

4. To analyze attachment filenames and extensions.

5. To develop a machine-learning model for email classification.

6. To combine different security signals into a risk score.

7. To provide security findings and recommendations to the user.

8. To develop an interactive dashboard for phishing email analysis.

9. To demonstrate phishing detection techniques using synthetic
   and authorized data.
   ## 5. Existing System

Traditional email security systems may use different techniques
such as spam filtering, URL checking, and rule-based detection.

However, analyzing only one part of an email may not provide a
complete view of the possible security indicators.

## 6. Proposed System

The proposed system combines multiple analysis techniques.

The system analyzes:

- Sender
- Email content
- URLs
- Attachments
- Machine-learning patterns

The analysis results are processed by the risk engine.

The risk engine produces:

- Risk score
- Risk classification
- Security findings
- Recommendations
- Machine-learning prediction


The results are displayed through the Streamlit dashboard.
## 7. System Architecture

The system follows a modular architecture in which the dashboard
communicates with the backend API. The backend sends the email data
to the different analysis modules.

The main components are:

- Streamlit Dashboard
- FastAPI Backend
- Risk Engine
- Sender Analyzer
- Content Analyzer
- URL Analyzer
- Attachment Analyzer
- Machine Learning Module

The overall flow is:

User
↓
Streamlit Dashboard
↓
FastAPI Backend
↓
Risk Engine
↓
Security Analyzers + Machine Learning
↓
Combined Risk Score
↓
Analysis Result
↓
Streamlit Dashboard
                    USER
                      |
                      v
          +-----------------------+
          | Streamlit Dashboard   |
          |       app.py          |
          +-----------+-----------+
                      |
                      v
          +-----------------------+
          | FastAPI Backend       |
          |     backend/main.py   |
          +-----------+-----------+
                      |
                      v
              +---------------+
              | Risk Engine   |
              +-------+-------+
                      |
        +-------------+-------------+
        |             |             |
        v             v             v
     Sender        Content          URL
    Analyzer       Analyzer       Analyzer
        |             |             |
        +-------------+-------------+
                      |
                      v
              Attachment Analyzer
                      |
                      v
              Rule-Based Analysis
                      |
                      v
             Machine Learning Model
                      |
                      v
              Combined Risk Score
                      |
                      v
                Final Result
                      |
                      v
             Streamlit Dashboard

## 8. Methodology

The project follows several steps to analyze an email.

### Step 1: Dataset Generation

A synthetic dataset containing legitimate and phishing-style email
examples is generated.

Each email record contains:

- Sender
- Subject
- Body
- URL
- Attachment
- Label

The labels are:

- 0 = Legitimate
- 1 = Phishing

### Step 2: Data Preparation

The sender, subject, body, URL, and attachment information are
combined to create the text input used by the machine-learning model.

### Step 3: Feature Extraction

TF-IDF is used to convert email text into numerical features that
can be processed by the machine-learning algorithm.

### Step 4: Machine Learning

A Logistic Regression classifier is trained using the generated
dataset.

The dataset is divided into training and testing portions.

### Step 5: Rule-Based Analysis

The system separately analyzes:

- Sender
- Content
- URLs
- Attachments

Each analyzer identifies specific security indicators.

### Step 6: Risk Calculation

The rule-based analysis and machine-learning result are combined
by the risk engine.

### Step 7: Result Generation

The system generates:

- Risk score
- Risk classification
- ML prediction
- Security findings
- Recommendations

### Step 8: Dashboard Display

The final results are displayed through the Streamlit dashboard.
## 9. Dataset

The project uses a synthetic dataset created specifically for
educational and authorized cybersecurity analysis.

The dataset contains examples of both legitimate and phishing-style
emails.

Each record contains the following fields:

| Field | Description |
|---|---|
| Sender | Email sender address |
| Subject | Email subject |
| Body | Email message content |
| URLs | URL present in the email |
| Attachment | Attachment filename |
| Label | Classification of the email |

The labels used are:

- 0 = Legitimate
- 1 = Phishing

The dataset is generated using Python and is stored as:

`data/phishing_email_dataset.csv`

The dataset is used to train and evaluate the machine-learning
model.
## 10. Rule-Based Detection

The rule-based detection system checks different characteristics
of an email.

### Sender Analysis

The sender analyzer checks for suspicious characteristics in the
sender address, including suspicious terms and unusual domain
patterns.

### Content Analysis

The content analyzer checks for indicators such as:

- Urgency language
- Credential requests
- Financial or payment-related language
- Threat or fear-based language
- Generic greetings

### URL Analysis

The URL analyzer performs static analysis of URLs.

It checks characteristics such as:

- HTTP instead of HTTPS
- Raw IP addresses
- Suspicious keywords
- Unusually large numbers of subdomains
- Long URLs
- Suspicious-looking top-level domains

The system does not automatically visit suspicious URLs.

### Attachment Analysis

The attachment analyzer checks attachment filenames and extensions.

Potentially risky file extensions are given additional risk points.

Attachments are analyzed using metadata such as filenames and
extensions rather than being executed.
## 11. Machine Learning Model

The project uses machine learning to classify email examples as
legitimate or phishing.

### TF-IDF

TF-IDF stands for Term Frequency-Inverse Document Frequency.

It converts text into numerical features that can be used by a
machine-learning algorithm.

The project considers individual words and combinations of words
using unigrams and bigrams.

### Logistic Regression

Logistic Regression is used as the classification algorithm.

The model learns patterns from the training dataset and predicts
whether an email belongs to the legitimate or phishing category.

The trained model is saved as:

`models/phishing_model.pkl`

The prediction module provides:

- Prediction
- Phishing probability
- Legitimate probability
## 12. Risk Scoring

The risk engine combines the results from the rule-based analysis
and the machine-learning model.

The rule-based analysis produces scores from:

- Sender analysis
- Content analysis
- URL analysis
- Attachment analysis

The rule-based score and machine-learning phishing probability are
then combined to produce the final risk score.

The system uses the following risk categories:

| Risk Score | Classification |
|---|---|
| 0–20 | LOW RISK |
| 21–40 | MODERATE RISK |
| 41–70 | SUSPICIOUS |
| 71–100 | HIGH RISK |

The final result also contains security findings and recommendations
to help the user understand the detected indicators.
## 13. Implementation

The project is implemented using Python.

### Frontend

Streamlit is used to create the interactive dashboard.

The dashboard allows the user to:

- Enter sender information
- Enter the email subject
- Enter the email body
- Enter a URL
- Enter an attachment filename
- Start the analysis
- View the analysis results
- View analysis history

### Backend

FastAPI is used to create the backend API.

The main API endpoint is:

`POST /analyze`

The endpoint receives the email information and sends it to the
risk engine.

### Security Analysis Modules

The backend contains separate modules for:

- Sender analysis
- Content analysis
- URL analysis
- Attachment analysis
- Risk calculation

This modular structure makes the system easier to understand,
test, and maintain.

### Machine Learning Module

The machine-learning module contains:

- Model training
- Model prediction

The trained model is stored in the `models` directory.

### Testing

## 16. Testing

The project uses Pytest to test the different components of the
phishing email detection system.

The following modules were tested:

- Sender Analyzer
- Content Analyzer
- URL Analyzer
- Attachment Analyzer
- Risk Engine

The tests verify that the individual components correctly identify
different security indicators and produce the expected results.

The complete test suite was executed using:

```powershell
python -m pytest
## 14. Results

The developed system successfully provides an interactive
environment for analyzing email examples.

The dashboard displays:

- Machine-learning prediction
- Phishing probability
- Legitimate probability
- Rule-based score
- Combined risk score
- Risk classification
- Sender security signal
- Content security signal
- URL security signal
- Attachment security signal
- Detected findings
- Security recommendations
- Analysis history

### Phishing Email Test

A synthetic phishing-style email was entered into the dashboard
containing suspicious sender information, urgent language, a
suspicious URL, and a potentially risky attachment.

The system analyzed these indicators and displayed the resulting
risk assessment.

### Legitimate Email Test

A synthetic legitimate email was also entered into the dashboard.

The system analyzed the email and displayed its corresponding
classification and risk information.

### Machine Learning Results

### Machine Learning Results

The dataset contained 1,000 email records.

The dataset was divided into:

- Training records: 800
- Testing records: 200

The machine-learning model achieved an accuracy of 1.00, which
corresponds to 100% accuracy on the test dataset.

The classification results were:

| Class | Precision | Recall | F1-score | Support |
|---|---:|---:|---:|---:|
| Legitimate | 1.00 | 1.00 | 1.00 | 100 |
| Phishing | 1.00 | 1.00 | 1.00 | 100 |

The overall accuracy was:

**Accuracy: 1.00 (100%)**

The macro average and weighted average for precision, recall, and
F1-score were also 1.00.

These results are based on the synthetic dataset used for this
educational project. Since the dataset was generated from predefined
synthetic templates, the 100% test accuracy should not be interpreted
as real-world phishing detection accuracy.

## 15. Screenshots

The following screenshots demonstrate the working of the Phishing Email
Detection Dashboard.

### 15.1 Main Dashboard

The main dashboard provides the interface for entering email
information and starting the analysis.

![Main Dashboard](../screenshots/01_dashboard.png)

### 15.2 Phishing Email Detection

This screenshot shows the analysis of a synthetic phishing-style
email, including the risk score, machine-learning prediction,
security findings, and recommendations.

![Phishing Detection](../screenshots/02_phishing_detection.png)

### 15.3 Legitimate Email Detection

This screenshot shows the analysis of a synthetic legitimate email.

![Legitimate Detection](../screenshots/03_legitimate_detection.png)

### 15.4 Analysis History

The dashboard maintains a history of previously analyzed emails.

![Analysis History](../screenshots/04_analysis_history.png)

## 16. Testing

The project uses Pytest for testing the different components.

The following modules are tested:

- Sender Analyzer
- Content Analyzer
- URL Analyzer
- Attachment Analyzer
- Risk Engine

The tests verify that the individual components correctly identify
different security indicators and produce the expected results.
### Test Result

The complete automated test suite was executed using Pytest.

The test suite completed successfully with all implemented tests
passing.

The exact number of tests passed was recorded from the final Pytest
execution.
The test suite completed successfully with 20 tests passing.

The complete test suite can be executed using:

```powershell
python -m pytest

## 18. Limitations

The project has several limitations.

1. The machine-learning model is trained using synthetic data.

2. The dataset is relatively small and based on predefined
   examples.

3. The model may not perform the same way on real-world phishing
   emails.

4. The URL analyzer performs static analysis and does not visit or
   inspect the actual webpage.

5. Attachment analysis is limited to filenames and extensions.

6. The system does not execute attachments.

7. The machine-learning probability should not be interpreted as a
   calibrated real-world probability.

8. The rule-based indicators cannot identify every possible phishing
   technique.
## 19. Future Scope

The project can be extended in several ways.

### Larger Dataset

A larger and more diverse authorized dataset could be used to
improve the machine-learning component.

### Advanced Machine Learning

Other machine-learning or deep-learning techniques could be
evaluated for comparison.

### Improved URL Analysis

Additional static URL features could be added to improve suspicious
URL detection.

### Improved Attachment Analysis

Additional safe metadata analysis could be added for attachment
assessment.

### Email Integration

The system could potentially be integrated with an authorized email
environment for automated analysis.

### Advanced Dashboard

The dashboard could be extended with charts, statistics, filtering,
and downloadable analysis reports.

### Continuous Model Improvement

The model could be retrained using new authorized examples to
improve its ability to recognize different phishing patterns.
## 20. Conclusion

The Phishing Email Detection Dashboard demonstrates how multiple
security analysis techniques can be combined to identify potential
phishing indicators.

The system analyzes sender information, email content, URLs, and
attachments using rule-based techniques. It also uses TF-IDF and
Logistic Regression for machine-learning classification.

The risk engine combines these results and produces a risk score,
classification, findings, and recommendations.

The Streamlit dashboard provides an easy-to-use interface, while
FastAPI provides the backend API.

The project provides a practical educational demonstration of
phishing email analysis and multi-signal cybersecurity detection.

Since the project uses synthetic data, the results should be
considered demonstrations of the implemented methodology rather
than evidence of real-world phishing detection performance.

## 21. References

1. Python Documentation
2. FastAPI Documentation
3. Streamlit Documentation
4. Scikit-learn Documentation
5. Pandas Documentation
6. Pytest Documentation