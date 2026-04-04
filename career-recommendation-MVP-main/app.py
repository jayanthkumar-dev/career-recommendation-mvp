import streamlit as st

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

# Streamlit app
st.title("Smart Career Recommendation System")
st.markdown("Discover career paths tailored to your skills, interests, and goals")

# Sidebar for inputs
st.sidebar.header("Your Profile")

education = st.sidebar.selectbox(
    "Education Level",
    ["diploma", "ug", "pg"],
    format_func=lambda x: {"diploma": "Diploma", "ug": "Undergraduate", "pg": "Postgraduate"}[x]
)

interest = st.sidebar.selectbox(
    "Primary Interest",
    ["tech", "data", "health", "business"],
    format_func=lambda x: {"tech": "Technology", "data": "Data & Analytics", "health": "Healthcare", "business": "Business"}[x]
)

industry = st.sidebar.selectbox(
    "Preferred Industry",
    ["it", "finance", "healthcare", "media"],
    format_func=lambda x: {"it": "IT", "finance": "Finance", "healthcare": "Healthcare", "media": "Media"}[x]
)

skills = st.sidebar.multiselect(
    "Your Skills",
    ["programming", "analysis", "communication", "creativity", "leadership"],
    format_func=lambda x: {"programming": "Programming", "analysis": "Data Analysis", "communication": "Communication", "creativity": "Creativity", "leadership": "Leadership"}[x]
)

if st.sidebar.button("Get Career Recommendations"):
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

        scored_careers.append({**career, "score": score, "reasons": reasons})

    # Sort by score descending
    scored_careers.sort(key=lambda x: x["score"], reverse=True)

    # Display top 5
    st.header("Recommended Careers")
    for i, career in enumerate(scored_careers[:5]):
        with st.container():
            st.subheader(f"{i+1}. {career['title']}")
            st.write(f"**Career Overview:** {career_descriptions.get(career['title'], 'This career aligns well with your profile and interests.')}")
            st.write(f"**Why this career?** This career is recommended because it {', '.join(career['reasons'])}, making it a strong match for your background.")
            st.write("**Development Plan:**")
            for step in career["developmentPlan"].split('\n'):
                st.write(f"- {step}")
            st.write(f"**Match Score:** {career['score']}")
            st.divider()
else:
    st.write("Select your details on the sidebar and click 'Get Career Recommendations' to see personalized suggestions.")