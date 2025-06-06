# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class PayerPlanGroupSortField(str, enum.Enum):
    PLAN_GROUP_NAME = "plan_group_name"
    PLAN_TYPE = "plan_type"
    CREATED_AT = "created_at"
    _UNKNOWN = "__PAYERPLANGROUPSORTFIELD_UNKNOWN__"
    """
    This member is used for forward compatibility. If the value is not recognized by the enum, it will be stored here, and the raw value is accessible through `.value`.
    """

    @classmethod
    def _missing_(cls, value: typing.Any) -> "PayerPlanGroupSortField":
        unknown = cls._UNKNOWN
        unknown._value_ = value
        return unknown

    def visit(
        self,
        plan_group_name: typing.Callable[[], T_Result],
        plan_type: typing.Callable[[], T_Result],
        created_at: typing.Callable[[], T_Result],
        _unknown_member: typing.Callable[[str], T_Result],
    ) -> T_Result:
        if self is PayerPlanGroupSortField.PLAN_GROUP_NAME:
            return plan_group_name()
        if self is PayerPlanGroupSortField.PLAN_TYPE:
            return plan_type()
        if self is PayerPlanGroupSortField.CREATED_AT:
            return created_at()
        return _unknown_member(self._value_)
