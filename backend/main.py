from fastapi import FastAPI
from pydantic import BaseModel

from backend.services.risk_engine import analyze_email


app = FastAPI(
    title="Phishing Email Detection API",
    description="API for analyzing emails for phishing indicators",
    version="1.0.0"
)


class EmailRequest(BaseModel):
    sender: str
    subject: str
    body: str
    urls: list[str] = []
    attachment: str = ""


@app.get("/")
def home():
    return {
        "message": "Phishing Email Detection API is running"
    }


@app.post("/analyze")
def analyze(request: EmailRequest):

    result = analyze_email(
    sender=request.sender,
    subject=request.subject,
    body=request.body,
    urls=request.urls,
    attachment=request.attachment
)

    return result