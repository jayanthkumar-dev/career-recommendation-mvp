# 🧭 PathPilot – Career Recommendation System

A smart, rule-based career recommendation web app built with **Python** and **Streamlit**.
PathPilot guides students and early-career professionals toward their ideal career path by
analysing their education level, interests, skills, and preferred industry.

## ✨ Features

- **Multi-step UI** — clean profile-input screen → personalised results screen
- **8 curated career paths** across Technology, Data, Healthcare, and Business
- **Transparent scoring** — every recommendation shows exactly *why* it was suggested
- **Development roadmaps** — 5-step action plan for each career
- **Zero external API dependencies** — fully self-contained, no API keys required

## 🚀 Quick Start (Local)

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Run the app
streamlit run app.py
```

The app will open at `http://localhost:8501`.

## ☁️ Deploy to Streamlit Cloud

1. Push this repository to GitHub.
2. Visit [share.streamlit.io](https://share.streamlit.io) and sign in.
3. Click **"New app"**, select this repository.
4. Set **Main file path** to `app.py` (root of the repository).
5. Click **Deploy** — your app will be live at `https://<your-app>.streamlit.app`.

## 🧩 How It Works

Each career in the knowledge base is scored against the user's profile:

| Criterion         | Points |
|-------------------|--------|
| Interest match    | +4     |
| Industry match    | +3     |
| Each skill match  | +2     |
| Education match   | +1     |

The top 5 careers (score > 0) are displayed with full rationale and a development roadmap.

## 🛠️ Tech Stack

- **Python 3.10+**
- **Streamlit ≥ 1.32**
- Rule-based recommendation logic (no external AI/API)

---
Built by the **PathPilot Team** 🧭
