"""
Approval Models

Human-in-the-Loop (HITL)
"""

from __future__ import annotations

from datetime import datetime
from enum import Enum

from pydantic import BaseModel, ConfigDict, Field


class ApprovalStatus(str, Enum):
    PENDING = "PENDING"
    APPROVED = "APPROVED"
    REJECTED = "REJECTED"


class ApprovalRecord(BaseModel):
    model_config = ConfigDict(
        validate_assignment=True,
        extra="forbid"
    )

    stage: str

    status: ApprovalStatus = ApprovalStatus.PENDING

    approved_by: str = "Traveller"

    comments: str = ""

    timestamp: datetime = Field(default_factory=datetime.utcnow)


class ApprovalState(BaseModel):
    """
    Maintains approval state for the complete workflow.
    """

    model_config = ConfigDict(
        validate_assignment=True,
        extra="forbid"
    )

    recommendation_status: ApprovalStatus = ApprovalStatus.PENDING

    trip_summary_status: ApprovalStatus = ApprovalStatus.PENDING

    itinerary_status: ApprovalStatus = ApprovalStatus.PENDING

    recommendation_approved: bool = False

    trip_summary_approved: bool = False

    itinerary_approved: bool = False

    current_stage: str = "DISCOVERY"

    approval_history: list[ApprovalRecord] = Field(default_factory=list)

    def approve(
        self,
        stage: str,
        comments: str = ""
    ):

        stage = stage.lower()

        if stage == "recommendation":
            self.recommendation_status = ApprovalStatus.APPROVED
            self.recommendation_approved = True

        elif stage == "summary":
            self.trip_summary_status = ApprovalStatus.APPROVED
            self.trip_summary_approved = True

        elif stage == "itinerary":
            self.itinerary_status = ApprovalStatus.APPROVED
            self.itinerary_approved = True

        self.approval_history.append(
            ApprovalRecord(
                stage=stage,
                status=ApprovalStatus.APPROVED,
                comments=comments,
            )
        )

    def reject(
        self,
        stage: str,
        comments: str = ""
    ):

        stage = stage.lower()

        if stage == "recommendation":
            self.recommendation_status = ApprovalStatus.REJECTED
            self.recommendation_approved = False

        elif stage == "summary":
            self.trip_summary_status = ApprovalStatus.REJECTED
            self.trip_summary_approved = False

        elif stage == "itinerary":
            self.itinerary_status = ApprovalStatus.REJECTED
            self.itinerary_approved = False

        self.approval_history.append(
            ApprovalRecord(
                stage=stage,
                status=ApprovalStatus.REJECTED,
                comments=comments,
            )
        )

    @property
    def completed(self) -> bool:
        return (
            self.recommendation_approved
            and self.trip_summary_approved
            and self.itinerary_approved
        )
