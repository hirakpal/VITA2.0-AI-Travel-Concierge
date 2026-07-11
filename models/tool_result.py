from pydantic import BaseModel
from typing import Any


class ToolResult(BaseModel):

    tool_name: str

    success: bool

    data: Any = None

    error: str | None = None

    execution_time_ms: float = 0.0
