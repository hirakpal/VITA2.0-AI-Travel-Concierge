from pydantic import BaseModel, Field
from typing import List, Optional


class TravellerProfile(BaseModel):

    destination: Optional[str] = None

    origin: Optional[str] = None
    
    trip_name: str | None = None

    trip_type: str | None = None

    travellers: Optional[str] = None

    adults: int = 1

    children: int = 0

    infants: int = 0

    companions: list[str] = Field(default_factory=list)
    
    constraints: list[str] = Field(default_factory=list)

    duration: Optional[int] = None

    travel_month: Optional[str] = None

    budget: Optional[float] = None

    currency: str = "INR"

    travel_style: List[str] = Field(default_factory=list)

    interests: List[str] = Field(default_factory=list)

    accommodation_type: Optional[str] = None

    transport_preference: Optional[str] = None

    food_preferences: List[str] = Field(default_factory=list)

    accessibility_requirements: List[str] = Field(default_factory=list)

    visa_required: Optional[bool] = None

    passport_available: Optional[bool] = None

    profile_completion: float = 0.0
