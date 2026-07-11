from pydantic import BaseModel
from typing import List


class RecommendationCard(BaseModel):

    id: str

    title: str

    category: str

    description: str

    estimated_cost: float

    rating: float

    selected: bool = False


class RecommendationSet(BaseModel):

    recommendations: List[RecommendationCard] = []
