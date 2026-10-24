from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

app = FastAPI(title="ON-BRAND AI")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def home():
    return FileResponse(BASE_DIR / "index.html")


@app.get("/health")
def health_check():
    return {
        "status": "working",
        "project": "ON-BRAND AI"
    }

from pydantic import BaseModel

class AdRequest(BaseModel):
    text: str

@app.post("/analyze")
def analyze_ad(request: AdRequest):
    ad_text = request.text
    risky_phrases = {
        "100%": "Absolute claims need strong supporting evidence.",
        "guaranteed": "Guarantees may mislead people if outcomes aren't assured.",
        "no.1": "A number-one claim needs reliable comparative evidence.",
        "best": "A 'best' claim needs clear supporting criteria.",
        "risk-free": "Risk-free claims need careful evidence and review."
    }

    findings = []

    for phrase, reason in risky_phrases.items():
        if phrase in ad_text.lower():
            findings.append({
                "claim": phrase,
                "reason": reason
            })

    return {
        "project": "ON-BRAND AI",
        "message": "Review these claims before publishing.",
        "findings": findings,
        "note": "This is a preliminary review, not legal advice or proof that a claim is false."
    }