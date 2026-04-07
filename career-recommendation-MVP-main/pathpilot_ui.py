from typing import Dict, Iterable, Tuple

import streamlit as st


def apply_theme(hide_sidebar: bool = True) -> None:
    sidebar_rules = ""
    if hide_sidebar:
        sidebar_rules = """
        [data-testid="stSidebar"] {display: none !important;}
        [data-testid="collapsedControl"] {display: none !important;}
        """

    st.markdown(
        f"""
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Manrope:wght@400;500;600;700;800&display=swap');

            :root {{
                --pp-bg: #0e1117;
                --pp-text: #f5f7fb;
                --pp-muted: #b3bdd1;
                --pp-blue: #4f8cff;
                --pp-purple: #9b5cff;
                --pp-card: rgba(22, 27, 40, 0.9);
                --pp-border: rgba(79, 140, 255, 0.22);
            }}

            {sidebar_rules}

            .stApp {{
                font-family: 'Manrope', 'Segoe UI', sans-serif;
                background:
                    radial-gradient(900px 500px at 12% -10%, rgba(79, 140, 255, 0.26), transparent 55%),
                    radial-gradient(800px 500px at 88% -12%, rgba(155, 92, 255, 0.24), transparent 58%),
                    var(--pp-bg);
                color: var(--pp-text);
            }}

            .main .block-container {{
                max-width: 900px;
                padding-top: 2.2rem;
                padding-bottom: 2.4rem;
            }}

            h1, h2, h3, h4, p, label, span, div {{
                color: var(--pp-text);
            }}

            .pp-hero {{
                text-align: center;
                margin: 0 auto 2.6rem auto;
                animation: ppFadeUp 0.55s ease;
                display: flex;
                flex-direction: column;
                align-items: center;
            }}

            .pp-hero h1 {{
                margin: 0;
                font-size: clamp(2.5rem, 7vw, 4.2rem);
                line-height: 1.03;
                font-weight: 800;
                letter-spacing: -0.03em;
            }}

            .pp-hero-tagline {{
                margin-top: 0.65rem;
                font-size: clamp(1rem, 2.5vw, 1.3rem);
                color: #d6def0;
                font-weight: 500;
            }}

            .pp-hero-tagline-lg {{
                font-size: clamp(1.15rem, 2.9vw, 1.55rem);
            }}

            .pp-hero-copy {{
                margin: 0.8rem auto 1.2rem auto;
                color: var(--pp-muted);
                max-width: 560px;
                font-size: 1rem;
                text-align: center;
                line-height: 1.55;
            }}

            .pp-hero-copy-balanced {{
                margin-top: 0.55rem;
                margin-bottom: 1.55rem;
            }}

            [data-testid="stVerticalBlockBorderWrapper"] {{
                border-radius: 20px;
                border: 1px solid var(--pp-border) !important;
                background: var(--pp-card);
                box-shadow: 0 20px 44px rgba(4, 8, 20, 0.42);
                transition: transform 0.2s ease, border-color 0.2s ease;
            }}

            [data-testid="stVerticalBlockBorderWrapper"]:hover {{
                transform: translateY(-2px);
                border-color: rgba(79, 140, 255, 0.45) !important;
            }}

            [data-testid="stTextInputRootElement"] input,
            [data-testid="stSelectbox"] div[data-baseweb="select"] > div {{
                border-radius: 12px !important;
                border: 1px solid rgba(179, 189, 209, 0.28) !important;
                background: rgba(16, 21, 33, 0.92) !important;
                color: #f5f7fb !important;
            }}

            .stButton > button {{
                border: 0 !important;
                border-radius: 999px !important;
                font-weight: 700 !important;
                color: #ffffff !important;
                background: linear-gradient(120deg, var(--pp-blue), var(--pp-purple)) !important;
                box-shadow: 0 12px 28px rgba(79, 140, 255, 0.32);
                transition: transform 0.15s ease, box-shadow 0.15s ease;
            }}

            .stButton > button:hover {{
                transform: translateY(-1px);
                box-shadow: 0 16px 30px rgba(155, 92, 255, 0.36);
            }}

            .pp-loading {{
                text-align: center;
                padding: 0.4rem 0 1.3rem 0;
                color: var(--pp-muted);
                font-weight: 500;
            }}

            .pp-success {{
                padding: 12px 16px;
                margin: 0.2rem 0 1rem 0;
                border-radius: 14px;
                border: 1px solid rgba(79, 140, 255, 0.35);
                background: linear-gradient(120deg, rgba(79, 140, 255, 0.2), rgba(155, 92, 255, 0.2));
                font-weight: 600;
            }}

            .pp-mini-note {{
                color: var(--pp-muted);
                font-size: 0.93rem;
                line-height: 1.45;
            }}

            .pp-badge {{
                display: inline-block;
                border-radius: 999px;
                padding: 4px 10px;
                font-size: 0.78rem;
                font-weight: 700;
                border: 1px solid rgba(79, 140, 255, 0.55);
                background: rgba(79, 140, 255, 0.18);
                color: #d9e7ff;
                margin-right: 8px;
                margin-bottom: 8px;
            }}

            .pp-warning {{
                border-left: 3px solid #ff7f7f;
                background: rgba(255, 127, 127, 0.12);
                border-radius: 10px;
                padding: 9px 12px;
                margin: 8px 0;
            }}

            .pp-advice {{
                border-left: 3px solid #8bffcb;
                background: rgba(139, 255, 203, 0.12);
                border-radius: 10px;
                padding: 9px 12px;
                margin: 8px 0;
            }}

            .pp-result-card {{
                padding: 0.2rem 0.2rem 0.5rem 0.2rem;
            }}

            .pp-result-animated {{
                opacity: 0;
                transform: translateY(8px);
                animation: ppCardIn 0.35s ease-out forwards;
                will-change: opacity, transform;
            }}

            .pp-meta-row {{
                display: flex;
                justify-content: space-between;
                align-items: center;
                gap: 12px;
                margin-bottom: 8px;
            }}

            .pp-salary-chip {{
                display: inline-block;
                border-radius: 999px;
                padding: 6px 11px;
                font-size: 0.8rem;
                font-weight: 700;
                color: #d9e7ff;
                background: rgba(79, 140, 255, 0.2);
                border: 1px solid rgba(79, 140, 255, 0.5);
            }}

            .pp-skill-pills {{
                display: flex;
                flex-wrap: wrap;
                gap: 8px;
                margin-top: 0.4rem;
            }}

            .pp-skill-pill {{
                border-radius: 999px;
                font-size: 0.78rem;
                font-weight: 600;
                padding: 4px 10px;
                color: #d9e7ff;
                border: 1px solid rgba(155, 92, 255, 0.45);
                background: rgba(155, 92, 255, 0.18);
            }}

            @keyframes ppFadeUp {{
                from {{
                    opacity: 0;
                    transform: translateY(8px);
                }}
                to {{
                    opacity: 1;
                    transform: translateY(0);
                }}
            }}

            @keyframes ppCardIn {{
                from {{
                    opacity: 0;
                    transform: translateY(8px);
                }}
                to {{
                    opacity: 1;
                    transform: translateY(0);
                }}
            }}

            @media (prefers-reduced-motion: reduce) {{
                .pp-hero,
                .pp-result-animated {{
                    animation: none !important;
                    opacity: 1 !important;
                    transform: none !important;
                }}
            }}
        </style>
        """,
        unsafe_allow_html=True,
    )


