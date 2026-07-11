from pydantic import BaseModel


class ConfidenceScore(BaseModel):

    profile: float = 0.0

    recommendation: float = 0.0

    itinerary: float = 0.0

    overall: float = 0.0
