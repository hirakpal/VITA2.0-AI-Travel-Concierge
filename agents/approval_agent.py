"""
Approval Agent

Responsible for handling all Human-in-the-Loop (HITL) approvals.

Stages:
1. Recommendation Approval
2. Trip Summary Approval
3. Itinerary Approval
"""

from datetime import datetime

from models.agent_response import AgentResponse
from models.mission import MissionEvent, MissionStatus
from state.vita_state import VitaState


class ApprovalAgent:

    name = "Approval Agent"

    def execute(
        self,
        state: VitaState,
        approval_type: str,
        approved: bool,
    ) -> AgentResponse:

        response = AgentResponse(
            success=True,
            agent=self.name,
            confidence=1.0,
            message=""
        )

        if approval_type == "recommendation":

            state.approvals.recommendation_approved = approved

            response.message = (
                "Recommendations approved."
                if approved
                else "Recommendations rejected."
            )

        elif approval_type == "summary":

            state.approvals.trip_summary_approved = approved

            response.message = (
                "Trip summary approved."
                if approved
                else "Trip summary rejected."
            )

        elif approval_type == "itinerary":

            state.approvals.itinerary_approved = approved

            response.message = (
                "Itinerary approved."
                if approved
                else "Itinerary rejected."
            )

        else:

            response.success = False

            response.message = f"Unknown approval type: {approval_type}"

            return response

        state.mission_log.append(

            MissionEvent(

                timestamp=datetime.utcnow(),

                stage=state.workflow.current_stage.value,

                agent_name=self.name,

                tool_name=None,

                message=response.message,

                status=MissionStatus.SUCCESS,

                confidence=1.0,

                execution_time_ms=0.0,
            )
        )

        return response
