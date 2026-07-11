"""
Audit Agent

Responsibilities
----------------
1. Record every important action
2. Record agent execution
3. Record tool execution
4. Record approvals
5. Record errors
6. Provide audit history
"""

from __future__ import annotations

from datetime import datetime
from typing import Any

from models.agent_response import AgentResponse
from models.audit import AuditEvent
from state.vita_state import VitaState
from services.audit_logger import AuditLogger


class AuditAgent:

    name = "Audit Agent"

    def __init__(self):

        self.logger = AuditLogger()

    # -----------------------------------------------------
    # Generic Event
    # -----------------------------------------------------

    def log_event(
        self,
        state: VitaState,
        component: str,
        action: str,
        status: str,
        message: str,
        execution_time_ms: float = 0.0,
    ) -> AgentResponse:

        event = AuditEvent(

            timestamp=datetime.utcnow(),

            component=component,

            action=action,

            status=status,

            message=message,

            execution_time_ms=execution_time_ms,
        )

        self.logger.log(event)

        return AgentResponse(

            success=True,

            agent=self.name,

            confidence=1.0,

            message="Audit event recorded."
        )

    # -----------------------------------------------------
    # Agent Execution
    # -----------------------------------------------------

    def log_agent_execution(
        self,
        state: VitaState,
        agent_name: str,
        success: bool,
        execution_time_ms: float,
    ):

        self.log_event(

            state,

            component=agent_name,

            action="Agent Execution",

            status="SUCCESS" if success else "FAILED",

            message=f"{agent_name} executed.",

            execution_time_ms=execution_time_ms,
        )

    # -----------------------------------------------------
    # Tool Execution
    # -----------------------------------------------------

    def log_tool_execution(
        self,
        state: VitaState,
        tool_name: str,
        success: bool,
        execution_time_ms: float,
    ):

        self.log_event(

            state,

            component=tool_name,

            action="Tool Execution",

            status="SUCCESS" if success else "FAILED",

            message=f"{tool_name} executed.",

            execution_time_ms=execution_time_ms,
        )

    # -----------------------------------------------------
    # Approval
    # -----------------------------------------------------

    def log_approval(
        self,
        state: VitaState,
        stage: str,
        approved: bool,
    ):

        self.log_event(

            state,

            component="Approval",

            action=stage,

            status="APPROVED" if approved else "REJECTED",

            message=f"{stage} approval",
        )

    # -----------------------------------------------------
    # Error
    # -----------------------------------------------------

    def log_error(
        self,
        state: VitaState,
        component: str,
        error: Exception,
    ):

        self.log_event(

            state,

            component=component,

            action="Exception",

            status="ERROR",

            message=str(error),
        )

    # -----------------------------------------------------
    # Retrieve History
    # -----------------------------------------------------

    def history(self):

        return self.logger.get_logs()

    # -----------------------------------------------------
    # Clear Logs
    # -----------------------------------------------------

    def clear(self):

        self.logger.clear()
