import streamlit as st

from pathpilot_ui import (
    apply_theme,
    render_about_section,
    render_contact_section,
    render_footer,
    render_home_intro,
    render_profile_inputs,
    render_top_nav,
)
from pathpilot_utils import build_recommendations

st.set_page_config(page_title="PathPilot", page_icon="🧭", layout="wide", initial_sidebar_state="collapsed")

if "profile" not in st.session_state:
    st.session_state.profile = {
        "education": "",
        "interest": "",
        "industry": "",
        "skills_text": "",
        "github_url": "",
        "linkedin_url": "",
    }

if "recommendations" not in st.session_state:
    st.session_state.recommendations = []

if "home_section" not in st.session_state:
    st.session_state.home_section = "profile"


def render_profile_page() -> None:
    apply_theme(hide_sidebar=True)
    render_top_nav(is_results_page=False)
    current_section = st.session_state.home_section

    if current_section == "about":
        render_about_section()
    elif current_section == "contact":
        render_contact_section()
    else:
        render_home_intro()

        profile = render_profile_inputs(st.session_state.profile)

        if st.button("Generate My Career Path", use_container_width=True):
            required_fields = [profile.get("education", ""), profile.get("interest", ""), profile.get("industry", ""), profile.get("skills_text", "")]
            if all(required_fields):
                st.session_state.profile = profile
                st.session_state.recommendations = build_recommendations(profile)
                st.switch_page("pages/2_Career_Recommendations.py")
            else:
                st.error("Please fill all fields.")

        st.markdown("---")

    render_footer()


if __name__ == "__main__":
    render_profile_page()
