# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class WriteOffSortField(str, enum.Enum):
    AMOUNT_CENTS = "amount_cents"
    WRITE_OFF_TIMESTAMP = "write_off_timestamp"
    WRITE_OFF_NOTE = "write_off_note"
    _UNKNOWN = "__WRITEOFFSORTFIELD_UNKNOWN__"
    """
    This member is used for forward compatibility. If the value is not recognized by the enum, it will be stored here, and the raw value is accessible through `.value`.
    """

    @classmethod
    def _missing_(cls, value: typing.Any) -> "WriteOffSortField":
        unknown = cls._UNKNOWN
        unknown._value_ = value
        return unknown

    def visit(
        self,
        amount_cents: typing.Callable[[], T_Result],
        write_off_timestamp: typing.Callable[[], T_Result],
        write_off_note: typing.Callable[[], T_Result],
        _unknown_member: typing.Callable[[str], T_Result],
    ) -> T_Result:
        if self is WriteOffSortField.AMOUNT_CENTS:
            return amount_cents()
        if self is WriteOffSortField.WRITE_OFF_TIMESTAMP:
            return write_off_timestamp()
        if self is WriteOffSortField.WRITE_OFF_NOTE:
            return write_off_note()
        return _unknown_member(self._value_)
