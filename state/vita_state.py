from pydantic import BaseModel, Field
from typing import List

from models.traveller_profile import TravellerProfile
from models.travel_dna import TravelDNA
from models.recommendation import RecommendationSet
from models.trip_summary import TripSummary
from models.itinerary import Itinerary
from models.approval import ApprovalState
from models.workflow_state import WorkflowStage
from models.mission import MissionEvent


class VitaState(BaseModel):

    workflow_stage: WorkflowStage = WorkflowStage.DISCOVERY

    traveller_profile: TravellerProfile = Field(default_factory=TravellerProfile)

    travel_dna: TravelDNA = Field(default_factory=TravelDNA)

    recommendations: RecommendationSet = Field(default_factory=RecommendationSet)

    trip_summary: TripSummary = Field(default_factory=TripSummary)

    itinerary: Itinerary = Field(default_factory=Itinerary)

    approvals: ApprovalState = Field(default_factory=ApprovalState)

    mission_log: List[MissionEvent] = Field(default_factory=list)

    conversation_history: List[dict] = Field(default_factory=list)

    confidence_score: float = 0.0
