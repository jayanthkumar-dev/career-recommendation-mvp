# PathPilot

PathPilot is a premium, multi-page Streamlit web app that provides AI-assisted career recommendations based on user profile inputs.

It is designed as a clean, startup-style MVP with modern UI, explainable recommendation logic, and practical career guidance.

## Key Features

- Multi-page Streamlit experience:
	- Profile Analysis page
	- Career Recommendations page
- Premium SaaS-style UI:
	- Gradient background
	- Glassmorphism cards
	- Interactive hover effects
	- Centered hero section and polished navbar
- Explainable recommendation engine:
	- Input-aware weighted matching
	- Domain-sensitive suggestions (tech, healthcare, finance)
	- Reduced generic fallback bias
- Optional profile enrichment:
	- GitHub URL-based public skill signal extraction
	- LinkedIn URL field for future extension

## Tech Stack

- Python 3.11+
- Streamlit 1.56.0
- Standard library networking (`urllib`) for GitHub public API calls

## How It Works

PathPilot uses weighted matching across:

- Interest
- Industry
- Education
- Skills (manual + optional GitHub-derived signals)

The app then:

1. Scores matching careers
2. Ranks by relevance
3. Returns top recommendations with:
	 - Career overview
	 - Why this career was selected
	 - Development plan
	 - Key skills

## Project Structure

```text
career-recommendation-MVP-main/
|- app.py
|- pathpilot_ui.py
|- pathpilot_utils.py
|- pages/
|  |- 2_Career_Recommendations.py
|- requirements.txt
|- README.md
```

## Setup and Run

1. Clone the repository

```bash
git clone https://github.com/jayanthkumar-dev/career-recommendation-mvp.git
cd career-recommendation-mvp/career-recommendation-MVP-main
```

2. (Recommended) Create and activate a virtual environment

```bash
python -m venv .venv
# Windows PowerShell
.\.venv\Scripts\Activate.ps1
```

3. Install dependencies

```bash
pip install -r requirements.txt
```

4. Start the app

```bash
streamlit run app.py
```

## Input Fields

- Education
- Interest
- Industry
- Skills (comma-separated)
- GitHub URL (optional)
- LinkedIn URL (optional)

## Notes

- This project is Python-only (no Node.js backend, no JS frontend).
- GitHub analysis uses public profile/repository metadata only.
- LinkedIn auto-parsing is not enabled in this MVP.

## Roadmap

- LinkedIn summary parsing (safe/manual-assisted)
- Recommendation confidence explanation panel
- Export recommendations to PDF
- User history and saved profiles

## License

This project is currently provided as an MVP. Add a formal license file (`LICENSE`) for production/open-source distribution.
