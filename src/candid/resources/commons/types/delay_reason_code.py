# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class DelayReasonCode(str, enum.Enum):
    """
    Code indicating the reason why a request was delayed
    """

    C_1 = "1"
    """
    Proof of Eligibility Unknown or Unavailable
    """

    C_2 = "2"
    """
    Litigation
    """

    C_3 = "3"
    """
    Authorization Delays
    """

    C_4 = "4"
    """
    Delay in Certifying Provider
    """

    C_5 = "5"
    """
    Delay in Supplying Billing Forms
    """

    C_6 = "6"
    """
    Delay in Delivery of Custom-made Appliances
    """

    C_7 = "7"
    """
    Third Party Processing Delay
    """

    C_8 = "8"
    """
    Delay in Eligibility Determination
    """

    C_9 = "9"
    """
    Original Claim Rejected or Denied Due to a Reason Unrelated to the Billing Limitation Rules
    """

    C_10 = "10"
    """
    Administration Delay in the Prior Approval Process
    """

    C_11 = "11"
    """
    Other
    """

    C_15 = "15"
    """
    Natural Disaster
    """

    C_16 = "16"
    """
    Lack of Information
    """

    C_17 = "17"
    """
    No response to initial request
    """

    _UNKNOWN = "__DELAYREASONCODE_UNKNOWN__"
    """
    This member is used for forward compatibility. If the value is not recognized by the enum, it will be stored here, and the raw value is accessible through `.value`.
    """

    @classmethod
    def _missing_(cls, value: typing.Any) -> "DelayReasonCode":
        unknown = cls._UNKNOWN
        unknown._value_ = value
        return unknown

    def visit(
        self,
        c_1: typing.Callable[[], T_Result],
        c_2: typing.Callable[[], T_Result],
        c_3: typing.Callable[[], T_Result],
        c_4: typing.Callable[[], T_Result],
        c_5: typing.Callable[[], T_Result],
        c_6: typing.Callable[[], T_Result],
        c_7: typing.Callable[[], T_Result],
        c_8: typing.Callable[[], T_Result],
        c_9: typing.Callable[[], T_Result],
        c_10: typing.Callable[[], T_Result],
        c_11: typing.Callable[[], T_Result],
        c_15: typing.Callable[[], T_Result],
        c_16: typing.Callable[[], T_Result],
        c_17: typing.Callable[[], T_Result],
        _unknown_member: typing.Callable[[str], T_Result],
    ) -> T_Result:
        if self is DelayReasonCode.C_1:
            return c_1()
        if self is DelayReasonCode.C_2:
            return c_2()
        if self is DelayReasonCode.C_3:
            return c_3()
        if self is DelayReasonCode.C_4:
            return c_4()
        if self is DelayReasonCode.C_5:
            return c_5()
        if self is DelayReasonCode.C_6:
            return c_6()
        if self is DelayReasonCode.C_7:
            return c_7()
        if self is DelayReasonCode.C_8:
            return c_8()
        if self is DelayReasonCode.C_9:
            return c_9()
        if self is DelayReasonCode.C_10:
            return c_10()
        if self is DelayReasonCode.C_11:
            return c_11()
        if self is DelayReasonCode.C_15:
            return c_15()
        if self is DelayReasonCode.C_16:
            return c_16()
        if self is DelayReasonCode.C_17:
            return c_17()
        return _unknown_member(self._value_)
