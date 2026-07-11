from pydantic import BaseModel


class TravelDNA(BaseModel):

    adventure: int = 0

    luxury: int = 0

    culture: int = 0

    nature: int = 0

    relaxation: int = 0

    food: int = 0

    photography: int = 0

    shopping: int = 0

    nightlife: int = 0

    history: int = 0

    budget_score: int = 0

    trust_score: float = 0.5

    confidence: float = 0.0
