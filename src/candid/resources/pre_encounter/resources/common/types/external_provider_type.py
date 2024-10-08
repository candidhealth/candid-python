# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class ExternalProviderType(str, enum.Enum):
    PRIMARY = "PRIMARY"
    REFERRING = "REFERRING"
    ATTENDING = "ATTENDING"

    def visit(
        self,
        primary: typing.Callable[[], T_Result],
        referring: typing.Callable[[], T_Result],
        attending: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ExternalProviderType.PRIMARY:
            return primary()
        if self is ExternalProviderType.REFERRING:
            return referring()
        if self is ExternalProviderType.ATTENDING:
            return attending()
