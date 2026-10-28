ON-BRAND AI — Trust Every Claim

ON-BRAND AI is a web-based advertising claim review prototype that helps users identify potentially risky marketing phrases, understand why they may need supporting evidence, and consider safer alternative wording.

The project supports evidence-aware advertising review and human decision-making. It does not independently verify whether a claim is true or legally compliant.

Features

- Advertisement analysis: Submit advertising text for analysis.
- Claim detection: Identify configured phrases such as "100%", "guaranteed", "number one", "best", and "risk-free".
- Explanations: Display reasons why a flagged phrase may require evidence.
- Safer wording suggestions: Offer alternative wording for human consideration.
- Human review: Record a reviewer decision and comments.
- Review history: Display saved demo review records.
- Workspace statistics: Display advertisement checks, flagged phrases, and saved reviews.
- Responsive interface: Use the application on desktop and mobile screens.

Technology Stack

- Frontend: HTML, CSS, JavaScript
- Backend: Python, FastAPI
- API server: Uvicorn
- Data storage: Browser localStorage for demo check statistics and review records

Project Structure

on-brand-ai/
├── index.html
├── main.py
├── requirements.txt
├── .gitignore
└── README.md

Run the Project Locally

1. Clone the repository

git clone https://github.com/BRUNDA541/on-brand-ai.git
cd on-brand-ai

2. Create a virtual environment

python -m venv .venv

3. Activate the environment on Windows

.venv\Scripts\Activate.ps1

If PowerShell blocks activation, use Command Prompt:

.venv\Scripts\activate.bat

4. Install dependencies

pip install -r requirements.txt

5. Start the FastAPI server

uvicorn main:app --reload

The local application should be available at:

http://127.0.0.1:8000

FastAPI interactive API documentation:

http://127.0.0.1:8000/docs

Keep the terminal running while testing the application.

API Endpoints

GET /

Serves the frontend application.

GET /health

Returns a health status for the backend.

POST /analyze

Accepts advertising text as JSON and returns configured claim matches with explanations.

Example request:

{
  "text": "We guarantee 100% success for every customer."
}

The response includes the project name, a review message, detected phrases, and reasons for review.

Testing Checklist

- Open the deployed application.
- Submit advertising text containing configured phrases.
- Verify that claim alerts and suggested wording appear.
- Submit text without configured phrases.
- Try submitting empty text.
- Save a human-review decision and check the review history.
- Refresh the page and check whether saved browser records remain.
- Test the interface on desktop and mobile.
- Check the backend health endpoint.
- Verify that the frontend can communicate with the deployed backend.

Limitations

- Claim detection currently uses configured phrase matching, not independent fact-checking.
- A flagged phrase is not proof that a claim is false.
- An unflagged advertisement is not necessarily accurate or compliant.
- Review history and check statistics are stored in the browser, not in a shared database.
- OCR-based advertisement image text extraction must be implemented and tested before it can be claimed as a working feature.

Architecture

User → HTML/CSS/JavaScript frontend → FastAPI backend → Phrase-matching analysis → Results and explanations → Human review → Browser-local demo history.

Future Development

- Add OCR-based text extraction from advertisement images.
- Improve claim detection and evidence-management workflows.
- Introduce persistent, shared database storage.
- Add authenticated reviewer roles and collaboration.
- Expand automated testing and deployment monitoring.

Live Project

https://on-brand-ai.onrender.com

Source Code

https://github.com/BRUNDA541/on-brand-ai

Disclaimer

ON-BRAND AI is a prototype intended to support responsible advertising review. It does not replace evidence verification, qualified human judgement, or legal advice.