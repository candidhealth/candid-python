# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class ChargeCaptureSortField(str, enum.Enum):
    CREATED_AT = "created_at"
    DATE_OF_SERVICE = "date_of_service"
    _UNKNOWN = "__CHARGECAPTURESORTFIELD_UNKNOWN__"
    """
    This member is used for forward compatibility. If the value is not recognized by the enum, it will be stored here, and the raw value is accessible through `.value`.
    """

    @classmethod
    def _missing_(cls, value: typing.Any) -> "ChargeCaptureSortField":
        unknown = cls._UNKNOWN
        unknown._value_ = value
        return unknown

    def visit(
        self,
        created_at: typing.Callable[[], T_Result],
        date_of_service: typing.Callable[[], T_Result],
        _unknown_member: typing.Callable[[str], T_Result],
    ) -> T_Result:
        if self is ChargeCaptureSortField.CREATED_AT:
            return created_at()
        if self is ChargeCaptureSortField.DATE_OF_SERVICE:
            return date_of_service()
        return _unknown_member(self._value_)
