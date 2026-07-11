import streamlit as st

def initialize_session():

    if "messages" not in st.session_state:
        st.session_state.messages = []

    if "profile" not in st.session_state:
        st.session_state.profile = {
            "destination":"",
            "budget":"",
            "duration":"",
            "travellers":"",
            "travel_month":"",
            "travel_style":"",
            "completion":0
        }

    if "mission_logs" not in st.session_state:
        st.session_state.mission_logs = [
            "🚀 Mission Control initialized."
        ]
