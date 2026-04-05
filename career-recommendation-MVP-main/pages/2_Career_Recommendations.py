import streamlit as st

from pathpilot_ui import apply_theme, render_card_grid, render_footer, render_top_nav
from pathpilot_utils import build_recommendations

st.set_page_config(
    page_title="PathPilot | Recommendations",
    page_icon="🧭",
    layout="wide",
    initial_sidebar_state="collapsed",
)

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

if "last_regenerated_at" not in st.session_state:
    st.session_state.last_regenerated_at = ""


def main() -> None:
    import random
    import time

    apply_theme(hide_sidebar=True)
    render_top_nav(is_results_page=True)
    st.markdown("### Career Recommendations")

    if st.session_state.last_regenerated_at:
        st.caption(f"Last regenerated: {st.session_state.last_regenerated_at}")

    profile = st.session_state.profile
    required_fields = [profile.get("education", ""), profile.get("interest", ""), profile.get("industry", ""), profile.get("skills_text", "")]
    if not all(required_fields):
        st.warning("Profile is incomplete. Please go back to Page 1.")
        if st.button("Back to Page 1"):
            st.switch_page("app.py")
        return

    if not st.session_state.recommendations:
        with st.spinner("Generating recommendations..."):
            time.sleep(1.0)
            st.session_state.recommendations = build_recommendations(profile)

    render_card_grid(st.session_state.recommendations[:5])

    col1, col2 = st.columns(2)
    with col1:
        if st.button("Back to Profile", use_container_width=True):
            st.switch_page("app.py")
    with col2:
        if st.button("Regenerate", use_container_width=True, key="regenerate_recommendations_btn"):
            with st.spinner("Refreshing recommendations..."):
                refreshed = build_recommendations(profile)

                # Keep the strongest match first, but diversify the remaining suggestions.
                if len(refreshed) > 2:
                    tail = refreshed[1:]
                    random.shuffle(tail)
                    refreshed = [refreshed[0]] + tail

                st.session_state.recommendations = refreshed
                st.session_state.last_regenerated_at = time.strftime("%H:%M:%S")
            st.rerun()

    st.write("---")
    render_footer()


if __name__ == "__main__":
    main()
