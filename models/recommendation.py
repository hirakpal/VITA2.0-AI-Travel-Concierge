"""
Recommendation Models
"""

from __future__ import annotations

from enum import Enum
from typing import List

from pydantic import BaseModel, ConfigDict, Field


class RecommendationType(str, Enum):
    DESTINATION = "DESTINATION"
    HOTEL = "HOTEL"
    FLIGHT = "FLIGHT"
    ACTIVITY = "ACTIVITY"
    RESTAURANT = "RESTAURANT"
    TRANSPORT = "TRANSPORT"


class RecommendationStatus(str, Enum):
    SUGGESTED = "SUGGESTED"
    ACCEPTED = "ACCEPTED"
    REPLACED = "REPLACED"
    REMOVED = "REMOVED"


class RecommendationCard(BaseModel):

    model_config = ConfigDict(
        validate_assignment=True,
        extra="forbid"
    )

    id: str = ""

    type: RecommendationType = RecommendationType.DESTINATION

    title: str = ""

    subtitle: str = ""

    description: str = ""

    country: str = ""

    city: str = ""

    image_url: str = ""

    price: float = 0.0

    currency: str = "USD"

    rating: float = 0.0

    duration: str = ""

    confidence: float = 0.0

    source: str = ""

    tags: List[str] = Field(default_factory=list)

    alternatives: List["RecommendationCard"] = Field(default_factory=list)

    status: RecommendationStatus = RecommendationStatus.SUGGESTED


class RecommendationSet(BaseModel):

    model_config = ConfigDict(
        validate_assignment=True,
        extra="forbid"
    )

    cards: List[RecommendationCard] = Field(default_factory=list)

    approved: bool = False

    generated: bool = False

    confidence: float = 0.0

    def add(self, card: RecommendationCard):

        self.cards.append(card)

    def remove(self, card_id: str):

        self.cards = [

            c for c in self.cards

            if c.id != card_id

        ]

    def replace(
        self,
        card_id: str,
        new_card: RecommendationCard
    ):

        for i, card in enumerate(self.cards):

            if card.id == card_id:

                card.status = RecommendationStatus.REPLACED

                self.cards[i] = new_card

                break

    def accept(
        self,
        card_id: str
    ):

        for card in self.cards:

            if card.id == card_id:

                card.status = RecommendationStatus.ACCEPTED

    def selected(self):

        return [

            c

            for c in self.cards

            if c.status == RecommendationStatus.ACCEPTED

        ]

    @property
    def count(self):

        return len(self.cards)


RecommendationCard.model_rebuild()
