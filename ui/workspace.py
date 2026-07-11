import streamlit as st

FIELDS = {
    "Destination": "destination",
    "Budget": "budget",
    "Duration": "duration",
    "Travellers": "travellers",
    "Travel Month": "travel_month",
    "Travel Style": "travel_style"
}


def calculate_completion(profile):
    total = len(FIELDS)
    completed = sum(1 for key in FIELDS.values() if profile.get(key))
    return int((completed / total) * 100)


def render_workspace():

    profile = st.session_state.profile

    # Calculate profile completion
    profile["completion"] = calculate_completion(profile)

    st.subheader("🧳 Traveller Workspace")

    st.progress(profile["completion"] / 100)

    st.metric(
        "Profile Completion",
        f"{profile['completion']}%"
    )

    st.divider()

    st.write("### Traveller Readiness")

    for label, key in FIELDS.items():

        if profile.get(key):
            st.success(f"✅ {label}: {profile[key]}")
        else:
            st.warning(f"⚠ {label}: Pending")
