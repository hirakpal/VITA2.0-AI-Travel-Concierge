from typing import List, Optional

from pydantic import BaseModel, Field, ConfigDict


class TravellerProfile(BaseModel):
    """
    Current traveller profile collected during discovery.
    This model represents ONLY the current trip.
    """

    model_config = ConfigDict(
        validate_assignment=True,
        extra="forbid"
    )

    # ------------------------
    # Trip Information
    # ------------------------

    trip_name: Optional[str] = None
    trip_type: Optional[str] = None

    # ------------------------
    # Locations
    # ------------------------

    origin: Optional[str] = None
    destination: Optional[str] = None

    # ------------------------
    # Travellers
    # ------------------------

    travellers: Optional[str] = None

    adults: int = 1
    children: int = 0
    infants: int = 0

    companions: List[str] = Field(default_factory=list)

    # ------------------------
    # Travel Details
    # ------------------------

    duration_days: Optional[int] = None

    travel_month: Optional[str] = None

    start_date: Optional[str] = None
    end_date: Optional[str] = None

    # ------------------------
    # Budget
    # ------------------------

    budget: Optional[float] = None

    currency: str = "INR"

    # ------------------------
    # Preferences
    # ------------------------

    travel_style: List[str] = Field(default_factory=list)

    interests: List[str] = Field(default_factory=list)

    food_preferences: List[str] = Field(default_factory=list)

    accommodation_type: Optional[str] = None

    transport_preference: Optional[str] = None

    # ------------------------
    # Constraints
    # ------------------------

    accessibility_requirements: List[str] = Field(default_factory=list)

    constraints: List[str] = Field(default_factory=list)

    # ------------------------
    # Documents
    # ------------------------

    passport_available: Optional[bool] = None

    visa_required: Optional[bool] = None

    # ------------------------
    # Metadata
    # ------------------------

    profile_completion: float = 0.0

    confidence: float = 0.0
