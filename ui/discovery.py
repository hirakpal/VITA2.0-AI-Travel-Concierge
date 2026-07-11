import streamlit as st
from services.profile_extractor import extract_profile
from services.conversation_engine import get_next_question

def render_chat():

    st.subheader("💬 Conversation")

    st.info("Start chatting with VITA.")

    user_input = st.chat_input("Where would you like to travel?")

    if user_input:

        st.session_state.messages.append(
            {
                "role":"user",
                "content":user_input
            }
        )

        profile = extract_profile(
            user_input,
            st.session_state.profile
        )

        st.session_state.profile = profile

        st.session_state.mission_logs.append(
            "🧠 Traveller profile updated."
        )

        reply, log = get_next_question(profile)

        st.session_state.mission_logs.append(log)

        st.session_state.messages.append(
            {
                "role":"assistant",
                "content":reply
            }
        )

        st.rerun()

    for msg in st.session_state.messages:

        with st.chat_message(msg["role"]):
            st.write(msg["content"])
