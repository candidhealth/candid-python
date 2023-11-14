# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class TaskStatus(str, enum.Enum):
    FINISHED = "finished"
    ADDRESSED_BY_PROVIDER_GROUP = "addressed_by_provider_group"
    SENT_TO_PROVIDER_GROUP = "sent_to_provider_group"
    OPEN_TASK = "open"
    BLOCKED = "blocked"
    WAITING_FOR_REVIEW = "waiting_for_review"
    IN_PROGRESS = "in_progress"

    def visit(
        self,
        finished: typing.Callable[[], T_Result],
        addressed_by_provider_group: typing.Callable[[], T_Result],
        sent_to_provider_group: typing.Callable[[], T_Result],
        open_task: typing.Callable[[], T_Result],
        blocked: typing.Callable[[], T_Result],
        waiting_for_review: typing.Callable[[], T_Result],
        in_progress: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is TaskStatus.FINISHED:
            return finished()
        if self is TaskStatus.ADDRESSED_BY_PROVIDER_GROUP:
            return addressed_by_provider_group()
        if self is TaskStatus.SENT_TO_PROVIDER_GROUP:
            return sent_to_provider_group()
        if self is TaskStatus.OPEN_TASK:
            return open_task()
        if self is TaskStatus.BLOCKED:
            return blocked()
        if self is TaskStatus.WAITING_FOR_REVIEW:
            return waiting_for_review()
        if self is TaskStatus.IN_PROGRESS:
            return in_progress()
