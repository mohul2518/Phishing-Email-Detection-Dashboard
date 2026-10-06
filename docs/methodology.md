# Project Methodology

## Step 1: Dataset Generation

A synthetic dataset containing legitimate and phishing-style email
examples is generated for the project.

Each record contains:

- Sender
- Subject
- Body
- URLs
- Attachment
- Label

Labels are:

- 0 = Legitimate
- 1 = Phishing

## Step 2: Data Preparation

Email fields are combined into text features for machine-learning
classification.

## Step 3: Feature Extraction

TF-IDF is used to convert email text into numerical features.

Unigrams and bigrams are considered by the model.

## Step 4: Model Training

A Logistic Regression classifier is trained using the generated dataset.

The dataset is divided into training and testing portions.

## Step 5: Rule-Based Analysis

The application separately analyzes:

- Sender
- Content
- URLs
- Attachments

Each analyzer produces a score and security findings.

## Step 6: Risk Calculation

The rule-based score and ML phishing probability are combined by the
risk engine.

## Step 7: Result Generation

The system produces:

- Overall risk score
- Risk classification
- ML prediction
- Component scores
- Findings
- Recommendations

## Step 8: Dashboard Display

The Streamlit application displays the analysis results in an interactive
dashboard.