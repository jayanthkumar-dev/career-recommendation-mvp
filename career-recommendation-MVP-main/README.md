🎯 Career Recommendation System – MVP
A Python web application built with Streamlit that recommends 3–5 suitable career paths based on user inputs such as education level, interests, skills, and preferred industry.
Built as a rule-based, explainable MVP for hackathon use.
📌 Problem Statement
Many students and early-career professionals struggle to choose the right career path due to lack of personalized guidance.
Objective:
Design and develop a web application that:
Collects basic user inputs
Recommends 3–5 suitable career options
Provides a brief rationale for each recommendation
🚀 Solution Overview
This project implements a simple, explainable career recommendation engine using Python and Streamlit.
Key Highlights
Rule-based recommendation logic
Explainable scoring system (no black-box AI)
Clean, interactive UI
Fast and reliable MVP design
🧩 System Architecture
Copy code

User
 ↓
Streamlit App (Python)
 ↓
Rule-Based Recommendation Logic
 ↓
Career Recommendations (3–5 results)
🖥️ Application
Built using Python and Streamlit
Collects:
Education level
Interests
Skills
Preferred industry
Applies recommendation logic
Displays ranked career recommendations with reasons
🧠 Recommendation Logic (Explainable)
Each career option is evaluated against user inputs:
Matching interest increases score
Matching industry adds confidence
Relevant skills improve ranking
Education level ensures feasibility
The logic is deterministic and transparent, making recommendations easy to understand and justify.
📊 Output
For each recommended career, the system displays:
Career title
Brief description
Match score
Clear rationale explaining why the career was suggested
🛠️ Tech Stack
Application: Python, Streamlit
Architecture: Rule-based logic
✅ Conclusion
This project delivers a working, explainable, and scalable MVP that meets the problem statement requirements and demonstrates strong Python development fundamentals.

## How to Run
1. Ensure Python is installed.
2. Install dependencies: `pip install streamlit`
3. Run the app: `streamlit run app.py`
