ON-BRAND AI — Trust Every Claim

ON-BRAND AI is a web-based advertising claim review prototype that helps users identify potentially risky marketing phrases, understand why they may require supporting evidence, and consider safer alternative wording.

It supports evidence-aware advertising review and human decision-making. It does not independently verify whether a claim is true or legally compliant.

Features

- Advertisement analysis: Submit advertising text for analysis.
- Claim detection: Identify configured phrases such as "100%", "guaranteed", "number one", "best", and "risk-free".
- Explanations: Understand why flagged phrases may require evidence.
- Safer wording suggestions: Consider alternative wording.
- Evidence-aware review: Display evidence status, evidence requirements, and relevant research links where available.
- Image-based OCR: Upload advertisement images and extract text for analysis using Tesseract.js.
- Human review: Record reviewer decisions and comments.
- Review validation: Require a reviewer comment before saving a review.
- Review history: Display saved decisions, comments, advertisement text, and timestamps.
- Review management: Clear saved review history.
- Workspace statistics: Display advertisement checks, flagged phrases, and saved reviews.
- Responsive interface: Designed for desktop and mobile screens.

Technology Stack

- Frontend: HTML, CSS, JavaScript
- Backend: Python, FastAPI
- API server: Uvicorn
- OCR: Tesseract.js
- Demo storage: Browser localStorage

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

PowerShell:

.venv\Scripts\Activate.ps1

If PowerShell blocks activation, use Command Prompt:

.venv\Scripts\activate.bat

4. Install dependencies

pip install -r requirements.txt

5. Start the FastAPI server

uvicorn main:app --reload

Open the application at:

http://127.0.0.1:8000

FastAPI interactive documentation:

http://127.0.0.1:8000/docs

Health endpoint:

http://127.0.0.1:8000/health

Keep the terminal running while testing.

OCR note: Image text extraction uses Tesseract.js in the browser and may require an internet connection to load its library and language data.

API Endpoints

GET /

Serves the frontend application.

GET /health

Returns the backend health status.

POST /analyze

Accepts advertising text as JSON and returns configured claim matches and explanations.

Example request:

{
  "text": "We guarantee 100% success for every customer."
}

The response includes detected phrases, categories, explanations, evidence information, and suggested review guidance.

Architecture

                 USER
                   |
                   v
          HTML / CSS / JavaScript
                   |
          +--------+--------+
          |                 |
          v                 v
      Text Input        Image Upload
          |                 |
          |              Tesseract.js
          |                 |
          +--------+--------+
                   |
                   v
             Extracted Text
                   |
                   v
             FastAPI Backend
                   |
                   v
          Configured Phrase Matching
                   |
                   v
         Results and Evidence Guidance
                   |
                   v
             Human Reviewer
                   |
          Decision and Comment
                   |
                   v
          Browser localStorage
              Review History

Testing Checklist

- Submit advertising text containing configured phrases.
- Verify claim alerts and safer wording suggestions.
- Submit text without configured phrases.
- Test empty text input.
- Upload an advertisement image and extract text.
- Test uppercase, lowercase, and mixed-case claims.
- Save a reviewer decision with a comment.
- Verify that empty reviewer comments are rejected.
- Check review history and timestamps.
- Refresh the page and verify saved records remain.
- Clear review history and verify records disappear.
- Test the interface on desktop and mobile.
- Check the backend health endpoint.
- Verify frontend-to-backend communication.

Limitations

- Claim detection uses configured phrase matching, not independent fact-checking.
- A flagged phrase is not proof that a claim is false.
- An unflagged advertisement is not necessarily accurate or compliant.
- OCR accuracy depends on image quality, text clarity, and language support.
- Review history and statistics are stored in browser localStorage, not in a shared database.
- Review decisions are demo records, not legal approval or independent claim verification.

Future Development Roadmap

- Introduce persistent shared database storage.
- Add authenticated reviewer roles and team collaboration.
- Improve claim detection and evidence-management workflows.
- Expand OCR language support and image-processing capabilities.
- Add automated testing and deployment monitoring.
- Improve review history, auditability, and reporting.

Live Project

https://on-brand-ai.onrender.com

Source Code

https://github.com/BRUNDA541/on-brand-ai

Disclaimer

ON-BRAND AI is a prototype intended to support responsible advertising review. It does not replace evidence verification, qualified human judgement, or legal advice.