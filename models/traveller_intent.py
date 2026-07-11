from enum import Enum
from pydantic import BaseModel


class TripPurpose(str, Enum):
    LEISURE = "Leisure"
    BUSINESS = "Business"
    HONEYMOON = "Honeymoon"
    FAMILY = "Family"
    ADVENTURE = "Adventure"
    PILGRIMAGE = "Pilgrimage"
    EDUCATION = "Education"
    MEDICAL = "Medical"


class TravellerIntent(BaseModel):

    purpose: TripPurpose = TripPurpose.LEISURE

    urgency: str = "Flexible"

    confidence: float = 0.0
