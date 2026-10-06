# Machine Learning Model Results

## Dataset

The project uses a synthetic dataset containing legitimate and
phishing-style email examples.

The dataset contains the following fields:

- Sender
- Subject
- Body
- URLs
- Attachment
- Label

Where:

- 0 = Legitimate
- 1 = Phishing

## Model

The machine-learning pipeline uses:

- TF-IDF for text feature extraction
- Logistic Regression for classification

The dataset is divided into training and testing portions.

## Evaluation

The model is evaluated using:

- Accuracy
- Precision
- Recall
- F1-score
- Classification report

## Results

The actual model performance values are recorded from the
training output in the terminal.

The model is intended for educational and demonstration purposes.
Because the dataset is synthetically generated, the measured
performance should not be interpreted as real-world phishing
detection accuracy.

## Integration

The trained model is saved as:

models/phishing_model.pkl

The prediction module loads this model and provides:

- Phishing prediction
- Phishing probability
- Legitimate probability

The risk engine combines the machine-learning result with
rule-based security signals.