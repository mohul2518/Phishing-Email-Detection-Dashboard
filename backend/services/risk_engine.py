from .sender_analyzer import analyze_sender
from .content_analyzer import analyze_content
from .url_analyzer import analyze_url
from .attachment_analyzer import analyze_attachment

from ml.predict import predict_email


def classify_risk(score):
    if score <= 20:
        return "LOW RISK"

    if score <= 40:
        return "MODERATE RISK"

    if score <= 70:
        return "SUSPICIOUS"

    return "HIGH RISK"


def analyze_email(
    sender,
    subject,
    body,
    urls=None,
    attachment=""
):

    if urls is None:
        urls = []

    # --------------------------------
    # Rule-based analysis
    # --------------------------------

    sender_result = analyze_sender(sender)

    content_result = analyze_content(
        subject,
        body
    )

    url_results = []

    for url in urls:

        result = analyze_url(url)

        url_results.append({
            "url": url,
            "score": result["score"],
            "findings": result["findings"]
        })

    attachment_result = analyze_attachment(
        attachment
    )

    # --------------------------------
    # Component scores
    # --------------------------------

    sender_score = sender_result["score"]

    content_score = content_result["score"]

    url_score = min(
        sum(
            result["score"]
            for result in url_results
        ),
        40
    )

    attachment_score = min(
        attachment_result["score"],
        30
    )

    # --------------------------------
    # Rule-based total
    # --------------------------------

    rule_based_score = min(
        sender_score
        + content_score
        + url_score
        + attachment_score,
        100
    )

    # --------------------------------
    # ML prediction
    # --------------------------------

    ml_result = predict_email(
        sender=sender,
        subject=subject,
        body=body,
        urls=urls,
        attachment=attachment
    )

    ml_probability = (
        ml_result["phishing_probability"]
    )

    # --------------------------------
    # Combine rule-based + ML score
    # --------------------------------

    final_score = round(
        (
            rule_based_score * 0.6
        )
        +
        (
            ml_probability * 0.4
        )
    )

    final_score = min(
        final_score,
        100
    )

    classification = classify_risk(
        final_score
    )

    # --------------------------------
    # Findings
    # --------------------------------

    findings = []

    findings.extend(
        sender_result["findings"]
    )

    findings.extend(
        content_result["findings"]
    )

    for result in url_results:

        findings.extend(
            result["findings"]
        )

    findings.extend(
        attachment_result["findings"]
    )

    # --------------------------------
    # ML finding
    # --------------------------------

    if ml_result["prediction"] == 1:

        findings.append(
            "Machine-learning model detected "
            "patterns associated with phishing."
        )

    else:

        findings.append(
            "Machine-learning model did not detect "
            "strong phishing patterns."
        )

    # --------------------------------
    # Recommendations
    # --------------------------------

    if classification in [
        "SUSPICIOUS",
        "HIGH RISK"
    ]:

        recommendations = [
            "Do not click suspicious links.",
            "Do not provide passwords or other credentials.",
            "Verify the sender through a trusted channel.",
            "Report the message if appropriate."
        ]

    else:

        recommendations = [
            "No major phishing indicators were detected."
        ]

    # --------------------------------
    # Final result
    # --------------------------------

    return {

        "risk_score": final_score,

        "classification": classification,

        "components": {

            "sender_score": sender_score,

            "content_score": content_score,

            "url_score": url_score,

            "attachment_score": attachment_score
        },

        "ml_analysis": {

            "prediction":
                ml_result["classification"],

            "phishing_probability":
                ml_result[
                    "phishing_probability"
                ],

            "legitimate_probability":
                ml_result[
                    "legitimate_probability"
                ]
        },

        "rule_based_score":
            rule_based_score,

        "findings":
            findings,

        "recommendations":
            recommendations,

        "url_analysis":
            url_results,

        "attachment_analysis":
            attachment_result
    }