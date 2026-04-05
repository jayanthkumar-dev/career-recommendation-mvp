from typing import Dict, Iterable, List

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
            {sidebar_rules}

            .stApp {{
                background:
                    radial-gradient(1100px 500px at 10% 0%, rgba(56, 189, 248, 0.22), transparent 55%),
                    radial-gradient(900px 500px at 90% 0%, rgba(124, 58, 237, 0.22), transparent 55%),
                    linear-gradient(135deg, #070b25 0%, #1c1250 100%);
            }}

            .main .block-container {{
                padding-top: 1.1rem;
                padding-bottom: 1.4rem;
                max-width: 1120px;
            }}

            h1, h2, h3, p, label, div, span {{
                color: #e2e8f0;
            }}

            [data-testid="stVerticalBlockBorderWrapper"] {{
                border-radius: 16px;
                border: 1px solid rgba(148, 163, 184, 0.25) !important;
                background: rgba(15, 23, 42, 0.50);
                box-shadow: 0 16px 32px rgba(2, 6, 23, 0.35);
                backdrop-filter: blur(8px);
            }}

            .stButton > button {{
                border: 0 !important;
                border-radius: 999px !important;
                color: #ffffff !important;
                font-weight: 700 !important;
                background: linear-gradient(135deg, #38bdf8 0%, #7c3aed 100%) !important;
                box-shadow: 0 10px 24px rgba(59, 130, 246, 0.35) !important;
                transition: transform 0.18s ease, box-shadow 0.18s ease;
            }}

            .stButton > button:hover {{
                transform: translateY(-1px);
                box-shadow: 0 14px 28px rgba(124, 58, 237, 0.45) !important;
            }}

            [data-testid="stTextInputRootElement"] input,
            [data-testid="stTextAreaRootElement"] textarea {{
                border-radius: 12px !important;
                background: rgba(15, 23, 42, 0.7) !important;
                color: #e2e8f0 !important;
                border: 1px solid rgba(148, 163, 184, 0.35) !important;
            }}
        </style>
        """,
        unsafe_allow_html=True,
    )


def render_top_nav(is_results_page: bool = False) -> None:
    col1, col2, col3, col4 = st.columns([3.2, 1, 1, 1], vertical_alignment="center")

    with col1:
        st.markdown("""
        <div style="display:flex; align-items:center; gap:6px;">
            <span style="font-size:1.95rem; line-height:1; display:inline-flex; align-items:center; transform: translateY(-1px);">🚀</span>
            <div style="display:flex; flex-direction:column; justify-content:center; gap:1px; line-height:1;">
                <h2 style="margin:0; font-size:1.6rem; font-weight:900; line-height:1.05; background:linear-gradient(135deg, #38bdf8 0%, #7c3aed 100%); -webkit-background-clip:text; -webkit-text-fill-color:transparent; background-clip:text;">
                    PathPilot
                </h2>
                <p style="margin:0; font-size:0.75rem; letter-spacing:0.08em; color:#94a3b8; font-weight:700; line-height:1.05;">
                    CAREER AI NAVIGATOR
                </p>
            </div>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        if st.button("Home", use_container_width=True, key=f"nav_home_{'results' if is_results_page else 'home'}"):
            st.session_state.home_section = "profile"
            if is_results_page:
                st.switch_page("app.py")
            else:
                st.rerun()
    with col3:
        if st.button("About", use_container_width=True, key=f"nav_about_{'results' if is_results_page else 'home'}"):
            st.session_state.home_section = "about"
            if is_results_page:
                st.switch_page("app.py")
            else:
                st.rerun()
    with col4:
        if st.button("Contact", use_container_width=True, key=f"nav_contact_{'results' if is_results_page else 'home'}"):
            st.session_state.home_section = "contact"
            if is_results_page:
                st.switch_page("app.py")
            else:
                st.rerun()


def render_about_section() -> None:
    st.markdown(
        """
        <div style="padding: 8px 0 2px 0;">
            <h2 style="margin:0; font-size:2rem; font-weight:900; background:linear-gradient(135deg, #38bdf8 0%, #7c3aed 100%); -webkit-background-clip:text; -webkit-text-fill-color:transparent; background-clip:text;">
                About PathPilot
            </h2>
            <p style="margin:10px 0 0 0; color:#cbd5e1; font-size:1.05rem; line-height:1.75; max-width:900px;">
                PathPilot is an AI-powered career navigation platform designed to help students and professionals discover career directions with clarity and confidence.
                By combining your profile, interests, industry context, and practical skill signals, PathPilot transforms scattered information into focused career recommendations you can act on.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("")
    col1, col2, col3 = st.columns(3)
    with col1:
        with st.container(border=True):
            st.markdown("### AI-Powered Matching")
            st.write(
                "PathPilot analyzes profile and skill signals to rank career paths that align with your strengths and goals."
            )
    with col2:
        with st.container(border=True):
            st.markdown("### Actionable Roadmaps")
            st.write(
                "Each recommendation includes development steps and key skills so users know exactly what to do next."
            )
    with col3:
        with st.container(border=True):
            st.markdown("### Built for Real Growth")
            st.write(
                "From first-career decisions to role transitions, PathPilot supports practical, future-ready planning."
            )

    st.markdown("")
    with st.container(border=True):
        st.markdown("### Why Users Choose PathPilot")
        st.write("Clear, personalized recommendations instead of generic career advice.")
        st.write("Fast profile-to-career insights in seconds.")
        st.write("A startup-style experience with clean, modern design and focused guidance.")


def render_contact_section() -> None:
    st.markdown("### Contact")
    st.write("For feedback or support, reach us at hello@pathpilot.ai")


def render_home_intro() -> None:
    _, center_col, _ = st.columns([1, 2.2, 1])
    with center_col:
        st.markdown(
            """
            <div style="text-align: center; padding: 52px 0 22px 0; max-width: 760px; margin: 0 auto;">
                <h1 style="font-size: clamp(2.0rem, 4.5vw, 3.6rem); font-weight: 900; background: linear-gradient(135deg, #38bdf8 0%, #7c3aed 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text; margin: 0; line-height: 1.12;">
                    Profile Analysis
                </h1>
                <p style="font-size: clamp(1rem, 1.9vw, 1.35rem); color: #cbd5e1; margin: 12px auto 0 auto; font-weight: 400; line-height: 1.6; max-width: 680px;">
                    Enter your profile, and let AI navigate your career journey
                </p>
            </div>
            """,
            unsafe_allow_html=True,
        )


def render_profile_inputs(profile: Dict[str, str]) -> Dict[str, str]:
    with st.container(border=True):
        st.markdown(
            """
            <h3 style="margin: 0 0 6px 0; font-size: 1.55rem; font-weight: 800; color: #e2e8f0;">
                Tell Us About You
            </h3>
            """,
            unsafe_allow_html=True,
        )
        st.caption("Use text-only inputs. No dropdowns.")

        col1, col2 = st.columns(2)
        with col1:
            education = st.text_input("🎓 Education", value=profile.get("education", ""))
            industry = st.text_input("🏭 Industry", value=profile.get("industry", ""))
            github_url = st.text_input("🐙 GitHub URL (optional)", value=profile.get("github_url", ""))
        with col2:
            interest = st.text_input("💡 Interest", value=profile.get("interest", ""))
            skills_text = st.text_input("🛠️ Skills (comma-separated)", value=profile.get("skills_text", ""))
            linkedin_url = st.text_input("💼 LinkedIn URL (optional)", value=profile.get("linkedin_url", ""))

    return {
        "education": education.strip(),
        "interest": interest.strip(),
        "industry": industry.strip(),
        "skills_text": skills_text.strip(),
        "github_url": github_url.strip(),
        "linkedin_url": linkedin_url.strip(),
    }


def render_card_grid(recommendations: Iterable[Dict[str, object]]) -> None:
    cols = st.columns(2, gap="large")
    for index, rec in enumerate(recommendations):
        target = cols[index % 2]
        with target:
            with st.container(border=True):
                top_left, top_right = st.columns([3, 1])
                with top_left:
                    st.markdown(f"## {rec['emoji']} {rec['title']}")
                with top_right:
                    st.metric("Match", f"{rec.get('match_score', 90)}%")

                st.progress(min(100, int(rec.get("match_score", 90))))
                st.markdown(f"**Career overview:** {rec.get('career_overview', '')}")
                st.markdown(f"**Why this career?** {rec.get('why_this_career', '')}")
                st.markdown("**Development plan:**")
                for step in rec.get("development_plan", []):
                    st.write(f"- {step}")
                st.markdown("**Key skills:**")
                st.markdown(" ".join(f"`{skill}`" for skill in rec.get("skills", [])))


def render_footer() -> None:
    st.markdown(
        """
        <div style="text-align:center; color:#94a3b8; font-size:0.9rem; padding: 10px 0 6px 0;">
            © 2026 PathPilot | Built by Pathpilot team
        </div>
        """,
        unsafe_allow_html=True,
    )
