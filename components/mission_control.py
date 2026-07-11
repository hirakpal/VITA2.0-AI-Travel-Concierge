import streamlit as st

def render_mission_control():

    st.subheader("🚀 Mission Control")

    for log in reversed(st.session_state.mission_logs):
        st.success(log)

    st.info(
        "Next Step:\n\nStart a conversation with VITA."
    )
