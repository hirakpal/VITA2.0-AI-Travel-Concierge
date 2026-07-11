import streamlit as st
st.write("### Traveller Readiness")
FIELDS = {

"Destination":"destination",

"Budget":"budget",

"Duration":"duration",

"Travellers":"travellers",

"Travel Month":"travel_month",

"Travel Style":"travel_style"

}

for label,key in FIELDS.items():

    if profile[key]:

        st.success(f"✅ {label}")

    else:

        st.warning(f"⚠ {label}")


def completion(profile):

    filled = 0

    for field in FIELDS:

        if profile[field]:

            filled += 1

    return int((filled / len(FIELDS)) * 100)


def render_workspace():

    st.subheader("🧳 Traveller Workspace")

    profile = st.session_state.profile

    profile["completion"] = completion(profile)

    st.progress(profile["completion"] / 100)

    st.metric(
        "Profile Completion",
        f"{profile['completion']}%"
    )

    st.write("### 📍 Destination")

    st.info(profile["destination"] or "Not selected")

    st.write("### 💰 Budget")

    st.info(profile["budget"] or "Not provided")

    st.write("### 👥 Travellers")

    st.info(profile["travellers"] or "Unknown")

    st.write("### 📅 Travel Month")

    st.info(profile["travel_month"] or "Not selected")

    st.write("### ⏳ Duration")

    st.info(profile["duration"] or "Not selected")

    st.write("### 🎯 Travel Style")

    st.info(profile["travel_style"] or "Unknown")
