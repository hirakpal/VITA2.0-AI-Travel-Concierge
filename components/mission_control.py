import streamlit as st
from datetime import datetime


def render_mission_control():

    st.subheader("🚀 Mission Control")

    for log in reversed(st.session_state.mission_logs):

        current_time = datetime.now().strftime("%H:%M:%S")

        st.success(f"{current_time}  {log}")

    profile = st.session_state.profile

    if not profile["destination"]:

        next_step = "Tell me where you'd like to travel."

    elif not profile["budget"]:

        next_step = "What's your budget?"

    elif not profile["duration"]:

        next_step = "How many days are you planning?"

    else:

        next_step = "Traveller profile is progressing well."

    st.info(f"### Next Step\n\n{next_step}")
