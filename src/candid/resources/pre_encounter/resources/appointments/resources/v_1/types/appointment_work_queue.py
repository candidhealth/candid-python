# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class AppointmentWorkQueue(str, enum.Enum):
    EMERGENT_ISSUE = "EMERGENT_ISSUE"
    NEW_PATIENT = "NEW_PATIENT"
    RETURNING_PATIENT = "RETURNING_PATIENT"
    MANUAL_ESCALATION = "MANUAL_ESCALATION"
    _UNKNOWN = "__APPOINTMENTWORKQUEUE_UNKNOWN__"
    """
    This member is used for forward compatibility. If the value is not recognized by the enum, it will be stored here, and the raw value is accessible through `.value`.
    """

    @classmethod
    def _missing_(cls, value: typing.Any) -> "AppointmentWorkQueue":
        unknown = cls._UNKNOWN
        unknown._value_ = value
        return unknown

    def visit(
        self,
        emergent_issue: typing.Callable[[], T_Result],
        new_patient: typing.Callable[[], T_Result],
        returning_patient: typing.Callable[[], T_Result],
        manual_escalation: typing.Callable[[], T_Result],
        _unknown_member: typing.Callable[[str], T_Result],
    ) -> T_Result:
        if self is AppointmentWorkQueue.EMERGENT_ISSUE:
            return emergent_issue()
        if self is AppointmentWorkQueue.NEW_PATIENT:
            return new_patient()
        if self is AppointmentWorkQueue.RETURNING_PATIENT:
            return returning_patient()
        if self is AppointmentWorkQueue.MANUAL_ESCALATION:
            return manual_escalation()
        return _unknown_member(self._value_)
