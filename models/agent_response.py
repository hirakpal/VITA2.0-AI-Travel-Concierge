class AgentResponse(BaseModel):
    success: bool
    next_agent: str | None = None
    confidence: float = 0.0
    message: str = ""
    payload: dict = {}
