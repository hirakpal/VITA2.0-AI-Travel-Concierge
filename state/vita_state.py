from __future__ import annotations

from typing import Dict, List, Optional

from pydantic import BaseModel, ConfigDict, Field

from models.approval import ApprovalState
from models.confidence import ConfidenceScore
from models.itinerary import Itinerary
from models.mission import MissionEvent
from models.recommendation import RecommendationSet
from models.travel_dna import TravelDNA
from models.traveller_intent import TravellerIntent
from models.traveller_profile import TravellerProfile
from models.trip_summary import TripSummary
from state.workflow_state import WorkflowState


class ChatMessage(BaseModel):
    model_config = ConfigDict(extra="forbid")

    role: str
    content: str


class AgentExecution(BaseModel):
    model_config = ConfigDict(extra="forbid")

    agent_name: str
    status: str = "PENDING"
    confidence: float = 0.0
    execution_time_ms: float = 0.0
    tool_used: Optional[str] = None
    message: str = ""


class VitaState(BaseModel):
    """
    Master application state.

    Every agent receives VitaState.
    Every agent returns VitaState.
    """

    model_config = ConfigDict(
        validate_assignment=True,
        arbitrary_types_allowed=True,
        extra="forbid"
    )

    # ---------- Conversation ----------

    session_id: str = ""

    conversation: List[ChatMessage] = Field(default_factory=list)

    conversation_summary: str = ""

    # ---------- Traveller ----------

    traveller_profile: TravellerProfile = Field(
        default_factory=TravellerProfile
    )

    traveller_intent: TravellerIntent = Field(
        default_factory=TravellerIntent
    )

    travel_dna: TravelDNA = Field(
        default_factory=TravelDNA
    )

    # ---------- Planning ----------

    recommendations: RecommendationSet = Field(
        default_factory=RecommendationSet
    )

    trip_summary: TripSummary = Field(
        default_factory=TripSummary
    )

    itinerary: Itinerary = Field(
        default_factory=Itinerary
    )

    approvals: ApprovalState = Field(
        default_factory=ApprovalState
    )

    # ---------- Workflow ----------

    workflow: WorkflowState = Field(
        default_factory=WorkflowState
    )

    # ---------- Mission Control ----------

    mission_log: List[MissionEvent] = Field(default_factory=list)

    active_agent: str = "Conversation Manager"

    active_tool: Optional[str] = None

    # ---------- Confidence ----------

    confidence: ConfidenceScore = Field(
        default_factory=ConfidenceScore
    )

    # ---------- Execution ----------

    agent_history: List[AgentExecution] = Field(
        default_factory=list
    )

    # ---------- Retrieval ----------

    retrieved_context: List[str] = Field(default_factory=list)

    search_results: List[Dict] = Field(default_factory=list)

    # ---------- Metadata ----------

    metadata: Dict = Field(default_factory=dict)

    user_preferences: Dict = Field(default_factory=dict)

    audit_enabled: bool = True

    developer_mode: bool = False

    # ---------- Helpers ----------

    def add_user_message(self, message: str):

        self.conversation.append(
            ChatMessage(
                role="user",
                content=message
            )
        )

    def add_assistant_message(self, message: str):

        self.conversation.append(
            ChatMessage(
                role="assistant",
                content=message
            )
        )

    def add_mission_event(self, event: MissionEvent):

        self.mission_log.append(event)

    def current_stage(self):

        return self.workflow.current_stage

    def update_active_agent(
        self,
        name: str
    ):

        self.active_agent = name

    def reset(self):

        self.conversation.clear()

        self.mission_log.clear()

        self.agent_history.clear()

        self.retrieved_context.clear()

        self.search_results.clear()

        self.metadata.clear()
