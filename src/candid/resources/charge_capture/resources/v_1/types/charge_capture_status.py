# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class ChargeCaptureStatus(str, enum.Enum):
    PLANNED = "planned"
    NOT_BILLABLE = "not-billable"
    BILLABLE = "billable"
    ABORTED = "aborted"
    BILLED = "billed"
    ENTERED_IN_ERROR = "entered-in-error"
    UNKNOWN = "unknown"
    _UNKNOWN = "__CHARGECAPTURESTATUS_UNKNOWN__"
    """
    This member is used for forward compatibility. If the value is not recognized by the enum, it will be stored here, and the raw value is accessible through `.value`.
    """

    @classmethod
    def _missing_(cls, value: typing.Any) -> "ChargeCaptureStatus":
        unknown = cls._UNKNOWN
        unknown._value_ = value
        return unknown

    def visit(
        self,
        planned: typing.Callable[[], T_Result],
        not_billable: typing.Callable[[], T_Result],
        billable: typing.Callable[[], T_Result],
        aborted: typing.Callable[[], T_Result],
        billed: typing.Callable[[], T_Result],
        entered_in_error: typing.Callable[[], T_Result],
        unknown: typing.Callable[[], T_Result],
        _unknown_member: typing.Callable[[str], T_Result],
    ) -> T_Result:
        if self is ChargeCaptureStatus.PLANNED:
            return planned()
        if self is ChargeCaptureStatus.NOT_BILLABLE:
            return not_billable()
        if self is ChargeCaptureStatus.BILLABLE:
            return billable()
        if self is ChargeCaptureStatus.ABORTED:
            return aborted()
        if self is ChargeCaptureStatus.BILLED:
            return billed()
        if self is ChargeCaptureStatus.ENTERED_IN_ERROR:
            return entered_in_error()
        if self is ChargeCaptureStatus.UNKNOWN:
            return unknown()
        return _unknown_member(self._value_)
