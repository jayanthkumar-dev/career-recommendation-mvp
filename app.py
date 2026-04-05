from typing import Dict, List

import streamlit as st

st.set_page_config(
    page_title="PathPilot",
    page_icon="🧭",
    layout="wide",
    initial_sidebar_state="collapsed"
)


GLOBAL_STYLES = """
<style>
    * {
        margin: 0;
        padding: 0;
        box-sizing: border-box;
    }

    :root {
        color-scheme: dark;
    }

    body,
    .stApp {
        background: linear-gradient(135deg, #040714 0%, #0f172a 100%);
        color: #e2e8f0;
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
    }

    /* Navbar */
    .navbar {
        display: flex;
        align-items: center;
        justify-content: space-between;
        padding: 1.2rem 2rem 0.5rem;
        color: #e2e8f0;
        font-family: Inter, system-ui, sans-serif;
        margin-bottom: 1rem;
    }

    .navbar-logo {
        font-size: 1.25rem;
        letter-spacing: -0.02em;
        font-weight: 900;
        background: linear-gradient(135deg, #7c3aed 0%, #2563eb 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        display: flex;
        align-items: center;
        gap: 0.5rem;
    }

    .navbar-logo-icon {
        font-size: 1.5rem;
        background: linear-gradient(135deg, #7c3aed 0%, #2563eb 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    }

    .navbar-menu {
        display: flex;
        align-items: center;
        gap: 1rem;
        color: #94a3b8;
        font-size: 0.9rem;
    }

    .navbar-menu a {
        color: #94a3b8;
        text-decoration: none;
        transition: color 0.2s;
    }

    .navbar-menu a:hover {
        color: #e2e8f0;
    }

    /* Main hero panel - Page 1 */
    .hero-panel {
        border-radius: 28px;
        backdrop-filter: blur(18px);
        background: rgba(15, 23, 42, 0.88);
        border: 1px solid rgba(148, 163, 184, 0.18);
        box-shadow: 0 30px 90px rgba(15, 23, 42, 0.5);
        padding: 3rem 2.5rem;
        text-align: center;
        margin: 0 auto 2rem;
        max-width: 900px;
    }

    .page-title {
        font-size: clamp(2.2rem, 5vw, 3.2rem);
        margin: 0 0 0.8rem 0;
        color: #eef2ff;
        font-weight: 900;
        line-height: 1.1;
        word-break: break-word;
    }

    .page-subtitle {
        color: #cbd5e1;
        font-size: 1.05rem;
        line-height: 1.8;
        max-width: 800px;
        margin: 0 auto;
        word-break: break-word;
    }

    /* Form container - transparent */
    .form-container {
        max-width: 700px;
        margin: 2rem auto;
        padding: 0;
    }

    .form-label {
        color: #cbd5e1;
        font-size: 0.95rem;
        font-weight: 600;
        margin-bottom: 0.6rem;
        display: block;
    }

    .form-input {
        width: 100% !important;
        margin-bottom: 1.5rem;
    }

    .stTextInput>div>div>input {
        background: rgba(15, 23, 42, 0.95) !important;
        border: 1.5px solid rgba(148, 163, 184, 0.25) !important;
        border-radius: 14px !important;
        color: #e2e8f0 !important;
        padding: 0.8rem 1.2rem !important;
        font-size: 0.95rem !important;
    }

    .stTextInput>div>div>input::placeholder {
        color: #64748b !important;
    }

    .stTextInput>div>div>input:focus {
        border: 1.5px solid rgba(124, 58, 237, 0.5) !important;
        box-shadow: 0 0 0 3px rgba(124, 58, 237, 0.1) !important;
    }

    /* Button */
    .generate-btn {
        width: 100%;
        padding: 1rem;
        border-radius: 999px;
        background: linear-gradient(135deg, #7c3aed 0%, #2563eb 100%);
        color: white;
        font-size: 1rem;
        font-weight: 700;
        border: none;
        box-shadow: 0 20px 50px rgba(124, 58, 237, 0.3);
        cursor: pointer;
        transition: all 0.3s ease;
        margin-top: 0.5rem;
    }

    .generate-btn:hover {
        transform: translateY(-2px);
        box-shadow: 0 25px 60px rgba(124, 58, 237, 0.4);
    }

    .stButton>button {
        width: 100% !important;
        padding: 0.9rem 1.5rem !important;
        border-radius: 999px !important;
        background: linear-gradient(135deg, #7c3aed, #2563eb) !important;
        color: white !important;
        font-weight: 700 !important;
        border: none !important;
        box-shadow: 0 20px 50px rgba(124, 58, 237, 0.3) !important;
        transition: all 0.3s ease !important;
    }

    .stButton>button:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 25px 60px rgba(124, 58, 237, 0.4) !important;
    }

    /* Recommendation cards - Page 2 */
    .recommendations-title {
        font-size: clamp(2rem, 4vw, 3rem);
        color: #eef2ff;
        font-weight: 900;
        margin-bottom: 0.8rem;
        text-align: center;
    }

    .recommendations-subtitle {
        color: #cbd5e1;
        text-align: center;
        margin-bottom: 2.5rem;
        font-size: 1rem;
        max-width: 800px;
        margin-left: auto;
        margin-right: auto;
    }

    .cards-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(340px, 1fr));
        gap: 1.8rem;
        margin-bottom: 2rem;
    }

    .recommendation-card {
        border-radius: 24px;
        backdrop-filter: blur(18px);
        background: rgba(15, 23, 42, 0.95);
        border: 1px solid rgba(96, 165, 250, 0.15);
        box-shadow: 0 20px 60px rgba(15, 23, 42, 0.4);
        padding: 2rem;
        transition: all 0.3s ease;
        word-break: break-word;
        overflow-wrap: break-word;
    }

    .recommendation-card:hover {
        transform: translateY(-8px);
        box-shadow: 0 30px 80px rgba(124, 58, 237, 0.2);
        border-color: rgba(124, 58, 237, 0.3);
    }

    .card-emoji {
        font-size: 2.8rem;
        margin-bottom: 0.8rem;
        display: block;
    }

    .card-score {
        display: inline-block;
        background: linear-gradient(135deg, #7c3aed, #2563eb);
        color: white;
        padding: 0.45rem 0.85rem;
        border-radius: 999px;
        font-size: 0.85rem;
        font-weight: 700;
        margin-bottom: 0.8rem;
    }

    .card-title {
        font-size: 1.5rem;
        color: #eef2ff;
        margin: 0 0 0.6rem 0;
        font-weight: 800;
        word-break: break-word;
    }

    .card-description {
        color: #cbd5e1;
        line-height: 1.7;
        margin-bottom: 1.2rem;
        font-size: 0.95rem;
        word-break: break-word;
    }

    .card-section-label {
        color: #94a3b8;
        font-size: 0.85rem;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 0.05em;
        margin-top: 1rem;
        margin-bottom: 0.4rem;
    }

    .card-section-content {
        color: #cbd5e1;
        font-size: 0.9rem;
        line-height: 1.6;
        word-break: break-word;
    }

    .card-section-content ul {
        margin: 0;
        padding-left: 1.2rem;
    }

    .card-section-content li {
        margin-bottom: 0.35rem;
    }

    .card-header {
        display: flex;
        align-items: flex-start;
        justify-content: space-between;
        margin-bottom: 1.5rem;
        border-bottom: 1px solid rgba(96, 165, 250, 0.1);
        padding-bottom: 1rem;
    }

    .card-header-left {
        display: flex;
        align-items: flex-start;
        gap: 1rem;
    }

    .card-match-score {
        background: linear-gradient(135deg, #7c3aed 0%, #2563eb 100%);
        color: white;
        padding: 0.5rem 1rem;
        border-radius: 8px;
        font-size: 1rem;
        font-weight: 700;
        text-align: center;
        min-width: 70px;
    }

    .card-overview-section {
        margin-bottom: 1.5rem;
        padding: 1rem;
        background: rgba(30, 41, 59, 0.5);
        border-left: 3px solid #7c3aed;
        border-radius: 8px;
    }

    .card-section {
        margin-bottom: 1.2rem;
    }

    .card-section:last-child {
        margin-bottom: 0;
    }

    .skill-chip {
        display: inline-flex;
        align-items: center;
        background: linear-gradient(135deg, #7c3aed, #38bdf8);
        color: white;
        padding: 0.45rem 0.8rem;
        border-radius: 999px;
        font-size: 0.8rem;
        font-weight: 600;
        margin: 0.3rem 0.3rem 0 0;
    }

    .skills-container {
        margin-top: 1rem;
        display: flex;
        flex-wrap: wrap;
    }

    /* Footer */
    .footer {
        color: #94a3b8;
        text-align: center;
        padding: 2rem 1rem 1.5rem;
        font-size: 0.9rem;
    }

    /* Responsive */
    @media (max-width: 768px) {
        .hero-panel {
            padding: 2rem 1.5rem;
        }

        .form-container {
            padding: 1.8rem;
            margin: 1rem auto;
        }

        .cards-grid {
            grid-template-columns: 1fr;
        }

        .page-title {
            font-size: 2rem;
        }

        .recommendations-title {
            font-size: 1.8rem;
        }

        .navbar {
            padding: 1rem 1.5rem 0.5rem;
        }

        .navbar-menu {
            gap: 0.75rem;
            font-size: 0.8rem;
        }
    }
</style>
"""


