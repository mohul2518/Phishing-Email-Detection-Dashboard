from pathlib import Path


def analyze_attachment(filename):
    score = 0
    findings = []

    filename = (filename or "").strip()

    # No attachment
    if not filename:
        return {
            "score": 0,
            "findings": []
        }

    extension = Path(filename).suffix.lower()

    # Potentially risky executable/script extensions
    risky_extensions = {
        ".exe",
        ".scr",
        ".bat",
        ".cmd",
        ".com",
        ".msi",
        ".vbs",
        ".js",
        ".ps1"
    }

    if extension in risky_extensions:
        score += 30
        findings.append(
            f"Attachment uses a potentially risky file type: {extension}"
        )

    # Double-extension pattern
    parts = filename.lower().split(".")

    if len(parts) >= 3:
        score += 20
        findings.append(
            "Attachment filename contains multiple file extensions."
        )

    # Suspicious words in filename
    suspicious_words = [
        "invoice",
        "payment",
        "security",
        "update",
        "verify",
        "password",
        "account"
    ]

    found_words = [
        word for word in suspicious_words
        if word in filename.lower()
    ]

    if found_words:
        score += 10
        findings.append(
            "Attachment filename contains suspicious keywords: "
            + ", ".join(found_words)
        )

    return {
        "score": min(score, 100),
        "findings": findings
    }