"""
Tool Result Model

Every external tool (Weather, Flights, Hotels,
Google Maps, Places, etc.) returns ToolResult.
"""

from __future__ import annotations

from datetime import datetime
from typing import Any, Dict

from pydantic import BaseModel, ConfigDict, Field


class ToolResult(BaseModel):
    model_config = ConfigDict(
        validate_assignment=True,
        extra="forbid"
    )

    # -------------------------------------------------
    # Tool Information
    # -------------------------------------------------

    tool_name: str = ""

    success: bool = True

    message: str = ""

    # -------------------------------------------------
    # Returned Data
    # -------------------------------------------------

    data: Dict[str, Any] = Field(default_factory=dict)

    raw_response: Dict[str, Any] = Field(default_factory=dict)

    # -------------------------------------------------
    # Metrics
    # -------------------------------------------------

    execution_time_ms: float = 0.0

    timestamp: datetime = Field(default_factory=datetime.utcnow)

    confidence: float = 1.0

    cached: bool = False

    # -------------------------------------------------
    # Error Information
    # -------------------------------------------------

    error: str | None = None

    # -------------------------------------------------
    # Helper Methods
    # -------------------------------------------------

    def set_error(
        self,
        error: Exception | str
    ):

        self.success = False

        self.error = str(error)

        self.message = str(error)

    def add_data(
        self,
        key: str,
        value: Any
    ):

        self.data[key] = value

    def add_raw_response(
        self,
        response: Dict[str, Any]
    ):

        self.raw_response = response

    @property
    def has_error(self):

        return not self.success

    @property
    def is_empty(self):

        return len(self.data) == 0
