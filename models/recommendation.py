from pydantic import BaseModel
from typing import List


class RecommendationCard(BaseModel):

    id: str

    title: str

    category: str

    description: str

    price: float

    currency: str = "INR"

    rating: float

    selected: bool = False


class RecommendationSet(BaseModel):

    recommendations: List[RecommendationCard] = []
