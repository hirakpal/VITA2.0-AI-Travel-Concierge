"""
Base Agent

Every VITA agent inherits from this class.

Responsibilities
----------------
1. Common execution lifecycle
2. Timing
3. Error handling
4. Audit hooks
5. Confidence reporting
"""

from __future__ import annotations

import time
from abc import ABC, abstractmethod

from models.agent_response import AgentResponse
from state.vita_state import VitaState


class BaseAgent(ABC):

    name = "Base Agent"

    description = ""

    version = "1.0"

    def __init__(self):

        self.execution_time_ms = 0.0

    # --------------------------------------------------
    # Public Entry Point
    # --------------------------------------------------

    def run(
        self,
        state: VitaState,
        **kwargs
    ) -> AgentResponse:

        start = time.perf_counter()

        try:

            response = self.execute(
                state,
                **kwargs
            )

            if response is None:

                response = AgentResponse(
                    success=False,
                    agent=self.name,
                    confidence=0.0,
                    message="Agent returned None."
                )

        except Exception as ex:

            response = AgentResponse(
                success=False,
                agent=self.name,
                confidence=0.0,
                message=str(ex)
            )

        finally:

            self.execution_time_ms = round(

                (time.perf_counter() - start) * 1000,

                2
            )

        response.execution_time_ms = self.execution_time_ms

        return response

    # --------------------------------------------------
    # Must be implemented by every agent
    # --------------------------------------------------

    @abstractmethod
    def execute(
        self,
        state: VitaState,
        **kwargs
    ) -> AgentResponse:
        pass

    # --------------------------------------------------
    # Utility
    # --------------------------------------------------

    def success(
        self,
        message: str,
        confidence: float = 1.0
    ) -> AgentResponse:

        return AgentResponse(

            success=True,

            agent=self.name,

            confidence=confidence,

            message=message
        )

    def failure(
        self,
        message: str,
        confidence: float = 0.0
    ) -> AgentResponse:

        return AgentResponse(

            success=False,

            agent=self.name,

            confidence=confidence,

            message=message
        )

    # --------------------------------------------------
    # Agent Info
    # --------------------------------------------------

    def info(self):

        return {

            "name": self.name,

            "description": self.description,

            "version": self.version
        }
