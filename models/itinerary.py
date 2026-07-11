from pydantic import BaseModel
from typing import List


class Activity(BaseModel):

    time: str

    title: str

    description: str

    location: str = ""
    
    latitude: float | None = None
    
    longitude: float | None = None
    
    estimated_duration: int = 0


class DayPlan(BaseModel):

    day: int

    activities: List[Activity] = []


class Itinerary(BaseModel):

    destination: str = ""

    days: List[DayPlan] = []
