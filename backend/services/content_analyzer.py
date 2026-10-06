import re


def analyze_content(subject, body):
    """
    Analyze email subject and body for phishing-related indicators.

    Returns:
        score: risk score generated from content
        findings: explanations for detected indicators
    """

    score = 0
    findings = []

    subject = (subject or "").strip()
    body = (body or "").strip()

    # Combine subject and body for analysis
    text = f"{subject} {body}".lower()

    # -----------------------------------------
    # 1. Urgency indicators
    # -----------------------------------------

    urgency_words = [
        "urgent",
        "immediately",
        "as soon as possible",
        "action required",
        "act now",
        "final warning",
        "important",
    ]

    urgency_found = []

    for word in urgency_words:
        if word in text:
            urgency_found.append(word)

    if urgency_found:
        score += 10
        findings.append(
            "Urgency language detected: "
            + ", ".join(urgency_found)
        )

    # -----------------------------------------
    # 2. Credential requests
    # -----------------------------------------

    credential_words = [
        "password",
        "username",
        "login",
        "credentials",
        "verify your account",
        "account verification",
        "security verification",
        "otp",
    ]

    credential_found = []

    for word in credential_words:
        if word in text:
            credential_found.append(word)

    if credential_found:
        score += 20
        findings.append(
            "Credential/account information request detected: "
            + ", ".join(credential_found)
        )

    # -----------------------------------------
    # 3. Financial/payment requests
    # -----------------------------------------

    financial_words = [
        "payment",
        "invoice",
        "bank account",
        "credit card",
        "debit card",
        "refund",
        "transaction",
        "payment information",
    ]

    financial_found = []

    for word in financial_words:
        if word in text:
            financial_found.append(word)

    if financial_found:
        score += 15
        findings.append(
            "Financial or payment-related language detected: "
            + ", ".join(financial_found)
        )

    # -----------------------------------------
    # 4. Threat / fear language
    # -----------------------------------------

    threat_words = [
        "suspended",
        "blocked",
        "locked",
        "terminated",
        "closed",
        "legal action",
        "penalty",
    ]

    threat_found = []

    for word in threat_words:
        if word in text:
            threat_found.append(word)

    if threat_found:
        score += 10
        findings.append(
            "Threat or fear-based language detected: "
            + ", ".join(threat_found)
        )

    # -----------------------------------------
    # 5. Generic greeting
    # -----------------------------------------

    generic_greetings = [
        "dear customer",
        "dear user",
        "dear member",
        "hello user",
        "dear sir",
        "dear madam",
    ]

    greeting_found = []

    for greeting in generic_greetings:
        if greeting in text:
            greeting_found.append(greeting)

    if greeting_found:
        score += 5
        findings.append(
            "Generic greeting detected: "
            + ", ".join(greeting_found)
        )

    # -----------------------------------------
    # 6. Multiple exclamation marks
    # -----------------------------------------

    if re.search(r"!{2,}", subject):
        score += 5
        findings.append(
            "Subject contains multiple exclamation marks."
        )

    # -----------------------------------------
    # 7. Excessive uppercase letters
    # -----------------------------------------

    letters = [char for char in subject if char.isalpha()]

    if len(letters) >= 10:
        uppercase_count = sum(
            char.isupper() for char in subject
        )

        uppercase_ratio = uppercase_count / len(letters)

        if uppercase_ratio >= 0.7:
            score += 5
            findings.append(
                "Subject contains an unusually high amount "
                "of uppercase text."
            )

    return {
        "score": min(score, 100),
        "findings": findings
    }