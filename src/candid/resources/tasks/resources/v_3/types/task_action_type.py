# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class TaskActionType(str, enum.Enum):
    CLOSE_TASK = "close_task"
    CLOSE_TASK_AND_REPROCESS = "close_task_and_reprocess"
    _UNKNOWN = "__TASKACTIONTYPE_UNKNOWN__"
    """
    This member is used for forward compatibility. If the value is not recognized by the enum, it will be stored here, and the raw value is accessible through `.value`.
    """

    @classmethod
    def _missing_(cls, value: typing.Any) -> "TaskActionType":
        unknown = cls._UNKNOWN
        unknown._value_ = value
        return unknown

    def visit(
        self,
        close_task: typing.Callable[[], T_Result],
        close_task_and_reprocess: typing.Callable[[], T_Result],
        _unknown_member: typing.Callable[[str], T_Result],
    ) -> T_Result:
        if self is TaskActionType.CLOSE_TASK:
            return close_task()
        if self is TaskActionType.CLOSE_TASK_AND_REPROCESS:
            return close_task_and_reprocess()
        return _unknown_member(self._value_)
