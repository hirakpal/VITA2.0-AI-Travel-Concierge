import streamlit as st

def render_chat():

    st.subheader("💬 Conversation")

    st.info("Start chatting with VITA.")

    user_input = st.chat_input("Where would you like to travel?")

    if user_input:

        st.session_state.messages.append(
            {
                "role": "user",
                "content": user_input
            }
        )

        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": "👋 Hello! I'm VITA. Let's plan your next adventure together."
            }
        )

        st.rerun()

    for msg in st.session_state.messages:

        with st.chat_message(msg["role"]):
            st.write(msg["content"])
