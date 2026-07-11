from enum import Enum

from pydantic import BaseModel, ConfigDict


class WorkflowStage(str, Enum):

    DISCOVERY = "DISCOVERY"

    RECOMMENDATION = "RECOMMENDATION"

    TRIP_SUMMARY = "TRIP_SUMMARY"

    ITINERARY = "ITINERARY"

    COMPLETED = "COMPLETED"


class WorkflowState(BaseModel):

    model_config = ConfigDict(
        validate_assignment=True,
        extra="forbid"
    )

    current_stage: WorkflowStage = WorkflowStage.DISCOVERY

    next_stage: WorkflowStage | None = None

    waiting_for_user: bool = True

    last_agent: str = ""

    completed: bool = False

    retries: int = 0
