import streamlit as st

# ── Page config must be the very first Streamlit call ──────────────────────
st.set_page_config(
    page_title="PathPilot – Career Guidance",
    page_icon="🧭",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ── Global CSS ──────────────────────────────────────────────────────────────
st.markdown("""
<style>
    /* Hide the default Streamlit sidebar toggle / menu when not needed */
    [data-testid="collapsedControl"] { display: none; }

    /* ── Brand header ── */
    .brand-header {
        text-align: center;
        padding: 2rem 0 0.5rem;
    }
    .brand-logo {
        font-size: 3rem;
        font-weight: 900;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        letter-spacing: -1px;
    }
    .brand-tagline {
        font-size: 1.1rem;
        color: #6b7280;
        margin-top: 0.25rem;
    }

    /* ── Section headings ── */
    .section-title {
        font-size: 1.6rem;
        font-weight: 700;
        color: #1f2937;
        margin-bottom: 1.5rem;
        padding-bottom: 0.5rem;
        border-bottom: 3px solid #667eea;
        display: inline-block;
    }

    /* ── Career card ── */
    .career-card {
        background: linear-gradient(135deg, #f8f9ff 0%, #eef2ff 100%);
        border-radius: 16px;
        padding: 1.75rem;
        margin: 1rem 0;
        box-shadow: 0 4px 20px rgba(102, 126, 234, 0.12);
        border-left: 5px solid #667eea;
    }
    .career-card-title {
        font-size: 1.35rem;
        font-weight: 700;
        color: #1f2937;
        margin-bottom: 0.5rem;
    }
    .career-card p {
        color: #374151;
        line-height: 1.6;
        margin: 0.4rem 0;
    }
    .career-card ul {
        margin: 0.5rem 0 0.5rem 1.2rem;
        color: #374151;
        line-height: 1.8;
    }
    .match-badge {
        display: inline-block;
        background: linear-gradient(45deg, #667eea, #764ba2);
        color: white;
        padding: 0.35rem 1rem;
        border-radius: 20px;
        font-weight: 700;
        font-size: 0.9rem;
        margin-top: 0.75rem;
    }

    /* ── Info / warning banners ── */
    .info-banner {
        background: linear-gradient(135deg, #eff6ff 0%, #dbeafe 100%);
        border-radius: 12px;
        padding: 1.25rem 1.5rem;
        border-left: 5px solid #3b82f6;
        color: #1e40af;
        font-size: 1rem;
    }

    /* ── Step indicator ── */
    .step-indicator {
        text-align: center;
        font-size: 0.9rem;
        color: #9ca3af;
        margin-bottom: 1rem;
    }

    /* ── Footer ── */
    .footer {
        text-align: center;
        padding: 2rem 0 1rem;
        color: #9ca3af;
        font-size: 0.85rem;
        border-top: 1px solid #e5e7eb;
        margin-top: 3rem;
    }
</style>
""", unsafe_allow_html=True)

# ── Career knowledge base ───────────────────────────────────────────────────
CAREERS = [
    {
        "title": "Software Developer",
        "interest": "tech",
        "industry": "it",
        "skills": ["programming"],
        "minEdu": "ug",
        "description": (
            "Designs, develops, and maintains software applications and systems "
            "using modern programming languages and frameworks."
        ),
        "developmentPlan": [
            "Master core programming languages (Python, JavaScript, Java).",
            "Build a portfolio of personal projects on GitHub.",
            "Learn popular frameworks such as React, Node.js, or Django.",
            "Contribute to open-source projects to gain collaborative experience.",
            "Pursue cloud certifications (AWS, GCP, or Azure) for a competitive edge.",
        ],
    },
    {
        "title": "Data Analyst",
        "interest": "data",
        "industry": "finance",
        "skills": ["analysis"],
        "minEdu": "ug",
        "description": (
            "Analyses datasets to uncover trends and actionable insights that help "
            "organisations make informed, data-driven decisions."
        ),
        "developmentPlan": [
            "Learn SQL and Excel for data extraction and manipulation.",
            "Master visualisation tools such as Tableau or Power BI.",
            "Study Python (pandas, matplotlib) or R for advanced analytics.",
            "Complete Google Data Analytics or IBM Data Analyst certification.",
            "Practice storytelling with data through dashboards and reports.",
        ],
    },
    {
        "title": "Healthcare Administrator",
        "interest": "health",
        "industry": "healthcare",
        "skills": ["communication", "leadership"],
        "minEdu": "diploma",
        "description": (
            "Manages healthcare facility operations, coordinates staff, ensures "
            "regulatory compliance, and improves patient experience."
        ),
        "developmentPlan": [
            "Gain hands-on experience in a healthcare setting.",
            "Learn healthcare regulations, billing codes, and medical terminology.",
            "Pursue a degree or certification in Healthcare Administration (MHA/ACHE).",
            "Develop leadership and project management skills.",
            "Stay current with healthcare technology and policy changes.",
        ],
    },
    {
        "title": "Digital Marketer",
        "interest": "business",
        "industry": "media",
        "skills": ["creativity", "communication"],
        "minEdu": "ug",
        "description": (
            "Promotes brands and products across digital channels—SEO, social media, "
            "email, and paid ads—to drive growth and engagement."
        ),
        "developmentPlan": [
            "Learn SEO, SEM, and social media marketing fundamentals.",
            "Earn Google Analytics 4 and Google Ads certifications.",
            "Build and run real campaigns to demonstrate measurable ROI.",
            "Stay updated on platform algorithm changes and content trends.",
            "Develop copywriting and creative design skills.",
        ],
    },
    {
        "title": "Product Manager",
        "interest": "business",
        "industry": "it",
        "skills": ["leadership", "communication"],
        "minEdu": "pg",
        "description": (
            "Leads product strategy and development by defining requirements, "
            "aligning cross-functional teams, and delivering user-centric solutions."
        ),
        "developmentPlan": [
            "Gain experience in software development or business analysis.",
            "Learn Agile/Scrum methodologies and product lifecycle management.",
            "Develop strong stakeholder communication and prioritisation skills.",
            "Study user research and usability testing techniques.",
            "Pursue a CSPO or Product School certification.",
        ],
    },
    {
        "title": "Cybersecurity Analyst",
        "interest": "tech",
        "industry": "finance",
        "skills": ["programming", "analysis"],
        "minEdu": "ug",
        "description": (
            "Protects organisations from cyber threats by monitoring networks, "
            "analysing vulnerabilities, and responding to security incidents."
        ),
        "developmentPlan": [
            "Learn networking fundamentals (TCP/IP, firewalls, VPNs).",
            "Study ethical hacking and penetration testing basics.",
            "Pursue CompTIA Security+, CEH, or CISSP certification.",
            "Practice on platforms like TryHackMe or HackTheBox.",
            "Stay current with threat intelligence and emerging attack vectors.",
        ],
    },
    {
        "title": "UX Designer",
        "interest": "tech",
        "industry": "media",
        "skills": ["creativity", "communication"],
        "minEdu": "ug",
        "description": (
            "Crafts intuitive and engaging digital experiences by researching user "
            "needs, designing wireframes, and iterating based on feedback."
        ),
        "developmentPlan": [
            "Learn design tools: Figma, Sketch, or Adobe XD.",
            "Study user research methods and usability testing.",
            "Build a portfolio of case studies showcasing your design process.",
            "Understand basic front-end principles (HTML/CSS) for developer handoff.",
            "Earn a Google UX Design Professional Certificate.",
        ],
    },
    {
        "title": "Financial Analyst",
        "interest": "data",
        "industry": "finance",
        "skills": ["analysis", "communication"],
        "minEdu": "ug",
        "description": (
            "Evaluates financial data, builds models, and provides investment or "
            "budget recommendations to guide strategic business decisions."
        ),
        "developmentPlan": [
            "Master financial modelling in Excel and financial statement analysis.",
            "Study corporate finance, accounting, and valuation methods.",
            "Pursue CFA Level 1 or FMVA certification.",
            "Practice building DCF and LBO models with real company data.",
            "Develop strong presentation and stakeholder reporting skills.",
        ],
    },
]

EDU_LABELS = {
    "diploma": "Diploma / Certificate",
    "ug": "Undergraduate Degree",
    "pg": "Postgraduate Degree",
}
INTEREST_LABELS = {
    "tech": "Technology & Engineering",
    "data": "Data & Analytics",
    "health": "Healthcare & Medicine",
    "business": "Business & Management",
}
INDUSTRY_LABELS = {
    "it": "Information Technology",
    "finance": "Finance & Banking",
    "healthcare": "Healthcare",
    "media": "Media & Marketing",
}
SKILL_LABELS = {
    "programming": "Programming",
    "analysis": "Data Analysis",
    "communication": "Communication",
    "creativity": "Creativity & Design",
    "leadership": "Leadership",
}
EDU_RANK = {"diploma": 0, "ug": 1, "pg": 2}


# ── Recommendation engine ───────────────────────────────────────────────────
def compute_recommendations(education: str, interest: str, industry: str, skills: list) -> list:
    """Score each career and return the top matches."""
    results = []
    for career in CAREERS:
        score = 0
        reasons = []

        if career["interest"] == interest:
            score += 4
            reasons.append(f"aligns with your {INTEREST_LABELS[interest]} interest")

        if career["industry"] == industry:
            score += 3
            reasons.append(f"fits your preferred {INDUSTRY_LABELS[industry]} industry")

        matched_skills = [s for s in career["skills"] if s in skills]
        for skill in matched_skills:
            score += 2
            reasons.append(f"leverages your {SKILL_LABELS[skill]} skill")

        # Education feasibility: career accessible at user's level
        if EDU_RANK[education] >= EDU_RANK[career["minEdu"]]:
            score += 1
            reasons.append("matches your education level")

        results.append({**career, "score": score, "reasons": reasons})

    results.sort(key=lambda x: x["score"], reverse=True)
    # Return top 5 careers with at least 1 matching criterion
    return [r for r in results if r["score"] > 0][:5]


# ── Session-state initialisation ────────────────────────────────────────────
if "page" not in st.session_state:
    st.session_state.page = "profile"
if "recommendations" not in st.session_state:
    st.session_state.recommendations = []
if "profile" not in st.session_state:
    st.session_state.profile = {}


# ── Brand header (shown on every page) ─────────────────────────────────────
st.markdown("""
<div class="brand-header">
    <div class="brand-logo">🧭 PathPilot</div>
    <div class="brand-tagline">Discover your perfect career path — powered by smart matching</div>
</div>
""", unsafe_allow_html=True)

st.write("")  # spacing


# ── PAGE 1: Profile Input ───────────────────────────────────────────────────
def render_profile_page():
    st.markdown('<p class="step-indicator">Step 1 of 2 — Build Your Profile</p>', unsafe_allow_html=True)
    st.markdown('<span class="section-title">📝 Tell us about yourself</span>', unsafe_allow_html=True)

    col1, col2 = st.columns(2, gap="large")

    with col1:
        education = st.selectbox(
            "🎓 Highest Education Level",
            options=list(EDU_LABELS.keys()),
            format_func=lambda x: EDU_LABELS[x],
            index=1,
            help="Select your current or highest completed level of education.",
        )

        interest = st.selectbox(
            "💡 Primary Interest Area",
            options=list(INTEREST_LABELS.keys()),
            format_func=lambda x: INTEREST_LABELS[x],
            index=0,
            help="Choose the broad field you are most passionate about.",
        )

    with col2:
        industry = st.selectbox(
            "🏢 Preferred Industry",
            options=list(INDUSTRY_LABELS.keys()),
            format_func=lambda x: INDUSTRY_LABELS[x],
            index=0,
            help="Select the industry sector where you'd like to build your career.",
        )

        skills = st.multiselect(
            "🛠️ Your Key Skills",
            options=list(SKILL_LABELS.keys()),
            format_func=lambda x: SKILL_LABELS[x],
            default=[],
            help="Select all the skills you currently possess.",
        )

    st.write("")

    if not skills:
        st.markdown(
            '<div class="info-banner">💡 <strong>Tip:</strong> Select at least one skill to get the most relevant career recommendations.</div>',
            unsafe_allow_html=True,
        )
        st.write("")

    _, centre, _ = st.columns([1, 2, 1])
    with centre:
        if st.button("🚀 Get My Career Recommendations", use_container_width=True, type="primary"):
            with st.spinner("Analysing your profile…"):
                recs = compute_recommendations(education, interest, industry, skills)

            st.session_state.profile = {
                "education": education,
                "interest": interest,
                "industry": industry,
                "skills": skills,
            }
            st.session_state.recommendations = recs
            st.session_state.page = "recommendations"
            st.rerun()


# ── PAGE 2: Recommendations ─────────────────────────────────────────────────
def render_recommendations_page():
    profile = st.session_state.profile
    recs = st.session_state.recommendations

    st.markdown('<p class="step-indicator">Step 2 of 2 — Your Personalised Results</p>', unsafe_allow_html=True)

    # Profile summary banner
    st.markdown(
        f"""
        <div class="info-banner">
            📋 <strong>Profile Summary:</strong>
            {EDU_LABELS.get(profile.get('education',''), '')} &nbsp;|&nbsp;
            {INTEREST_LABELS.get(profile.get('interest',''), '')} &nbsp;|&nbsp;
            {INDUSTRY_LABELS.get(profile.get('industry',''), '')} &nbsp;|&nbsp;
            Skills: {', '.join(SKILL_LABELS[s] for s in profile.get('skills', [])) or 'None selected'}
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.write("")

    st.markdown('<span class="section-title">🎯 Your Career Recommendations</span>', unsafe_allow_html=True)

    if not recs:
        st.warning(
            "No strong matches found for your current profile. Try selecting more skills or a different interest area.",
            icon="⚠️",
        )
    else:
        for i, career in enumerate(recs, 1):
            plan_items = "".join(f"<li>{step}</li>" for step in career["developmentPlan"])
            reasons_text = "; ".join(career["reasons"]) if career["reasons"] else "general alignment with your profile"
            st.markdown(
                f"""
                <div class="career-card">
                    <div class="career-card-title">#{i} &nbsp; {career['title']}</div>
                    <p><strong>📋 Overview:</strong> {career['description']}</p>
                    <p><strong>🤔 Why this career?</strong> This role is recommended because it {reasons_text}.</p>
                    <p><strong>📈 Development Roadmap:</strong></p>
                    <ul>{plan_items}</ul>
                    <div class="match-badge">Match Score: {career['score']} / 10</div>
                </div>
                """,
                unsafe_allow_html=True,
            )

    st.write("")
    _, centre, _ = st.columns([1, 2, 1])
    with centre:
        if st.button("← Back to Profile", use_container_width=True):
            st.session_state.page = "profile"
            st.rerun()


# ── Router ───────────────────────────────────────────────────────────────────
if st.session_state.page == "profile":
    render_profile_page()
elif st.session_state.page == "recommendations":
    render_recommendations_page()

# ── Footer ───────────────────────────────────────────────────────────────────
st.markdown(
    '<div class="footer">Built by the PathPilot Team &nbsp;|&nbsp; Helping you navigate your career journey 🧭</div>',
    unsafe_allow_html=True,
)
