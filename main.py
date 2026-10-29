from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from pathlib import Path
from pydantic import BaseModel, Field

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


class AdRequest(BaseModel):
    text: str = Field(max_length=10000)


# These are starting points for human verification,
# not proof that an advertising claim is true or false.
SOURCES = {
    "advertising": {
        "name": "Advertising Standards Council of India",
        "url": "https://www.ascionline.in/"
    },
    "consumer_protection": {"name": "Department of Consumer Affairs", "url": "https://consumeraffairs.gov.in/"},
    "food": {
        "name": "Food Safety and Standards Authority of India",
        "url": "https://www.fssai.gov.in/"
    }
}


RISKY_CLAIMS = [
    {
        "phrases": ["100%", "guaranteed", "risk-free", "zero risk"],
        "category": "Absolute or guarantee claims",
        "reason": "Absolute promises may require strong evidence and clear qualifications.",
        "evidence_needed": (
            "Provide reliable documentation supporting the exact promise, "
            "including any conditions or limitations."
        ),
        "source_keys": ["advertising", "consumer_protection"]
    },
    {
        "phrases": ["no.1", "number one", "#1", "best"],
        "category": "Superiority claims",
        "reason": "Claims of being the best or number one need clear criteria and comparison evidence.",
        "evidence_needed": (
            "Provide the comparison method, relevant competitors, "
            "measurement criteria, and date of the supporting data."
        ),
        "source_keys": ["advertising", "consumer_protection"]
    },
    {
        "phrases": ["clinically proven", "scientifically proven", "doctor recommended"],
        "category": "Scientific or medical claims",
        "reason": "Scientific and medical claims need appropriate supporting evidence.",
        "evidence_needed": (
            "Provide relevant research, study details, and evidence that "
            "supports the specific product and wording."
        ),
        "source_keys": ["advertising", "consumer_protection"]
    },
    {
        "phrases": ["cures", "miracle cure", "permanent cure"],
        "category": "Treatment or cure claims",
        "reason": "Treatment and cure claims need careful verification and may be subject to additional rules.",
        "evidence_needed": (
            "Provide credible evidence for the specific treatment claim "
            "and have an authorised reviewer check applicable requirements."
        ),
        "source_keys": ["advertising", "consumer_protection"]
    },
    {
        "phrases": ["organic", "chemical-free", "100% natural"],
        "category": "Product composition claims",
        "reason": "Composition and natural-product claims should be supported by verifiable product information.",
        "evidence_needed": (
            "Provide ingredient information, relevant certifications or "
            "test results, and evidence supporting the exact wording."
        ),
        "source_keys": ["advertising", "food"]
    },
    {
        "phrases": ["limited time", "only today", "lowest price"],
        "category": "Price or urgency claims",
        "reason": "Price comparisons and urgency statements need accurate, verifiable context.",
        "evidence_needed": (
            "Provide the offer dates, applicable terms, and records supporting "
            "the stated price or comparison."
        ),
        "source_keys": ["advertising", "consumer_protection"]
    }
]


@app.post("/analyze")
def analyze_ad(request: AdRequest):
    ad_text = request.text.strip()

    if not ad_text:
        return {
            "project": "ON-BRAND AI",
            "message": "Enter advertisement text before starting a review.",
            "findings": [],
            "note": "No claim was reviewed because the text was empty."
        }

    text_lower = ad_text.lower()
    findings = []

    for rule in RISKY_CLAIMS:
        matched_phrases = [
            phrase for phrase in rule["phrases"]
            if phrase in text_lower
        ]

        if matched_phrases:
            findings.append({
                "claim": ", ".join(matched_phrases),
                "category": rule["category"],
                "reason": rule["reason"],
                "evidence_needed": rule["evidence_needed"],
                "evidence_status": "Needs human verification",
                "source_links": [
                    SOURCES[key]
                    for key in rule["source_keys"]
                ]
            })

    return {
        "project": "ON-BRAND AI",
        "message": (
            "Potentially risky claims were identified for review."
            if findings
            else "No configured risky phrases were detected. "
                 "This does not establish that the advertisement is compliant."
        ),
        "findings": findings,
        "note": (
            "This is a preliminary screening tool. Source links are "
            "starting points for research, not proof that a claim is true "
            "or false. A human reviewer must assess the actual evidence."
        )
    }