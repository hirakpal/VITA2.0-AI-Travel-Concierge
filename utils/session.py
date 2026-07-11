# utils/session.py

import streamlit as st


def initialize_session():
    """
    Initialize all Streamlit session state variables.
    This function is called once from app.py.
    """

    # ==========================
    # Conversation
    # ==========================
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # ==========================
    # Discovery Wizard
    # ==========================
    if "conversation_state" not in st.session_state:
        st.session_state.conversation_state = "destination"

    if "current_step" not in st.session_state:
        st.session_state.current_step = 1

    if "total_steps" not in st.session_state:
        st.session_state.total_steps = 6

    # ==========================
    # Traveller Profile
    # ==========================
    if "profile" not in st.session_state:
        st.session_state.profile = {
            "destination": "",
            "travellers": "",
            "duration": "",
            "travel_month": "",
            "budget": "",
            "travel_style": "",
            "interests": [],
            "completion": 0
        }

    # ==========================
    # Mission Control
    # ==========================
    if "mission_logs" not in st.session_state:
        st.session_state.mission_logs = [
            "🚀 VITA started successfully.",
            "👋 Ready to discover your next trip."
        ]

    # ==========================
    # Recommendation Engine
    # ==========================
    if "recommendations" not in st.session_state:
        st.session_state.recommendations = []

    # ==========================
    # Trip Summary
    # ==========================
    if "trip_summary" not in st.session_state:
        st.session_state.trip_summary = {}

    # ==========================
    # Itinerary
    # ==========================
    if "itinerary" not in st.session_state:
        st.session_state.itinerary = []

    # ==========================
    # Travel DNA
    # ==========================
    if "travel_dna" not in st.session_state:
        st.session_state.travel_dna = {
            "Adventure": 0,
            "Nature": 0,
            "Luxury": 0,
            "Relaxation": 0,
            "Culture": 0,
            "Food": 0,
            "Photography": 0,
            "Shopping": 0,
            "Nightlife": 0,
            "Budget": 0
        }

    # ==========================
    # Workflow Stage
    # ==========================
    if "current_stage" not in st.session_state:
        st.session_state.current_stage = "Discovery"

    # ==========================
    # Session Metadata
    # ==========================
    if "session_id" not in st.session_state:
        import uuid
        st.session_state.session_id = str(uuid.uuid4())[:8]

    if "developer_mode" not in st.session_state:
        st.session_state.developer_mode = False

    if "confidence_score" not in st.session_state:
        st.session_state.confidence_score = 0

    if "profile_ready" not in st.session_state:
        st.session_state.profile_ready = False


def reset_trip():
    """
    Reset only trip-related information while keeping
    application settings intact.
    """

    st.session_state.messages = []

    st.session_state.profile = {
        "destination": "",
        "travellers": "",
        "duration": "",
        "travel_month": "",
        "budget": "",
        "travel_style": "",
        "interests": [],
        "completion": 0
    }

    st.session_state.conversation_state = "destination"
    st.session_state.current_step = 1
    st.session_state.current_stage = "Discovery"

    st.session_state.mission_logs = [
        "🔄 New trip planning session started."
    ]

    st.session_state.recommendations = []
    st.session_state.trip_summary = {}
    st.session_state.itinerary = []
    st.session_state.profile_ready = False
    st.session_state.confidence_score = 0
