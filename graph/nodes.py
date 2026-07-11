"""
Workflow Nodes

Each node returns the updated VitaState.
"""

from state.vita_state import VitaState


def conversation_node(state: VitaState):

    state.update_active_agent("Conversation Manager")

    return state


def intent_node(state: VitaState):

    state.update_active_agent("Intent Agent")

    return state


def entity_node(state: VitaState):

    state.update_active_agent("Entity Extraction Agent")

    return state


def preference_node(state: VitaState):

    state.update_active_agent("Preference Inference Agent")

    return state


def planner_node(state: VitaState):

    state.update_active_agent("Planner Agent")

    return state


def recommendation_node(state: VitaState):

    state.update_active_agent("Recommendation Agent")

    return state


def itinerary_node(state: VitaState):

    state.update_active_agent("Itinerary Agent")

    return state


def approval_node(state: VitaState):

    state.update_active_agent("Approval Agent")

    return state
