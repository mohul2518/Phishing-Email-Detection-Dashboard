import re
from urllib.parse import urlparse


def analyze_url(url):
    """
    Analyze a URL without opening or visiting it.

    Returns:
        score: risk score
        findings: reasons for the score
    """

    score = 0
    findings = []

    url = (url or "").strip()

    # Empty URL
    if not url:
        return {
            "score": 0,
            "findings": []
        }

    # -----------------------------------------
    # 1. Check URL format
    # -----------------------------------------

    parsed = urlparse(url)

    if not parsed.scheme or not parsed.netloc:
        score += 15
        findings.append("URL does not appear to have a normal structure.")

    # -----------------------------------------
    # 2. HTTP instead of HTTPS
    # -----------------------------------------

    if parsed.scheme.lower() == "http":
        score += 10
        findings.append(
            "URL uses HTTP instead of HTTPS."
        )

    # -----------------------------------------
    # 3. Raw IP address
    # -----------------------------------------

    hostname = parsed.hostname or ""

    ip_pattern = r"^\d{1,3}(\.\d{1,3}){3}$"

    if re.match(ip_pattern, hostname):
        score += 20
        findings.append(
            "URL uses a raw IP address instead of a domain name."
        )

    # -----------------------------------------
    # 4. Suspicious keywords
    # -----------------------------------------

    suspicious_words = [
        "login",
        "verify",
        "verification",
        "account",
        "password",
        "credential",
        "payment",
        "update",
        "confirm",
    ]

    found_words = []

    url_lower = url.lower()

    for word in suspicious_words:
        if word in url_lower:
            found_words.append(word)

    if found_words:
        score += 10
        findings.append(
            "URL contains suspicious keywords: "
            + ", ".join(found_words)
        )

    # -----------------------------------------
    # 5. Excessive subdomains
    # -----------------------------------------

    domain_parts = hostname.split(".")

    if len(domain_parts) > 3:
        score += 10
        findings.append(
            "URL contains an unusually large number of subdomains."
        )

    # -----------------------------------------
    # 6. Very long URL
    # -----------------------------------------

    if len(url) > 100:
        score += 10
        findings.append(
            "URL is unusually long."
        )

    # -----------------------------------------
    # 7. Suspicious TLD
    # -----------------------------------------

    suspicious_tlds = {
        "zip",
        "click",
        "work",
        "country",
        "gq"
    }

    if "." in hostname:
        tld = hostname.split(".")[-1].lower()

        if tld in suspicious_tlds:
            score += 10
            findings.append(
                f"URL uses a suspicious-looking TLD: .{tld}"
            )

    return {
        "score": min(score, 100),
        "findings": findings
    }