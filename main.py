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
        "url": "https://consumeraffairs.gov.in/"
    },
    "consumer_protection": {
        "name": "Department of Consumer Affairs",
        "url": "https://consumeraffairs.nic.in/"
    },
    "food": {
        "name": "Food Safety and Standards Authority of India",
        "url": "https://www.fssai.gov.in/"
    }
}


RISKY_CLAIMS = [
    {
        "phrases": ["100%", "guaranteed", "risk-free", "zero risk","no hidden charges"],
        "category": "Absolute or guarantee claims",
        "reason": "Absolute promises may require strong evidence and clear qualifications.",
        "evidence_needed": (
            "Provide reliable documentation supporting the exact promise, "
            "including any conditions or limitations."
        ),
        "source_keys": ["advertising", "consumer_protection"]
    },
    {
        "phrases": ["no.1", "number one", "#1", "best","India's best"],
        "category": "Superiority claims",
        "reason": "Claims of being the best or number one need clear criteria and comparison evidence.",
        "evidence_needed": (
            "Provide the comparison method, relevant competitors, "
            "measurement criteria, and date of the supporting data."
        ),
        "source_keys": ["advertising", "consumer_protection"]
    },
    {
        "phrases": ["clinically proven", "scientifically proven","boosts immunity"],
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
        "phrases": ["organic", "chemical-free", "100% natural","eco-friendly"],
        "category": "Product composition claims",
        "reason": "Composition and natural-product claims should be supported by verifiable product information.",
        "evidence_needed": (
            "Provide ingredient information, relevant certifications or "
            "test results, and evidence supporting the exact wording."
        ),
        "source_keys": ["advertising", "food"]
    },
    {
        "phrases": ["limited time", "only today"],
        "category": "Price or urgency claims",
        "reason": "Price comparisons and urgency statements need accurate, verifiable context.",
        "evidence_needed": (
            "Provide the offer dates, applicable terms, and records supporting "
            "the stated price or comparison."
        ),
        "source_keys": ["advertising", "consumer_protection"]
    },
    {
    "phrases": ["lowest price", "lowest ever price"],
    "category": "Price Comparison Claims",
    "reason": "Lowest-price claims imply that an offer is cheaper than competing or available alternatives. Without reliable, current comparisons and clear conditions, the claim may mislead consumers.",
    "evidence_needed": (
        "Provide dated price comparisons, the relevant market or competitors, "
        "the comparison period, and any conditions or exclusions."
    ),
    "source_keys": ["advertising", "consumer_protection"]
},
{
    "phrases": ["doctor approved", "doctor recommended", "doctor certified"],
    "category": "Medical Endorsement Claims",
    "reason": "Medical endorsement claims may imply professional approval or recommendation without sufficient proof of the endorsement or its scope.",
    "evidence_needed": (
        "Provide verifiable endorsement records, the qualified professional's credentials, "
        "the scope of approval, and any relevant disclosures."
    ),
    "source_keys": ["advertising", "consumer_protection"]
},
{
    "phrases": ["24/7", "24 hours a day", "round-the-clock"],
    "category": "Continuous Availability Claims",
    "reason": "These phrases imply continuous service or support. Limited operating hours, outages, or response delays may make the claim misleading.",
    "evidence_needed": (
        "Provide actual operating hours, service availability records, "
        "and any limitations or exceptions."
    ),
    "source_keys": ["advertising", "consumer_protection"]
},
{
    "phrases": ["limited seats", "limited spots", "limited slots", "few seats left", "only a few seats"],
    "category": "Scarcity and Availability Claims",
    "reason": "Limited availability messaging may create false urgency if the stated capacity restriction is not genuine.",
    "evidence_needed": (
        "State the actual availability or enrolment limit, provide supporting capacity records, "
        "and update availability information when circumstances change."
    ),
    "source_keys": ["advertising", "consumer_protection"]
},
{
    "phrases": ["dream college"],
    "category": "Educational Excellence Claims",
    "reason": "Calling an institution a dream college may create an overly positive impression if the advertisement implies exceptional quality, guaranteed admission, or career outcomes without supporting evidence.",
    "evidence_needed": (
        "Provide verifiable course details, accreditation information, "
        "reliable placement statistics, and evidence for any stated educational outcomes."
    ),
    "source_keys": ["advertising", "consumer_protection"]
},
{
    "phrases": ["zero side effect", "no side effects", "without side effects"],
    "category": "Medical Safety Claims",
    "reason": "Absolute safety claims may imply that a product has no adverse effects for anyone, which requires strong scientific support and may be inappropriate for some medical products.",
    "evidence_needed": (
        "Provide relevant clinical safety data, documented adverse-effect information, "
        "the population studied, and applicable limitations."
    ),
    "source_keys": ["advertising", "consumer_protection"]
},
{
    "phrases": ["clinical tested", "clinically proven"],
    "category": "Clinical Evidence Claims",
    "reason": "Clinical testing or proof claims imply scientific evaluation. They may mislead if the studies are missing, unsuitable, unreliable, or do not support the advertised outcome.",
    "evidence_needed": (
        "Provide the relevant study or trial records, methodology, study population, "
        "results, and evidence that supports the specific advertised claim."
    ),
    "source_keys": ["advertising", "consumer_protection"]
},
{
    "phrases": ["risk free", "zero risk"],
    "category": "Risk and Safety Claims",
    "reason": "Risk-free claims imply that no meaningful risk exists, which may be misleading if risks, conditions, or exclusions apply.",
    "evidence_needed": (
        "Identify the risks assessed, provide supporting evidence, "
        "and disclose material limitations, conditions, and exclusions."
    ),
    "source_keys": ["advertising", "consumer_protection"]
},
{
    "phrases": ["best", "the best", "best in class"],
    "category": "Superiority Claims",
    "reason": "Superiority claims may imply that a product or service outperforms alternatives without clear criteria or reliable comparative evidence.",
    "evidence_needed": (
        "Define the comparison criteria and provide reliable, current evidence "
        "supporting the stated superiority and relevant comparison group."
    ),
    "source_keys": ["advertising", "consumer_protection"]
},
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