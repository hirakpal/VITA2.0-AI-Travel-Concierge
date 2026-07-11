"""
Memory Agent

Responsibilities
----------------
1. Read Travel DNA
2. Update Travel DNA
3. Maintain traveller memory
4. Persist memory through Memory Service
"""

from __future__ import annotations

from models.agent_response import AgentResponse
from state.vita_state import VitaState
from services.memory_service import MemoryService


class MemoryAgent:

    name = "Memory Agent"

    def __init__(self):

        self.memory = MemoryService()

    # --------------------------------------------------
    # Load Traveller Memory
    # --------------------------------------------------

    def load(self, state: VitaState) -> VitaState:

        dna = self.memory.load_travel_dna(
            state.session_id
        )

        if dna is not None:

            state.travel_dna = dna

        return state

    # --------------------------------------------------
    # Save Traveller Memory
    # --------------------------------------------------

    def save(self, state: VitaState):

        self.memory.save_travel_dna(

            state.session_id,

            state.travel_dna

        )

    # --------------------------------------------------
    # Update DNA after Recommendation Approval
    # --------------------------------------------------

    def update_after_recommendation(
        self,
        state: VitaState,
    ) -> AgentResponse:

        dna = state.travel_dna

        profile = state.traveller_profile

        # ---------- Travel Style ----------

        for style in profile.travel_style:

            style = style.lower()

            if style == "luxury":
                dna.luxury += 5

            elif style == "adventure":
                dna.adventure += 5

            elif style == "nature":
                dna.nature += 5

            elif style == "food":
                dna.food += 5

            elif style == "culture":
                dna.culture += 5

            elif style == "shopping":
                dna.shopping += 5

            elif style == "nightlife":
                dna.nightlife += 5

        dna.trips_completed += 1

        dna.confidence_score = min(
            1.0,
            dna.confidence_score + 0.05
        )

        self.save(state)

        return AgentResponse(

            success=True,

            agent=self.name,

            confidence=1.0,

            message="Travel DNA updated."

        )

    # --------------------------------------------------
    # Update after itinerary approval
    # --------------------------------------------------

    def update_after_itinerary(
        self,
        state: VitaState
    ) -> AgentResponse:

        dna = state.travel_dna

        dna.trust_score = min(

            1.0,

            dna.trust_score + 0.02

        )

        self.save(state)

        return AgentResponse(

            success=True,

            agent=self.name,

            confidence=1.0,

            message="Traveller memory updated."

        )
