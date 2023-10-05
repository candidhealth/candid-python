# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class EncounterOwnerOfNextActionType(str, enum.Enum):
    CANDID = "CANDID"
    CUSTOMER = "CUSTOMER"
    CODER = "CODER"
    NONE = "NONE"

    def visit(
        self,
        candid: typing.Callable[[], T_Result],
        customer: typing.Callable[[], T_Result],
        coder: typing.Callable[[], T_Result],
        none: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is EncounterOwnerOfNextActionType.CANDID:
            return candid()
        if self is EncounterOwnerOfNextActionType.CUSTOMER:
            return customer()
        if self is EncounterOwnerOfNextActionType.CODER:
            return coder()
        if self is EncounterOwnerOfNextActionType.NONE:
            return none()