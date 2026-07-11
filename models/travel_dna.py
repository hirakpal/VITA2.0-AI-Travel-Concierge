from typing import List

from pydantic import BaseModel, Field, ConfigDict


class TravelDNA(BaseModel):
    """
    Long-term traveller memory.
    Updated ONLY after user approval.
    """

    model_config = ConfigDict(
        validate_assignment=True,
        extra="forbid"
    )

    # Behaviour Scores

    adventure: int = 0
    luxury: int = 0
    culture: int = 0
    food: int = 0
    nature: int = 0
    relaxation: int = 0
    shopping: int = 0
    nightlife: int = 0
    photography: int = 0
    history: int = 0

    # Preferences

    preferred_continents: List[str] = Field(default_factory=list)

    preferred_countries: List[str] = Field(default_factory=list)

    preferred_trip_length: int = 0

    preferred_budget_range: str = ""

    # Intelligence

    trust_score: float = 0.5

    confidence_score: float = 0.0

    trips_completed: int = 0
