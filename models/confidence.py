from __future__ import annotations

from pydantic import BaseModel, ConfigDict


class ConfidenceScore(BaseModel):
    """
    Overall confidence calculated across the workflow.
    """

    model_config = ConfigDict(
        validate_assignment=True,
        extra="forbid"
    )

    overall: float = 0.0

    intent: float = 0.0

    entity_extraction: float = 0.0

    preference_inference: float = 0.0

    recommendation: float = 0.0

    itinerary: float = 0.0

    governance: float = 0.0

    hallucination_risk: float = 0.0

    needs_human_review: bool = False

    threshold: float = 0.90

    def update(self):

        scores = [
            self.intent,
            self.entity_extraction,
            self.preference_inference,
            self.recommendation,
            self.itinerary,
            self.governance
        ]

        valid = [s for s in scores if s > 0]

        if valid:
            self.overall = round(sum(valid) / len(valid), 3)

        self.needs_human_review = (
            self.overall < self.threshold
        )
