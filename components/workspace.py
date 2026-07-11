import streamlit as st

def render_workspace():

    st.subheader("🧳 Traveller Workspace")

    profile = st.session_state.profile

    st.metric(
        "Profile Completion",
        f"{profile['completion']}%"
    )

    st.text_input(
        "Destination",
        value=profile["destination"],
        disabled=True
    )

    st.text_input(
        "Budget",
        value=profile["budget"],
        disabled=True
    )

    st.text_input(
        "Duration",
        value=profile["duration"],
        disabled=True
    )

    st.text_input(
        "Travel Style",
        value=profile["travel_style"],
        disabled=True
    )
