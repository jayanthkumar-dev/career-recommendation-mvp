import streamlit as st

from pathpilot_ui import (
    apply_theme,
    render_footer,
    render_hybrid_blueprint,
    render_hybrid_intro,
    render_mentor_loading,
    render_ai_conversation,
    render_smart_profile_input,
)
from pathpilot_utils import build_dynamic_questions, build_hybrid_coach_report

st.set_page_config(page_title="PathPilot", page_icon="🧭", layout="wide", initial_sidebar_state="collapsed")

if "coach_stage" not in st.session_state:
    st.session_state.coach_stage = "intro"

if "profile_data" not in st.session_state:
    st.session_state.profile_data = {
        "name": "",
        "education": "Undergraduate",
        "domain_interest": "Technology",
        "mentor_mode": "Corporate Strategist",
        "skills": [],
        "skills_text": "",
        "custom_skills_text": "",
        "experience_level": "Beginner",
        "confidence_level": "Medium",
        "expected_salary": "12",
        "career_priority": "passion",
        "github_url": "",
        "linkedin_url": "",
        "portfolio_url": "",
    }

if "dynamic_questions" not in st.session_state:
    st.session_state.dynamic_questions = []

if "mentor_answers" not in st.session_state:
    st.session_state.mentor_answers = {}

if "mentor_question_index" not in st.session_state:
    st.session_state.mentor_question_index = 0

if "mentor_report" not in st.session_state:
    st.session_state.mentor_report = {}

if "loading_index" not in st.session_state:
    st.session_state.loading_index = 0

LOADING_MESSAGES = [
    "Analyzing your profile...",
    "Matching your skills...",
    "Generating your roadmap...",
]


def render_profile_page() -> None:
    import time

    apply_theme(hide_sidebar=True)

    stage = st.session_state.coach_stage

    if stage == "intro":
        if render_hybrid_intro():
            st.session_state.coach_stage = "profile"
            st.rerun()

    elif stage == "profile":
        profile, submitted = render_smart_profile_input(st.session_state.profile_data)
        if submitted:
            if not profile.get("name") or not profile.get("skills_text"):
                st.error("Please add your name and at least one skill to continue.")
            else:
                st.session_state.profile_data = profile
                st.session_state.dynamic_questions = build_dynamic_questions(profile)
                st.session_state.mentor_answers = {}
                st.session_state.mentor_question_index = 0
                st.session_state.coach_stage = "conversation"
                st.rerun()

    elif stage == "conversation":
        index = st.session_state.mentor_question_index
        questions = st.session_state.dynamic_questions
        current_question = questions[index]
        question_id = str(current_question["id"])
        selected = st.session_state.mentor_answers.get(question_id, "")

        history = []
        for q in questions[:index]:
            qid = str(q.get("id", ""))
            answer_val = st.session_state.mentor_answers.get(qid, "")
            answer_text = ""
            for opt in q.get("options", []):
                if opt.get("value") == answer_val:
                    answer_text = str(opt.get("label", ""))
                    break
            if answer_text:
                history.append({"question": str(q.get("prompt", "")), "answer": answer_text})

        chosen_value = render_ai_conversation(history, current_question, selected)

        col1, col2 = st.columns(2)
        with col1:
            if st.button("Previous", use_container_width=True, disabled=index == 0):
                if index > 0:
                    st.session_state.mentor_question_index -= 1
                    st.rerun()
        with col2:
            next_label = "Generate Career Blueprint" if index == len(questions) - 1 else "Next Question"
            if st.button(next_label, use_container_width=True, key=f"next_{question_id}"):
                st.session_state.mentor_answers[question_id] = chosen_value

                if index < len(questions) - 1:
                    st.session_state.mentor_question_index += 1
                    st.rerun()

                st.session_state.loading_index = 0
                st.session_state.coach_stage = "loading"
                st.rerun()

    elif stage == "loading":
        current_index = min(st.session_state.loading_index, len(LOADING_MESSAGES) - 1)
        render_mentor_loading(LOADING_MESSAGES[current_index])
        time.sleep(0.8)

        if current_index < len(LOADING_MESSAGES) - 1:
            st.session_state.loading_index += 1
            st.rerun()

        st.session_state.mentor_report = build_hybrid_coach_report(
            st.session_state.profile_data,
            st.session_state.mentor_answers,
        )
        st.session_state.coach_stage = "results"
        st.rerun()

    elif stage == "results":
        render_hybrid_blueprint(st.session_state.mentor_report)

        col1, col2 = st.columns(2)
        with col1:
            if st.button("Retake AI Conversation", use_container_width=True, key="pp_reset"):
                st.session_state.coach_stage = "conversation"
                st.session_state.mentor_answers = {}
                st.session_state.mentor_question_index = 0
                st.session_state.mentor_report = {}
                st.rerun()
        with col2:
            if st.button("Edit Profile", use_container_width=True, key="pp_back_hero"):
                st.session_state.coach_stage = "profile"
                st.rerun()

    render_footer()


if __name__ == "__main__":
    render_profile_page()