if "page" not in st.session_state:
    st.session_state.page = "profile"

if "recommendations" not in st.session_state:
    st.session_state.recommendations = []

if "profile_saved" not in st.session_state:
    st.session_state.profile_saved = False

if "education" not in st.session_state:
    st.session_state.education = ""

if "interest" not in st.session_state:
    st.session_state.interest = ""

if "industry" not in st.session_state:
    st.session_state.industry = ""

if "skills_raw" not in st.session_state:
    st.session_state.skills_raw = ""

if "github" not in st.session_state:
    st.session_state.github = ""

if "linkedin" not in st.session_state:
    st.session_state.linkedin = ""


def set_page(page_name: str) -> None:
    st.session_state.page = page_name


def generate_recommendations_from_ai(profile: Dict) -> List[Dict]:
    """Generate career recommendations based on user profile data (offline, no API calls)."""
    
    # Comprehensive career database with keywords and details
    career_database = [
        {
            "title": "AI/Machine Learning Engineer",
            "emoji": "🤖",
            "keywords": ["ai", "ml", "machine learning", "python", "deep learning", "neural", "algorithm"],
            "base_description": "Build intelligent systems and algorithms that learn from data.",
            "why_template": "Your interest in {interest} combined with {skill} makes you ideal for ML engineering. This field is growing rapidly in {industry}.",
            "skills": ["Python", "TensorFlow", "Data Analysis", "Problem Solving"],
            "base_development": "1. Master Python and data structures\n2. Learn ML frameworks (TensorFlow, PyTorch)\n3. Build real ML projects with datasets"
        },
        {
            "title": "Data Scientist",
            "emoji": "📊",
            "keywords": ["data", "analytics", "python", "sql", "analysis", "statistics", "insights"],
            "base_description": "Extract actionable insights from data to drive business decisions.",
            "why_template": "Your analytical interest in {interest} and {skill} skills position you perfectly for data science in {industry}.",
            "skills": ["Python", "SQL", "Statistics", "Data Visualization"],
            "base_development": "1. Learn SQL and Python for data manipulation\n2. Master statistical analysis and visualization\n3. Work with real datasets and dashboards"
        },
        {
            "title": "Software Engineer",
            "emoji": "💻",
            "keywords": ["python", "programming", "java", "javascript", "coding", "development", "backend", "fullstack"],
            "base_description": "Design and build scalable software solutions and applications.",
            "why_template": "Your programming skills in {skill} and interest in {interest} make software engineering a natural fit for {industry}.",
            "skills": ["Programming", "System Design", "Problem Solving", "Code Quality"],
            "base_development": "1. Master core programming concepts\n2. Learn design patterns and architecture\n3. Contribute to open-source or build projects"
        },
        {
            "title": "Product Manager",
            "emoji": "🚀",
            "keywords": ["leadership", "management", "strategy", "communication", "business", "product"],
            "base_description": "Lead product strategy, prioritize roadmaps, and drive innovation.",
            "why_template": "Your leadership in {industry} and communication skills align with product management needs. Your {skill} background adds technical credibility.",
            "skills": ["Leadership", "Communication", "Strategic Thinking", "Cross-functional"],
            "base_development": "1. Learn product lifecycle and user research\n2. Develop roadmapping and prioritization skills\n3. Build track record of successful launches"
        },
        {
            "title": "Data Analyst",
            "emoji": "📈",
            "keywords": ["data", "analysis", "sql", "excel", "analytics", "reporting", "insights", "metrics"],
            "base_description": "Translate data into business insights through analysis and visualization.",
            "why_template": "Your analytical interest and {skill} skills are perfect for data analysis. High demand in {industry}.",
            "skills": ["SQL", "Excel", "Data Visualization", "Critical Thinking"],
            "base_development": "1. Master SQL and advanced Excel\n2. Learn visualization tools (Tableau, Power BI)\n3. Build analytical dashboards"
        },
        {
            "title": "UX/UI Designer",
            "emoji": "🎨",
            "keywords": ["design", "ux", "ui", "creative", "user research", "interface", "interest in design"],
            "base_description": "Create beautiful, intuitive product experiences that users love.",
            "why_template": "Your creative interest in {interest} combined with {industry} experience makes UX design ideal.",
            "skills": ["User Research", "Wireframing", "Visual Design", "Prototyping"],
            "base_development": "1. Learn design principles and tools (Figma)\n2. Master user research methodologies\n3. Build portfolio with real projects"
        },
        {
            "title": "DevOps Engineer",
            "emoji": "⚙️",
            "keywords": ["python", "cloud", "aws", "docker", "kubernetes", "infrastructure", "deployment", "linux"],
            "base_description": "Build reliable infrastructure and deployment pipelines for applications.",
            "why_template": "Your technical foundation in {skill} and knowledge of {industry} infrastructure makes DevOps a great path.",
            "skills": ["Cloud Platforms", "Docker", "Linux", "System Administration"],
            "base_development": "1. Master Linux and bash scripting\n2. Learn Docker and Kubernetes\n3. Set up CI/CD pipelines for real projects"
        },
        {
            "title": "Technical Consultant",
            "emoji": "💡",
            "keywords": ["consulting", "strategy", "leadership", "communication", "business", "technology", "industries"],
            "base_description": "Advise on technology strategy and solutions for complex business challenges.",
            "why_template": "Your combination of {skill} expertise and {industry} knowledge makes consulting compelling. Strong demand for technical advisors.",
            "skills": ["Strategic Thinking", "Communication", "Technical Knowledge", "Problem Solving"],
            "base_development": "1. Develop deep technical expertise\n2. Build business and consulting knowledge\n3. Gain experience across multiple industries"
        },
        {
            "title": "Security Engineer",
            "emoji": "🔒",
            "keywords": ["security", "python", "coding", "infrastructure", "linux", "network", "protection"],
            "base_description": "Protect systems and data by designing secure architectures.",
            "why_template": "Your technical foundation in {skill} and interest in {interest} align well with cybersecurity. Critical need in {industry}.",
            "skills": ["Security Protocols", "System Hardening", "Threat Analysis", "Linux"],
            "base_development": "1. Learn security fundamentals and protocols\n2. Master system hardening and networking\n3. Earn security certifications (Security+)"
        },
        {
            "title": "Tech Lead/Engineering Manager",
            "emoji": "👨‍💼",
            "keywords": ["leadership", "management", "python", "programming", "communication", "team", "guidance"],
            "base_description": "Lead engineering teams and guide technical strategy and growth.",
            "why_template": "Your leadership and {skill} engineering background make tech management perfect. High impact in {industry}.",
            "skills": ["Team Leadership", "Technical Mentoring", "Strategic Planning", "Communication"],
            "base_development": "1. Develop management and coaching skills\n2. Lead small projects and mentoring\n3. Scale to larger team leadership roles"
        }
    ]
    
    # Calculate match scores for each career
    education = profile.get("education", "").lower()
    interest = profile.get("interest", "").lower()
    industry = profile.get("industry", "").lower()
    skills = [s.lower() for s in profile.get("skills", [])]

    # Create comprehensive user keyword set with better matching
    user_keywords = set()

    # Process education
    for word in education.split():
        if len(word) > 2:  # Skip short words like "in", "of", etc.
            user_keywords.add(word)
            # Add common variations
            if word in ["computer", "computing"]:
                user_keywords.add("programming")
                user_keywords.add("coding")
            elif word in ["science", "engineering"]:
                user_keywords.add("technical")
                user_keywords.add("technology")

    # Process interest
    for word in interest.split():
        if len(word) > 2:
            user_keywords.add(word)
            # Add synonyms and related terms
            if word in ["ai", "artificial", "intelligence"]:
                user_keywords.add("ai")
                user_keywords.add("machine learning")
                user_keywords.add("ml")
                user_keywords.add("neural")
                user_keywords.add("algorithm")
            elif word in ["data", "analytics", "analysis"]:
                user_keywords.add("data")
                user_keywords.add("analytics")
                user_keywords.add("sql")
                user_keywords.add("statistics")
                user_keywords.add("insights")
            elif word in ["programming", "coding", "development"]:
                user_keywords.add("python")
                user_keywords.add("programming")
                user_keywords.add("coding")
                user_keywords.add("development")
            elif word in ["leadership", "management"]:
                user_keywords.add("leadership")
                user_keywords.add("management")
                user_keywords.add("communication")
                user_keywords.add("strategy")

    # Process industry
    for word in industry.split():
        if len(word) > 2:
            user_keywords.add(word)
            # Add industry-related terms
            if word in ["tech", "technology", "software"]:
                user_keywords.add("programming")
                user_keywords.add("coding")
                user_keywords.add("development")
            elif word in ["finance", "business"]:
                user_keywords.add("business")
                user_keywords.add("strategy")
                user_keywords.add("communication")

    # Add skills directly
    user_keywords.update(skills)

    scored_careers = []
    for career in career_database:
        # Calculate match score with better logic
        career_keywords = set(career["keywords"])
        matches = len(user_keywords & career_keywords)

        # Additional fuzzy matching for partial matches
        fuzzy_matches = 0
        for user_word in user_keywords:
            for career_word in career_keywords:
                # Check for partial matches (e.g., "machine" matches "machine learning")
                if user_word in career_word or career_word in user_word:
                    if user_word != career_word:  # Don't double count exact matches
                        fuzzy_matches += 0.5

        total_matches = matches + fuzzy_matches

        # Better scoring: base score varies by career relevance, higher match bonus
        base_score = 40  # Lower base score
        match_bonus = min(60, total_matches * 15)  # Up to 60% bonus
        match_score = min(100, base_score + match_bonus)

        # Build personalized why statement
        why_statement = career["why_template"].format(
            interest=interest.title() if interest else "technology",
            skill=skills[0].title() if skills else "technical foundation",
            industry=industry.title() if industry else "the industry"
        )

        scored_careers.append({
            "title": career["title"],
            "emoji": career["emoji"],
            "description": career["base_description"],
            "skills": career["skills"],
            "match_score": int(match_score),
            "why": why_statement,
            "development_plan": career["base_development"],
            "score": total_matches
        })

    # Sort by match score and return top 5
    scored_careers.sort(key=lambda x: x["score"], reverse=True)
    recommendations = scored_careers[:5]

    # Remove the intermediate "score" field
    for rec in recommendations:
        del rec["score"]

    return recommendations


