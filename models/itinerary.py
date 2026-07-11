from pydantic import BaseModel
from typing import List


class Activity(BaseModel):

    time: str

    title: str

    description: str


class DayPlan(BaseModel):

    day: int

    activities: List[Activity] = []


class Itinerary(BaseModel):

    destination: str = ""

    days: List[DayPlan] = []
