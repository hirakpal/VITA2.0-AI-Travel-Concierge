import streamlit as st

def render_mission_control():

    st.subheader("🚀 Mission Control")

    profile = st.session_state.profile

    # -------------------
    # Current Stage
    # -------------------

    if profile["completion"] < 100:

        stage = "🟢 Discovery"

    else:

        stage = "🟡 Recommendation"

    st.info(f"### Current Stage\n\n{stage}")

    # -------------------

    st.write("### Activity")

    for log in reversed(st.session_state.mission_logs):

        st.success(log)

    st.write("### Planning Progress")

    steps = [
        ("Discovery", profile["completion"] > 0),
        ("Traveller Profile", profile["completion"] == 100),
        ("Recommendations", False),
        ("Trip Summary", False),
        ("Itinerary", False),
        ("Final Approval", False)
    ]

    for title, done in steps:

        if done:

            st.markdown(f"✅ {title}")

        else:

            st.markdown(f"⬜ {title}")
