# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class ClaimSubmissionPayerResponsibilityType(str, enum.Enum):
    PRIMARY = "primary"
    SECONDARY = "secondary"
    _UNKNOWN = "__CLAIMSUBMISSIONPAYERRESPONSIBILITYTYPE_UNKNOWN__"
    """
    This member is used for forward compatibility. If the value is not recognized by the enum, it will be stored here, and the raw value is accessible through `.value`.
    """

    @classmethod
    def _missing_(cls, value: typing.Any) -> "ClaimSubmissionPayerResponsibilityType":
        unknown = cls._UNKNOWN
        unknown._value_ = value
        return unknown

    def visit(
        self,
        primary: typing.Callable[[], T_Result],
        secondary: typing.Callable[[], T_Result],
        _unknown_member: typing.Callable[[str], T_Result],
    ) -> T_Result:
        if self is ClaimSubmissionPayerResponsibilityType.PRIMARY:
            return primary()
        if self is ClaimSubmissionPayerResponsibilityType.SECONDARY:
            return secondary()
        return _unknown_member(self._value_)
