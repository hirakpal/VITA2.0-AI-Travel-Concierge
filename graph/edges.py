from state.workflow_state import WorkflowStage


def next_stage(stage: WorkflowStage):

    if stage == WorkflowStage.DISCOVERY:
        return WorkflowStage.RECOMMENDATION

    if stage == WorkflowStage.RECOMMENDATION:
        return WorkflowStage.TRIP_SUMMARY

    if stage == WorkflowStage.TRIP_SUMMARY:
        return WorkflowStage.ITINERARY

    if stage == WorkflowStage.ITINERARY:
        return WorkflowStage.COMPLETED

    return WorkflowStage.COMPLETED
