from __future__ import annotations

from datetime import datetime
from enum import Enum

from pydantic import BaseModel, ConfigDict, Field


class MissionStatus(str, Enum):
    SUCCESS = "SUCCESS"
    INFO = "INFO"
    WARNING = "WARNING"
    ERROR = "ERROR"


class MissionEvent(BaseModel):
    """
    Event displayed in Mission Control.
    """

    model_config = ConfigDict(
        validate_assignment=True,
        extra="forbid"
    )

    timestamp: datetime = Field(default_factory=datetime.utcnow)

    stage: str = ""

    agent_name: str = ""

    tool_name: str | None = None

    message: str = ""

    status: MissionStatus = MissionStatus.INFO

    confidence: float = 0.0

    execution_time_ms: float = 0.0
