import streamlit as st

from utils.session import initialize_session
from components.chat import render_chat
from components.workspace import render_workspace
from components.mission_control import render_mission_control

st.set_page_config(
    page_title="VITA - AI Travel Concierge",
    page_icon="🌍",
    layout="wide"
)

initialize_session()

st.markdown("# 🌍 VITA")
st.caption("Your Intelligent AI Travel Concierge")

left, middle, right = st.columns([4, 3, 3])

with left:
    render_chat()

with middle:
    render_workspace()

with right:
    render_mission_control()