def render_hero_section() -> bool:
    st.markdown(
        """
        <div class="pp-hero">
            <h1>PathPilot</h1>
            <div class="pp-hero-tagline">Navigate Your Future with AI</div>
            <p class="pp-hero-copy">Your next move, mapped by AI in under a minute.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    _, center_col, _ = st.columns([1.6, 1.5, 1.6])
    with center_col:
        return st.button("Start Analysis", key="pp_start_analysis", use_container_width=True)


def render_profile_card(profile: Dict[str, str]) -> Tuple[Dict[str, str], bool]:
    with st.container(border=True):
        st.markdown("## Profile Input")
        st.caption("Quick inputs. High-signal output.")

        skills_text = st.text_input(
            "Skills",
            value=profile.get("skills_text", ""),
            placeholder="Python, Problem Solving, Communication",
        )

        interest_options = [
            "AI & Data",
            "Design & Product",
            "Software Development",
            "Business & Strategy",
            "Healthcare",
            "Finance",
        ]
        selected_interest = profile.get("interest", "")
        default_interest_index = 0
        if selected_interest in interest_options:
            default_interest_index = interest_options.index(selected_interest)
        interest = st.selectbox("Interests", options=interest_options, index=default_interest_index)

        education_options = [
            "High School",
            "Undergraduate",
            "Postgraduate",
            "Bootcamp / Certification",
        ]
        selected_education = profile.get("education", "")
        default_education_index = 0
        if selected_education in education_options:
            default_education_index = education_options.index(selected_education)
        education = st.selectbox("Education Level", options=education_options, index=default_education_index)

        analyze_clicked = st.button("Analyze with AI", use_container_width=True, key="pp_analyze")

    return {
        "education": education.strip(),
        "interest": interest.strip(),
        "industry": interest.strip(),
        "skills_text": skills_text.strip(),
        "github_url": profile.get("github_url", "").strip(),
        "linkedin_url": profile.get("linkedin_url", "").strip(),
    }, analyze_clicked


def render_loading_screen(message: str) -> None:
    _, center_col, _ = st.columns([1.4, 1.8, 1.4])
    with center_col:
        with st.container(border=True):
            st.markdown("### Building your career map")
            with st.spinner(" "):
                st.markdown(f"<div class='pp-loading'>{message}</div>", unsafe_allow_html=True)


def _render_skill_tags(skills: Iterable[str]) -> None:
    pills = "".join(f"<span class='pp-skill-pill'>{skill}</span>" for skill in skills)
    st.markdown(f"<div class='pp-skill-pills'>{pills}</div>", unsafe_allow_html=True)


def render_results_section(recommendations: Iterable[Dict[str, object]]) -> None:
    st.markdown("## Top Career Matches for You")
    st.markdown("<div class='pp-success'>✨ We've found the best career paths for you!</div>", unsafe_allow_html=True)

    for index, rec in enumerate(recommendations):
        with st.container(border=True):
            st.markdown(
                f"<div class='pp-result-card pp-result-animated' style='animation-delay:{index * 70}ms;'>",
                unsafe_allow_html=True,
            )
            st.markdown(
                f"""
                <div class='pp-meta-row'>
                    <h3 style='margin:0; font-size:1.4rem; font-weight:800;'>{rec.get('title', '')}</h3>
                    <span class='pp-salary-chip'>{rec.get('salary_range', 'INR 6L - 18L / year')}</span>
                </div>
                """,
                unsafe_allow_html=True,
            )

            score = min(100, int(rec.get("match_score", 85)))
            st.markdown(f"**Match: {score}%**")
            st.progress(score)

            st.markdown(f"**Why this fits you:** {rec.get('personalized_explanation', '')}")
            st.markdown("**Required skills**")
            _render_skill_tags(rec.get("skills", []))

            st.markdown("**Next moves**")
            for step in rec.get("development_plan", []):
                st.write(f"- {step}")
            st.markdown("</div>", unsafe_allow_html=True)
            st.markdown("")


def render_footer() -> None:
    st.markdown(
        """
        <div style="text-align:center; color:#8f9ab3; font-size:0.85rem; padding-top: 0.8rem;">
            PathPilot © 2026
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_mentor_intro() -> bool:
    st.markdown(
        """
        <div class="pp-hero">
            <h1>PathPilot AI Mentor</h1>
            <div class="pp-hero-tagline">A real career coach conversation, powered by intelligence.</div>
            <p class="pp-hero-copy">I will ask high-signal questions and map your best life-direction paths with strategy, risk, and roadmap.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    _, mid, _ = st.columns([1.5, 1.8, 1.5])
    with mid:
        return st.button("Start Mentor Session", use_container_width=True, key="pp_start_mentor")


def render_question_chat(history: Iterable[Dict[str, str]], question: Dict[str, object], selected_value: str) -> str:
    st.markdown("## Mentor Conversation")
    st.caption("One focused question at a time.")

    with st.container(border=True):
        for item in history:
            st.markdown(f"**Mentor:** {item.get('question', '')}")
            st.markdown(f"**You:** {item.get('answer', '')}")
            st.markdown("")

        st.markdown(f"**Mentor:** {question.get('prompt', '')}")
        options = question.get("options", [])
        labels = [str(opt.get("label", "")) for opt in options]
        values = [str(opt.get("value", "")) for opt in options]

        selected_index = 0
        if selected_value in values:
            selected_index = values.index(selected_value)

        selected_label = st.radio(
            "Choose the option that feels most true right now",
            options=labels,
            index=selected_index,
            key=f"mentor_q_{question.get('id', 'q')}",
        )

        label_to_value = {label: value for label, value in zip(labels, values)}
        return label_to_value.get(selected_label, values[0] if values else "")


def render_mentor_loading(message: str) -> None:
    _, center_col, _ = st.columns([1.4, 1.8, 1.4])
    with center_col:
        with st.container(border=True):
            st.markdown("### Mentor is synthesizing your direction")
            with st.spinner(" "):
                st.markdown(f"<div class='pp-loading'>{message}</div>", unsafe_allow_html=True)


def render_mentor_results(report: Dict[str, object]) -> None:
    persona = report.get("persona", {})
    careers = report.get("careers", [])

    st.markdown("## Your Career Direction Blueprint")

    with st.container(border=True):
        st.markdown("### User Persona")
        st.write(persona.get("summary", ""))
        st.markdown("**Core strengths**")
        for strength in persona.get("strengths", []):
            st.write(f"- {strength}")

    st.markdown("")

    for index, career in enumerate(careers):
        with st.container(border=True):
            st.markdown(
                f"<div class='pp-result-card pp-result-animated' style='animation-delay:{index * 70}ms;'>",
                unsafe_allow_html=True,
            )
            st.markdown(f"### {career.get('label', 'Career')} • {career.get('title', '')}")
            score = int(career.get("match_score", 80))
            st.markdown(f"**Match Score: {score}%**")
            st.progress(score)

            st.markdown(f"**Why this fits you:** {career.get('personalized_explanation', '')}")
            st.markdown(f"**Salary range:** {career.get('salary_range', '')}")

            st.markdown("**Skills required**")
            _render_skill_tags(career.get("skills_required", []))

            st.markdown("**Roadmap**")
            roadmap = career.get("roadmap", {})
            for phase in ["0-3", "3-6", "6-12"]:
                st.markdown(f"**{phase} months**")
                for step in roadmap.get(phase, []):
                    st.write(f"- {step}")

            st.markdown(f"**Industry insight:** {career.get('industry_insights', '')}")
            st.markdown(f"**Risk warning:** {career.get('risks', '')}")
            st.markdown("</div>", unsafe_allow_html=True)
            st.markdown("")

    with st.container(border=True):
        st.markdown("### Final Personal Advice")
        st.write(report.get("final_advice", ""))


def render_hybrid_intro() -> bool:
    st.markdown(
        """
        <div class="pp-hero">
            <h1>PathPilot Hybrid Coach</h1>
            <div class="pp-hero-tagline pp-hero-tagline-lg">Profile intelligence + mentor dialogue + strategy blueprint.</div>
            <p class="pp-hero-copy pp-hero-copy-balanced">Map your next 12 months with high-signal inputs and an adaptive AI mentor.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    _, center_col, _ = st.columns([1.5, 1.8, 1.5])
    with center_col:
        return st.button("Start Smart Onboarding", use_container_width=True, key="pp_hybrid_start")


def render_smart_profile_input(profile: Dict[str, object]) -> Tuple[Dict[str, object], bool]:
    with st.container(border=True):
        st.markdown("## Stage 1 • Smart Profile Input")
        st.caption("Give precise signals. Get sharper career direction.")

        st.markdown("### Basic Info")
        c1, c2 = st.columns(2)
        with c1:
            name = st.text_input("Name", value=str(profile.get("name", "")))
            education = st.selectbox(
                "Education",
                options=["High School", "Undergraduate", "Postgraduate", "Bootcamp / Certification"],
                index=["High School", "Undergraduate", "Postgraduate", "Bootcamp / Certification"].index(
                    str(profile.get("education", "Undergraduate"))
                ) if str(profile.get("education", "Undergraduate")) in ["High School", "Undergraduate", "Postgraduate", "Bootcamp / Certification"] else 1,
            )
        with c2:
            domain_interest = st.selectbox(
                "Domain of Interest",
                options=["Technology", "Design", "Business", "Finance", "Healthcare", "Marketing"],
                index=["Technology", "Design", "Business", "Finance", "Healthcare", "Marketing"].index(
                    str(profile.get("domain_interest", "Technology"))
                ) if str(profile.get("domain_interest", "Technology")) in ["Technology", "Design", "Business", "Finance", "Healthcare", "Marketing"] else 0,
            )

        mentor_mode = st.selectbox(
            "Mentor Mode",
            options=["Friendly Coach", "Corporate Strategist", "Creative Career Architect"],
            index=["Friendly Coach", "Corporate Strategist", "Creative Career Architect"].index(
                str(profile.get("mentor_mode", "Corporate Strategist"))
            ) if str(profile.get("mentor_mode", "Corporate Strategist")) in ["Friendly Coach", "Corporate Strategist", "Creative Career Architect"] else 1,
        )

        st.markdown("### Skills & Capability")
        suggested_skills = [
            "Python", "SQL", "Communication", "Problem Solving", "Design Thinking", "Data Analysis", "Leadership", "Marketing", "Research", "AI Fundamentals",
        ]
        selected_skills = st.multiselect(
            "Skills (tag style)",
            options=suggested_skills,
            default=[s for s in profile.get("skills", []) if s in suggested_skills],
        )
        custom_skills_text = st.text_input(
            "Add custom skills (comma separated)",
            value=str(profile.get("custom_skills_text", "")),
            placeholder="Figma, Financial Modeling, Public Speaking",
        )

        c3, c4 = st.columns(2)
        with c3:
            experience_level = st.selectbox(
                "Experience Level",
                options=["Beginner", "Intermediate", "Advanced"],
                index=["Beginner", "Intermediate", "Advanced"].index(str(profile.get("experience_level", "Beginner"))) if str(profile.get("experience_level", "Beginner")) in ["Beginner", "Intermediate", "Advanced"] else 0,
            )
        with c4:
            confidence_level = st.selectbox(
                "Confidence Level",
                options=["Low", "Medium", "High"],
                index=["Low", "Medium", "High"].index(str(profile.get("confidence_level", "Medium"))) if str(profile.get("confidence_level", "Medium")) in ["Low", "Medium", "High"] else 1,
            )

        st.markdown("### Goals")
        c5, c6 = st.columns(2)
        with c5:
            expected_salary = st.text_input(
                "Expected Salary (LPA)",
                value=str(profile.get("expected_salary", "12")),
                placeholder="e.g. 12",
            )
        with c6:
            career_priority = st.selectbox(
                "Career Priority",
                options=["income", "passion", "stability", "freedom"],
                index=["income", "passion", "stability", "freedom"].index(str(profile.get("career_priority", "passion"))) if str(profile.get("career_priority", "passion")) in ["income", "passion", "stability", "freedom"] else 1,
            )

        st.markdown("### Digital Presence (Optional)")
        c7, c8, c9 = st.columns(3)
        with c7:
            github_url = st.text_input("GitHub", value=str(profile.get("github_url", "")), placeholder="https://github.com/username")
        with c8:
            linkedin_url = st.text_input("LinkedIn", value=str(profile.get("linkedin_url", "")), placeholder="https://linkedin.com/in/username")
        with c9:
            portfolio_url = st.text_input("Portfolio", value=str(profile.get("portfolio_url", "")), placeholder="https://yourportfolio.com")

        submitted = st.button("Begin AI Mentor Conversation", use_container_width=True, key="pp_profile_submit")

    custom_skills = [part.strip() for part in custom_skills_text.split(",") if part.strip()]
    merged_skills = []
    for skill in selected_skills + custom_skills:
        if skill not in merged_skills:
            merged_skills.append(skill)

    return {
        "name": name.strip(),
        "education": education,
        "domain_interest": domain_interest,
        "mentor_mode": mentor_mode,
        "skills": merged_skills,
        "skills_text": ", ".join(merged_skills),
        "custom_skills_text": custom_skills_text,
        "experience_level": experience_level,
        "confidence_level": confidence_level,
        "expected_salary": expected_salary.strip(),
        "career_priority": career_priority,
        "github_url": github_url.strip(),
        "linkedin_url": linkedin_url.strip(),
        "portfolio_url": portfolio_url.strip(),
    }, submitted


def render_ai_conversation(history: Iterable[Dict[str, str]], question: Dict[str, object], selected_value: str) -> str:
    st.markdown("## Stage 2 • AI Conversation")
    st.caption("Adaptive mentor dialogue based on your profile.")

    with st.container(border=True):
        for item in history:
            st.markdown(f"**Mentor:** {item.get('question', '')}")
            st.markdown(f"**You:** {item.get('answer', '')}")
            st.markdown("")

        st.markdown(f"**Mentor:** {question.get('prompt', '')}")
        options = question.get("options", [])
        labels = [str(opt.get("label", "")) for opt in options]
        values = [str(opt.get("value", "")) for opt in options]

        index = 0
        if selected_value in values:
            index = values.index(selected_value)

        selected_label = st.radio(
            "Select your answer",
            options=labels,
            index=index,
            key=f"hybrid_question_{question.get('id', 'q')}",
        )
        mapping = {label: value for label, value in zip(labels, values)}
        return mapping.get(selected_label, values[0] if values else "")


def render_hybrid_blueprint(report: Dict[str, object]) -> None:
    st.markdown("## Stage 3 • Advanced Career Blueprint")

    profile_snapshot = report.get("profile_snapshot", {})
    persona = report.get("persona", {})
    strategic_snapshot = report.get("strategic_snapshot", {})
    careers = report.get("careers", [])

    mode = str(profile_snapshot.get("mentor_mode", "Corporate Strategist"))
    mode_voice = {
        "Friendly Coach": "Mentor tone: practical, encouraging, and action-focused.",
        "Corporate Strategist": "Mentor tone: structured, steady, and long-term strategic.",
        "Creative Career Architect": "Mentor tone: imaginative, differentiated, and portfolio-first.",
    }.get(mode, "Mentor tone: focused and strategic.")

    selectable_careers = [c for c in careers if c]
    if not selectable_careers:
        st.warning("No career recommendations available.")
        return

    options = [f"{c.get('label')}: {c.get('title')} ({c.get('match_score', 0)}%)" for c in selectable_careers]
    option_to_title = {opt: str(c.get("title", "")) for opt, c in zip(options, selectable_careers)}

    if "selected_deep_dive_career" not in st.session_state:
        st.session_state.selected_deep_dive_career = str(selectable_careers[0].get("title", ""))

    selected_option = st.radio("Career Selection", options=options, horizontal=True)
    st.session_state.selected_deep_dive_career = option_to_title.get(selected_option, st.session_state.selected_deep_dive_career)

    selected = next(
        (c for c in selectable_careers if str(c.get("title", "")) == st.session_state.selected_deep_dive_career),
        selectable_careers[0],
    )

    with st.expander("🧠 User Persona", expanded=False):
        st.write(persona.get("summary", ""))
        st.markdown(f"<p class='pp-mini-note'>{mode_voice}</p>", unsafe_allow_html=True)
        st.metric("Career Confidence Score", f"{strategic_snapshot.get('career_confidence_score', 0)}%")
        st.markdown(
            f"**Profile context:** {profile_snapshot.get('education', '')} • {profile_snapshot.get('domain_interest', '')} • Priority: {profile_snapshot.get('career_priority', '')}"
        )

    with st.expander(
        f"🔎 Deep Dive: {selected.get('label', 'Career')} • {selected.get('title', '')} ({selected.get('match_score', 0)}%)",
        expanded=True,
    ):
        st.markdown(
            f"<span class='pp-badge'>Confidence {selected.get('match_score', 0)}%</span><span class='pp-badge'>Mode: {mode}</span>",
            unsafe_allow_html=True,
        )
        st.progress(int(selected.get("match_score", 0)))
        st.markdown(f"**Why this fits:** {selected.get('personalized_explanation', '')}")

        with st.expander("🛠️ Skills", expanded=False):
            focus_skills = list(selected.get("skills_to_focus", []))[:6]
            max_count = max(1, len(focus_skills))
            for index, skill in enumerate(focus_skills, start=1):
                st.write(f"{index}. {skill}")
                skill_score = int(60 + ((max_count - index) * (35 / max_count)))
                st.progress(skill_score)

        with st.expander("🗺️ 12-Month Roadmap", expanded=False):
            roadmap = selected.get("roadmap", {})
            for phase in ["0-3", "3-6", "6-12"]:
                st.markdown(f"**{phase} months**")
                for step in roadmap.get(phase, []):
                    st.write(f"- {step}")
            st.markdown("**Development Plan**")
            for step in selected.get("development_plan", []):
                st.write(f"- {step}")

        with st.expander("💰 Salary", expanded=False):
            st.write(f"Range: {selected.get('salary_range', '')}")
            trajectory = selected.get("salary_trajectory", {})
            st.write(f"0-3 months: {trajectory.get('0-3', '')}")
            st.write(f"3-6 months: {trajectory.get('3-6', '')}")
            st.write(f"6-12 months: {trajectory.get('6-12', '')}")

        with st.expander("📈 Industry Insights", expanded=False):
            st.metric(
                "User vs Market",
                f"{strategic_snapshot.get('user_readiness_score', 0)} / {strategic_snapshot.get('market_benchmark_score', 0)}",
            )
            st.markdown(f"<p class='pp-mini-note'>{strategic_snapshot.get('comparison_summary', '')}</p>", unsafe_allow_html=True)
            st.write(selected.get("industry_insights", ""))

        with st.expander("⚠️ Warnings", expanded=False):
            st.markdown(
                f"<div class='pp-warning'><b>Risk of Inaction:</b> {strategic_snapshot.get('risk_of_inaction', '')}</div>",
                unsafe_allow_html=True,
            )
            st.write(selected.get("risks", ""))
            st.write(f"Fast Path: {strategic_snapshot.get('fast_path', '')}")
            st.write(f"Safe Path: {strategic_snapshot.get('safe_path', '')}")

        with st.expander("✨ Final Advice", expanded=False):
            st.markdown(
                f"<div class='pp-advice'>{strategic_snapshot.get('motivational_insight', '')}</div>",
                unsafe_allow_html=True,
            )
            st.markdown(f"<p class='pp-mini-note'>{mode_voice}</p>", unsafe_allow_html=True)
            st.write(report.get("final_advice", ""))
