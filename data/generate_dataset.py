import csv
import random
from pathlib import Path


OUTPUT_FILE = (
    Path(__file__).parent
    / "phishing_email_dataset.csv"
)


# ============================================================
# LEGITIMATE EMAIL DATA
# ============================================================

legitimate_emails = [

    {
        "sender": "training@example.org",
        "subject": "Cybersecurity Workshop Reminder",
        "body": (
            "Hello students, this is a reminder about "
            "the cybersecurity workshop scheduled for Friday. "
            "Please attend the session."
        ),
        "urls": "",
        "attachment": "",
        "label": 0
    },

    {
        "sender": "library@example.org",
        "subject": "Library Book Reminder",
        "body": (
            "This is a reminder that your borrowed "
            "library book is due next week."
        ),
        "urls": "",
        "attachment": "",
        "label": 0
    },

    {
        "sender": "events@example.org",
        "subject": "College Event Information",
        "body": (
            "The annual technology event will be held "
            "this Saturday. Please check the event schedule "
            "for details."
        ),
        "urls": "https://example.org/events",
        "attachment": "",
        "label": 0
    },

    {
        "sender": "hr@example.org",
        "subject": "Training Schedule",
        "body": (
            "Please find the updated training schedule "
            "for this month."
        ),
        "urls": "",
        "attachment": "training_schedule.pdf",
        "label": 0
    },

    {
        "sender": "faculty@example.org",
        "subject": "Project Meeting",
        "body": (
            "The project meeting is scheduled for Monday "
            "at 10 AM. Please bring your project notes."
        ),
        "urls": "",
        "attachment": "",
        "label": 0
    },

    {
        "sender": "admin@example.org",
        "subject": "Campus Maintenance Notice",
        "body": (
            "Maintenance work will be carried out "
            "on campus this weekend."
        ),
        "urls": "",
        "attachment": "",
        "label": 0
    },

    {
        "sender": "placement@example.org",
        "subject": "Placement Training Session",
        "body": (
            "Students registered for placement training "
            "should attend the scheduled session."
        ),
        "urls": "https://example.org/placement",
        "attachment": "",
        "label": 0
    },

    {
        "sender": "finance@example.org",
        "subject": "Fee Receipt Available",
        "body": (
            "Your fee receipt is now available in the "
            "student portal."
        ),
        "urls": "https://example.org/student-portal",
        "attachment": "fee_receipt.pdf",
        "label": 0
    }
]


# ============================================================
# PHISHING EMAIL DATA
# ============================================================

phishing_emails = [

    {
        "sender": "security-alert@account-check.invalid.test",
        "subject": "URGENT: Verify Your Account Immediately",
        "body": (
            "Your account requires immediate verification. "
            "Please verify your account information immediately."
        ),
        "urls": "http://198.51.100.10/verify-account",
        "attachment": "",
        "label": 1
    },

    {
        "sender": "billing@payment-warning.invalid.test",
        "subject": "Payment Required Immediately",
        "body": (
            "Your payment could not be processed. "
            "Verify your payment information immediately."
        ),
        "urls": "http://198.51.100.20/payment",
        "attachment": "",
        "label": 1
    },

    {
        "sender": "support@account-check.invalid.test",
        "subject": "Your Account Will Be Suspended",
        "body": (
            "Your account will be suspended unless you "
            "confirm your account information immediately."
        ),
        "urls": "http://198.51.100.30/confirm",
        "attachment": "",
        "label": 1
    },

    {
        "sender": "notification@security.invalid.test",
        "subject": "Important Security Verification",
        "body": (
            "We detected unusual activity. Please verify "
            "your account credentials using the link below."
        ),
        "urls": "http://198.51.100.40/login",
        "attachment": "security_update.exe",
        "label": 1
    },

    {
        "sender": "account@verify-alert.invalid.test",
        "subject": "Final Warning: Account Verification",
        "body": (
            "Your account may be blocked. "
            "Verify your login credentials immediately."
        ),
        "urls": "http://198.51.100.50/verify",
        "attachment": "",
        "label": 1
    },

    {
        "sender": "payment@billing-alert.invalid.test",
        "subject": "Payment Failed - Action Required",
        "body": (
            "Your payment has failed. Please confirm "
            "your payment information to avoid suspension."
        ),
        "urls": "http://198.51.100.60/payment",
        "attachment": "",
        "label": 1
    },

    {
        "sender": "support@login-check.invalid.test",
        "subject": "Verify Your Login",
        "body": (
            "We detected suspicious activity on your account. "
            "Please verify your username and password."
        ),
        "urls": "http://198.51.100.70/login",
        "attachment": "login_update.exe",
        "label": 1
    },

    {
        "sender": "security@account-warning.invalid.test",
        "subject": "Account Security Alert",
        "body": (
            "Your account has been flagged for unusual activity. "
            "Confirm your credentials to prevent account closure."
        ),
        "urls": "http://198.51.100.80/confirm-account",
        "attachment": "",
        "label": 1
    }
]


# ============================================================
# GENERATE DATASET
# ============================================================

def generate_dataset(number_of_rows=1000):

    rows = []

    for _ in range(number_of_rows):

        if random.random() < 0.5:

            template = random.choice(
                legitimate_emails
            )

        else:

            template = random.choice(
                phishing_emails
            )

        rows.append(
            template.copy()
        )


    # Shuffle dataset

    random.shuffle(rows)


    # ========================================================
    # WRITE CSV
    # ========================================================

    fieldnames = [
        "sender",
        "subject",
        "body",
        "urls",
        "attachment",
        "label"
    ]


    with open(
        OUTPUT_FILE,
        "w",
        newline="",
        encoding="utf-8"
    ) as file:

        writer = csv.DictWriter(
            file,
            fieldnames=fieldnames
        )

        writer.writeheader()

        writer.writerows(rows)


    # ========================================================
    # INFORMATION
    # ========================================================

    print(
        "Dataset generated successfully!"
    )

    print(
        f"Location: {OUTPUT_FILE}"
    )

    print(
        f"Number of records: {len(rows)}"
    )


# ============================================================
# RUN
# ============================================================

if __name__ == "__main__":

    generate_dataset(1000)