"""
Traveller Intent Model
"""

from __future__ import annotations

from enum import Enum
from typing import List

from pydantic import BaseModel, ConfigDict, Field


class TripType(str, Enum):
    LEISURE = "LEISURE"
    BUSINESS = "BUSINESS"
    FAMILY = "FAMILY"
    HONEYMOON = "HONEYMOON"
    ADVENTURE = "ADVENTURE"
    PILGRIMAGE = "PILGRIMAGE"
    SOLO = "SOLO"
    GROUP = "GROUP"
    ROAD_TRIP = "ROAD_TRIP"
    STAYCATION = "STAYCATION"
    UNKNOWN = "UNKNOWN"


class TravellerIntent(BaseModel):

    model_config = ConfigDict(
        validate_assignment=True,
        extra="forbid"
    )

    # ----------------------------
    # Intent
    # ----------------------------

    primary_intent: TripType = TripType.UNKNOWN

    secondary_intents: List[TripType] = Field(default_factory=list)

    confidence: float = 0.0

    # ----------------------------
    # Trip Goal
    # ----------------------------

    goal: str = ""

    occasion: str = ""

    mood: str = ""

    # ----------------------------
    # Destination
    # ----------------------------

    destination: str = ""

    destinations: List[str] = Field(default_factory=list)

    # ----------------------------
    # Time
    # ----------------------------

    start_date: str = ""

    end_date: str = ""

    duration_days: int = 0

    flexible_dates: bool = False

    # ----------------------------
    # Budget
    # ----------------------------

    budget: float = 0.0

    currency: str = "USD"

    # ----------------------------
    # Travellers
    # ----------------------------

    adults: int = 1

    children: int = 0

    infants: int = 0

    # ----------------------------
    # Preferences
    # ----------------------------

    preferred_transport: str = ""

    preferred_hotel_type: str = ""

    interests: List[str] = Field(default_factory=list)

    constraints: List[str] = Field(default_factory=list)

    # ----------------------------
    # Status
    # ----------------------------

    complete: bool = False

    def update_confidence(self):

        score = 0

        if self.primary_intent != TripType.UNKNOWN:
            score += 20

        if self.destination:
            score += 20

        if self.start_date:
            score += 15

        if self.end_date:
            score += 15

        if self.budget > 0:
            score += 15

        if self.goal:
            score += 15

        self.confidence = round(score / 100, 2)

        self.complete = self.confidence >= 0.80

    @property
    def missing_fields(self):

        missing = []

        if self.destination == "":
            missing.append("destination")

        if self.start_date == "":
            missing.append("start_date")

        if self.end_date == "":
            missing.append("end_date")

        if self.budget == 0:
            missing.append("budget")

        if self.goal == "":
            missing.append("goal")

        return missing

    def reset(self):

        self.__dict__.update(
            TravellerIntent().model_dump()
        )