def get_profile_inputs() -> Dict:
    return {
        "education": st.session_state.get("education", "").strip(),
        "interest": st.session_state.get("interest", "").strip(),
        "industry": st.session_state.get("industry", "").strip(),
        "skills": [skill.strip() for skill in st.session_state.get("skills_raw", "").split(",") if skill.strip()],
        "github": st.session_state.get("github", "").strip(),
        "linkedin": st.session_state.get("linkedin", "").strip(),
    }


def render_navbar() -> None:
    col1, col2 = st.columns([3, 1])
    
    with col1:
        st.markdown('<div class="navbar-logo"><span class="navbar-logo-icon">🚀</span>PathPilot</div>', unsafe_allow_html=True)
    
    with col2:
        c1, c2 = st.columns(2)
        with c1:
            if st.button("Home", key="nav_home_small", use_container_width=True):
                st.session_state.profile_saved = False
                set_page("profile")
                st.rerun()
        with c2:
            if st.button("About", key="nav_about_small", use_container_width=True):
                set_page("about")
                st.rerun()


def render_about_page() -> None:
    """About Page"""
    st.markdown(
        """
        <div class="hero-panel">
            <h1 class="page-title">About PathPilot</h1>
            <p class="page-subtitle">Discover your ideal career path with AI-powered recommendations</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    
    st.markdown("## 🚀 What is PathPilot?")
    st.write(
        """
        PathPilot is an intelligent career guidance platform that analyzes your educational background, 
        interests, industry preferences, and skills to recommend personalized career paths. 
        Whether you're just starting your career or looking for a change, PathPilot helps you discover 
        opportunities aligned with your strengths.
        """
    )
    
    st.markdown("## 🎯 How It Works")
    st.write(
        """
        1. **Enter Your Profile** - Tell us about your education, interests, industry focus, and skills
        2. **AI Analysis** - Our system analyzes your inputs against thousands of career profiles
        3. **Get Recommendations** - Receive personalized career recommendations with:
           - Match scores showing how well each career fits your profile
           - Career overviews explaining what each role entails
           - Why this career matches your background
           - Development plans to help you succeed
           - Key skills required for each position
        """
    )
    
    st.markdown("## ✨ Key Features")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("### 📊 Smart Matching")
        st.write("Advanced algorithm matches your profile against 10+ specialized careers")
    
    with col2:
        st.markdown("### 🎓 Skill Insights")
        st.write("Understand which skills are most valuable for your target career")
    
    with col3:
        st.markdown("### 📈 Growth Roadmap")
        st.write("Get actionable development plans to achieve your career goals")
    
    st.markdown("## 👥 Built by PathPilot Team")
    st.write(
        """
        PathPilot is built by a dedicated team of career coaches, engineers, and data scientists 
        passionate about helping individuals find their perfect career path. Our platform combines 
        industry expertise with cutting-edge technology to provide meaningful career guidance.
        """
    )
    
    st.markdown("## 📞 Contact Us")
    st.write(
        """
        Have questions or feedback? We'd love to hear from you!
        
        - **Email**: info@pathpilot.com
        - **Website**: www.pathpilot.com
        - **Support**: support@pathpilot.com
        """
    )
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Navigation
    if st.button("← Back to Home", use_container_width=True):
        st.session_state.profile_saved = False
        set_page("profile")
        st.rerun()


def render_page1_profile() -> None:
    """Page 1: Profile Input Form"""
    st.markdown(
        """
        <div class="hero-panel">
            <h1 class="page-title">Profile Analysis</h1>
            <p class="page-subtitle">Tell us about your background, interests, and skills to discover your ideal career path powered by AI.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    with st.container():
        st.markdown('<div class="form-container">', unsafe_allow_html=True)

        col1, col2 = st.columns([1, 1], gap="small")
        with col1:
            st.markdown('<label class="form-label">Education</label>', unsafe_allow_html=True)
            st.text_input(
                "Education",
                key="education",
                placeholder="e.g. Bachelor's in Computer Science",
                label_visibility="collapsed",
            )

        with col2:
            st.markdown('<label class="form-label">Interest</label>', unsafe_allow_html=True)
            st.text_input(
                "Interest",
                key="interest",
                placeholder="e.g. Sustainability, AI, Finance",
                label_visibility="collapsed",
            )

        col3, col4 = st.columns([1, 1], gap="small")
        with col3:
            st.markdown('<label class="form-label">Industry</label>', unsafe_allow_html=True)
            st.text_input(
                "Industry",
                key="industry",
                placeholder="e.g. Technology, Healthcare",
                label_visibility="collapsed",
            )

        with col4:
            st.markdown('<label class="form-label">Skills (comma-separated)</label>', unsafe_allow_html=True)
            st.text_input(
                "Skills",
                key="skills_raw",
                placeholder="e.g. Python, Leadership, Design",
                label_visibility="collapsed",
            )

        col5, col6 = st.columns([1, 1], gap="small")
        with col5:
            st.markdown('<label class="form-label">GitHub Profile (optional)</label>', unsafe_allow_html=True)
            st.text_input(
                "GitHub",
                key="github",
                placeholder="https://github.com/username",
                label_visibility="collapsed",
            )

        with col6:
            st.markdown('<label class="form-label">LinkedIn Profile (optional)</label>', unsafe_allow_html=True)
            st.text_input(
                "LinkedIn",
                key="linkedin",
                placeholder="https://linkedin.com/in/username",
                label_visibility="collapsed",
            )

        st.markdown("<br>", unsafe_allow_html=True)

        if st.button("Generate My Career Path", use_container_width=True):
            profile = get_profile_inputs()
            if profile["education"] and profile["interest"] and profile["industry"] and profile["skills"]:
                st.session_state.profile_saved = True
                set_page("results")
                st.rerun()
            else:
                st.error("Please fill in all required fields (Education, Interest, Industry, Skills) before generating recommendations.")

        st.markdown("</div>", unsafe_allow_html=True)

        st.markdown(
            """
            <script>
            const attachEnterNavigation = () => {
                const formContainer = document.querySelector('.form-container');
                if (!formContainer) return;

                const inputs = Array.from(formContainer.querySelectorAll('input[type=text]:not([data-enter-nav])'));
                inputs.forEach((input, index) => {
                    input.dataset.enterNav = 'true';
                    input.addEventListener('keydown', function (event) {
                        if (event.key === 'Enter') {
                            event.preventDefault();
                            const allInputs = Array.from(formContainer.querySelectorAll('input[type=text]'));
                            const nextInput = allInputs[index + 1];
                            if (nextInput) {
                                nextInput.focus();
                            }
                        }
                    });
                });
            };

            const observer = new MutationObserver(() => {
                attachEnterNavigation();
            });

            const initEnterNavigation = () => {
                attachEnterNavigation();
                observer.observe(document.body, { childList: true, subtree: true });
            };

            if (document.readyState === 'complete') {
                initEnterNavigation();
            } else {
                window.addEventListener('load', initEnterNavigation);
                setTimeout(initEnterNavigation, 1000);
            }
            </script>
            """,
            unsafe_allow_html=True,
        )


def render_page2_results() -> None:
    """Page 2: Career Recommendations"""
    profile = get_profile_inputs()

    if not profile["education"] or not profile["interest"] or not profile["industry"] or not profile["skills"]:
        st.warning("⚠️ Complete your profile first to see recommendations.")
        if st.button("Back to Profile"):
            set_page("profile")
            st.rerun()
        return

    # Generate recommendations on first load of results page
    if not st.session_state.recommendations or not st.session_state.profile_saved:
        with st.spinner("🔄 Analyzing your profile and generating personalized career recommendations..."):
            recommendations = generate_recommendations_from_ai(profile)
            st.session_state.recommendations = recommendations

    # Display title and profile summary
    st.title("🧭 Career Recommendations")
    st.markdown(f"**Based on your profile:** {profile['education']} | {profile['interest']} | {profile['industry']}")

    # Display recommendations as normal text cards
    for idx, career in enumerate(st.session_state.recommendations[:5]):
        with st.container():
            # Header with emoji, title, and match score
            col1, col2 = st.columns([4, 1])
            with col1:
                st.markdown(f"## {career.get('emoji', '💼')} {career['title']}")
            with col2:
                st.metric("Match Score", f"{career.get('match_score', 85)}%")
            
            # Career Overview
            st.markdown("### 📋 Career Overview")
            st.write(career['description'])
            
            # Why This Career?
            st.markdown("### ✨ Why This Career?")
            st.write(career.get('why', 'This role matches your profile well.'))
            
            # Development Plan
            st.markdown("### 🎯 Development Plan")
            st.write(career.get('development_plan', 'Focus on continuous skill development.'))
            
            # Key Skills
            st.markdown("### 🛠️ Key Skills")
            skills_text = ", ".join(career['skills'])
            st.write(skills_text)
            
            st.divider()  # Separator between cards

    # Navigation
    col1, col2 = st.columns([1, 1])
    with col1:
        if st.button("← Back to Profile", use_container_width=True):
            st.session_state.profile_saved = False
            set_page("profile")
            st.rerun()

    with col2:
        if st.button("Reset & Start Over", use_container_width=True):
            st.session_state.education = ""
            st.session_state.interest = ""
            st.session_state.industry = ""
            st.session_state.skills_raw = ""
            st.session_state.github = ""
            st.session_state.linkedin = ""
            st.session_state.recommendations = []
            st.session_state.profile_saved = False
            set_page("profile")
            st.rerun()


def main() -> None:
    st.markdown(GLOBAL_STYLES, unsafe_allow_html=True)
    render_navbar()

    if st.session_state.page == "profile":
        render_page1_profile()
    elif st.session_state.page == "about":
        render_about_page()
    else:
        render_page2_results()

    st.markdown('<div class="footer">© 2026 PathPilot | Built by PathPilot Team</div>', unsafe_allow_html=True)


if __name__ == "__main__":
    main()
