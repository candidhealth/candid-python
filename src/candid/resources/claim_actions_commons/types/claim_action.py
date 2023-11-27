# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import typing

import typing_extensions

from .close_tasks_and_process_claim_action import CloseTasksAndProcessClaimAction
from .move_to_work_queue_claim_action import MoveToWorkQueueClaimAction
from .resubmit_corrected_claim_action import ResubmitCorrectedClaimAction
from .resubmit_fresh_claim_action import ResubmitFreshClaimAction
from .void_claim_action import VoidClaimAction


class ClaimAction_VoidClaimAction(VoidClaimAction):
    type: typing_extensions.Literal["void_claim_action"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class ClaimAction_ResubmitFreshClaimAction(ResubmitFreshClaimAction):
    type: typing_extensions.Literal["resubmit_fresh_claim_action"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class ClaimAction_ResubmitCorrectedClaimAction(ResubmitCorrectedClaimAction):
    type: typing_extensions.Literal["resubmit_corrected_claim_action"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class ClaimAction_CloseTasksAndProcessClaimAction(CloseTasksAndProcessClaimAction):
    type: typing_extensions.Literal["close_tasks_and_process_claim_action"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


class ClaimAction_MoveToWorkQueueClaimAction(MoveToWorkQueueClaimAction):
    type: typing_extensions.Literal["move_to_work_queue_claim_action"]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True


ClaimAction = typing.Union[
    ClaimAction_VoidClaimAction,
    ClaimAction_ResubmitFreshClaimAction,
    ClaimAction_ResubmitCorrectedClaimAction,
    ClaimAction_CloseTasksAndProcessClaimAction,
    ClaimAction_MoveToWorkQueueClaimAction,
]