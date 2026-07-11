from datetime import datetime
from pydantic import BaseModel


class AuditEvent(BaseModel):

    timestamp: datetime

    component: str

    action: str

    status: str

    message: str

    execution_time_ms: float = 0.0
