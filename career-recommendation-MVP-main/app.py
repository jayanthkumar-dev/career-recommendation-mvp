import streamlit as st
import random

# Set page config
st.set_page_config(
    page_title="Autonomous Intelligence Platform",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 2rem;
        font-weight: bold;
    }
    .subtitle {
        font-size: 1.2rem;
        color: #666;
        text-align: center;
        margin-bottom: 3rem;
    }
    .card {
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
        border-radius: 15px;
        padding: 2rem;
        margin: 1rem 0;
        box-shadow: 0 8px 32px rgba(0,0,0,0.1);
        border: 1px solid rgba(255,255,255,0.2);
        color: #2c3e50;
    }
    .career-title {
        font-size: 1.5rem;
        color: #2c3e50;
        font-weight: bold;
        margin-bottom: 0.5rem;
    }
    .score-badge {
        background: linear-gradient(45deg, #ff6b6b, #feca57);
        color: white;
        padding: 0.5rem 1rem;
        border-radius: 20px;
        font-weight: bold;
        display: inline-block;
        margin-top: 1rem;
    }
    .sidebar-header {
        font-size: 1.5rem;
        color: #1f77b4;
        margin-bottom: 1rem;
    }
    .recommend-btn {
        background: linear-gradient(45deg, #667eea, #764ba2);
        color: white;
        border: none;
        padding: 0.75rem 2rem;
        border-radius: 25px;
        font-size: 1rem;
        font-weight: bold;
        cursor: pointer;
        transition: all 0.3s ease;
    }
    .recommend-btn:hover {
        transform: translateY(-2px);
        box-shadow: 0 5px 15px rgba(0,0,0,0.2);
    }
</style>
""", unsafe_allow_html=True)

# Career data
careers = [
    {
        "title": "Software Developer",
        "interest": "tech",
        "industry": "it",
        "skills": ["programming"],
        "minEdu": "ug",
        "developmentPlan": "1. Master core programming languages (e.g., JavaScript, Python).\n2. Build projects to create a portfolio.\n3. Learn popular frameworks (React, Node.js)."
    },
    {
        "title": "Data Analyst",
        "interest": "data",
        "industry": "finance",
        "skills": ["analysis"],
        "minEdu": "ug",
        "developmentPlan": "1. Learn Excel and SQL for data manipulation.\n2. Master data visualization tools like Tableau or PowerBI.\n3. Learn Python or R for advanced analysis."
    },
    {
        "title": "Healthcare Administrator",
        "interest": "health",
        "industry": "healthcare",
        "skills": ["communication", "leadership"],
        "minEdu": "diploma",
        "developmentPlan": "1. Gain experience in a healthcare setting.\n2. Learn healthcare regulations and medical terminology.\n3. Pursue a degree or certification in Healthcare Administration."
    },
    {
        "title": "Digital Marketer",
        "interest": "business",
        "industry": "media",
        "skills": ["creativity", "communication"],
        "minEdu": "ug",
        "developmentPlan": "1. Learn SEO, SEM, and social media marketing.\n2. Get certified in Google Analytics and Google Ads.\n3. Build and run real campaigns to demonstrate ROI."
    },
    {
        "title": "Product Manager",
        "interest": "business",
        "industry": "it",
        "skills": ["leadership", "communication"],
        "minEdu": "pg",
        "developmentPlan": "1. Gain experience in software development or business analysis.\n2. Learn Agile methodologies and product lifecycle management.\n3. Develop strong stakeholder communication skills."
    }
]

# Career descriptions
career_descriptions = {
    "Software Developer": "Designs, develops, and maintains software applications and systems using programming languages and frameworks.",
    "Data Analyst": "Analyzes data to identify trends, patterns, and insights that help organizations make informed decisions.",
    "Healthcare Administrator": "Manages healthcare facilities and operations, ensuring efficient services and coordination.",
    "Digital Marketer": "Promotes products or brands using digital channels like social media, search engines, and content platforms.",
    "Product Manager": "Leads product development by defining requirements, coordinating teams, and aligning products with business goals."
}

# Main app
st.markdown('<h1 class="main-header">🧠 Autonomous Intelligence Platform</h1>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">AI-Powered Career Guidance System - Discover your perfect career path with intelligent recommendations</p>', unsafe_allow_html=True)

# Sidebar for inputs
st.sidebar.markdown('<h2 class="sidebar-header">🔍 Profile Analysis</h2>', unsafe_allow_html=True)

education = st.sidebar.selectbox(
    "🎓 Education Level",
    ["diploma", "ug", "pg"],
    format_func=lambda x: {"diploma": "Diploma", "ug": "Undergraduate", "pg": "Postgraduate"}[x]
)

interest = st.sidebar.selectbox(
    "💡 Primary Interest",
    ["tech", "data", "health", "business"],
    format_func=lambda x: {"tech": "Technology", "data": "Data & Analytics", "health": "Healthcare", "business": "Business"}[x]
)

industry = st.sidebar.selectbox(
    "🏢 Preferred Industry",
    ["it", "finance", "healthcare", "media"],
    format_func=lambda x: {"it": "IT", "finance": "Finance", "healthcare": "Healthcare", "media": "Media"}[x]
)

skills = st.sidebar.multiselect(
    "🛠️ Your Skills",
    ["programming", "analysis", "communication", "creativity", "leadership"],
    format_func=lambda x: {"programming": "Programming", "analysis": "Data Analysis", "communication": "Communication", "creativity": "Creativity", "leadership": "Leadership"}[x]
)

# Add some AI-sounding features
st.sidebar.markdown("---")
st.sidebar.markdown("🤖 **AI Enhancement**")
use_ai_boost = st.sidebar.checkbox("Enable AI Boost for better recommendations")
confidence_level = st.sidebar.slider("AI Confidence Threshold", 0, 100, 50)

if st.sidebar.button("🚀 Get AI Recommendations", key="recommend"):
    with st.spinner("🤖 AI is analyzing your profile..."):
        import time
        time.sleep(1)  # Simulate AI processing
    
    # Scoring logic
    scored_careers = []
    for career in careers:
        score = 0
        reasons = []

        # Interest match
        if career["interest"] == interest:
            score += 4
            reasons.append("matches your interest")

        # Industry match
        if career["industry"] == industry:
            score += 3
            reasons.append("fits your preferred industry")

        # Skill match
        for skill in career["skills"]:
            if skill in skills:
                score += 2
                reasons.append(f"uses your {skill} skill")

        # Education match
        if career["minEdu"] == education:
            score += 1
            reasons.append("aligns with your education level")

        # AI boost
        if use_ai_boost:
            score += random.randint(0, 2)  # Add some randomness for "AI"

        scored_careers.append({**career, "score": score, "reasons": reasons})

    # Sort by score descending
    scored_careers.sort(key=lambda x: x["score"], reverse=True)

    # Filter by confidence
    filtered_careers = [c for c in scored_careers if c["score"] >= confidence_level / 10][:5]

    st.header("🎯 AI-Generated Career Recommendations")
    
    if not filtered_careers:
        st.warning("🤖 No recommendations meet the confidence threshold. Try adjusting the settings or selecting more skills.")
    else:
        for i, career in enumerate(filtered_careers, 1):
            dev_plan_html = "".join(f"<li>{step}</li>" for step in career["developmentPlan"].split('\n') if step.strip())
            with st.container():
                st.markdown(f"""
                <div class="card">
                    <div class="career-title">{i}. {career['title']}</div>
                    <p><strong>📋 Career Overview:</strong> {career_descriptions.get(career['title'], 'This career aligns well with your profile and interests.')}</p>
                    <p><strong>🧠 Why this career?</strong> This career is recommended because it {', '.join(career['reasons'])}, making it a strong match for your background.</p>
                    <p><strong>📈 Development Plan:</strong></p>
                    <ul>
                        {dev_plan_html}
                    </ul>
                    <div class="score-badge">Match Score: {career['score']}/10</div>
                </div>
                """, unsafe_allow_html=True)

else:
    st.info("👈 Fill in your profile details in the sidebar and click 'Get AI Recommendations' to receive personalized career suggestions powered by our autonomous intelligence system.")