🎯 Career Recommendation System – MVP
A full-stack web application that recommends 3–5 suitable career paths based on user inputs such as education level, interests, skills, and preferred industry.
Built as a rule-based, explainable MVP for hackathon use.
📌 Problem Statement
Many students and early-career professionals struggle to choose the right career path due to lack of personalized guidance.
Objective:
Design and develop a web application that:
Collects basic user inputs
Recommends 3–5 suitable career options
Provides a brief rationale for each recommendation
🚀 Solution Overview
This project implements a simple, explainable career recommendation engine using a full-stack architecture.
Key Highlights
Rule-based recommendation logic
Explainable scoring system (no black-box AI)
Clean, full-screen UI
Fast and reliable MVP design
🧩 System Architecture
Copy code

User
 ↓
Frontend (HTML, CSS, JavaScript)
 ↓
Backend API (Node.js + Express)
 ↓
Rule-Based Recommendation Logic
 ↓
Career Recommendations (3–5 results)
🖥️ Frontend
Built using HTML, CSS, and JavaScript
Collects:
Education level
Interests
Skills
Preferred industry
Sends user input to backend via REST API
Displays ranked career recommendations with reasons
⚙️ Backend
Built using Node.js and Express
Exposes a /recommend API endpoint
Uses a predefined career dataset
Applies a weighted scoring algorithm:
Interest match → highest weight
Industry match → medium weight
Skill match → additive weight
Education match → refinement
Ranks careers and returns top results
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
Frontend: HTML, CSS, JavaScript
Backend: Node.js, Express
Architecture: REST API, rule-based logic
✅ Conclusion
This project delivers a working, explainable, and scalable MVP that meets the problem statement requirements and demonstrates strong full-stack fundamentals.
