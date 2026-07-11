"""
Standard response returned by every agent.

Every agent MUST return AgentResponse.
"""

from __future__ import annotations

from typing import Any, Dict, Optional

from pydantic import BaseModel, ConfigDict, Field


class AgentResponse(BaseModel):
    model_config = ConfigDict(
        validate_assignment=True,
        extra="forbid"
    )

    # ----------------------------------------
    # Execution Status
    # ----------------------------------------

    success: bool = True

    # ----------------------------------------
    # Agent Information
    # ----------------------------------------

    agent: str = ""

    next_agent: Optional[str] = None

    # ----------------------------------------
    # Confidence
    # ----------------------------------------

    confidence: float = 0.0

    # ----------------------------------------
    # User Message
    # ----------------------------------------

    message: str = ""

    # ----------------------------------------
    # Data returned by agent
    # ----------------------------------------

    payload: Dict[str, Any] = Field(default_factory=dict)

    # ----------------------------------------
    # Metrics
    # ----------------------------------------

    execution_time_ms: float = 0.0

    input_tokens: int = 0

    output_tokens: int = 0

    total_tokens: int = 0

    # ----------------------------------------
    # Tool Information
    # ----------------------------------------

    tool_name: Optional[str] = None

    tool_success: bool = True

    # ----------------------------------------
    # Error
    # ----------------------------------------

    error: Optional[str] = None

    # ----------------------------------------
    # Helper Methods
    # ----------------------------------------

    def set_error(self, error: Exception):

        self.success = False

        self.error = str(error)

        self.message = str(error)

    def add_payload(
        self,
        key: str,
        value: Any
    ):

        self.payload[key] = value

    def update_tokens(
        self,
        prompt_tokens: int,
        completion_tokens: int
    ):

        self.input_tokens = prompt_tokens

        self.output_tokens = completion_tokens

        self.total_tokens = (
            prompt_tokens + completion_tokens
        )

    def mark_tool(
        self,
        tool_name: str,
        success: bool = True
    ):

        self.tool_name = tool_name

        self.tool_success = success
