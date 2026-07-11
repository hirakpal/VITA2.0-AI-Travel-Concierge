from pydantic import BaseModel, ConfigDict


class ApprovalState(BaseModel):
    """
    Human approval checkpoints.
    """

    model_config = ConfigDict(
        validate_assignment=True,
        extra="forbid"
    )

    recommendation_approved: bool = False

    trip_summary_approved: bool = False

    itinerary_approved: bool = False

    travel_dna_updated: bool = False
