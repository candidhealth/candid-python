# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class InvoiceStatus(str, enum.Enum):
    DRAFT = "draft"
    OPEN = "open"
    PAID = "paid"
    VOID = "void"
    UNCOLLECTIBLE = "uncollectible"
    HELD = "held"

    def visit(
        self,
        draft: typing.Callable[[], T_Result],
        open: typing.Callable[[], T_Result],
        paid: typing.Callable[[], T_Result],
        void: typing.Callable[[], T_Result],
        uncollectible: typing.Callable[[], T_Result],
        held: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is InvoiceStatus.DRAFT:
            return draft()
        if self is InvoiceStatus.OPEN:
            return open()
        if self is InvoiceStatus.PAID:
            return paid()
        if self is InvoiceStatus.VOID:
            return void()
        if self is InvoiceStatus.UNCOLLECTIBLE:
            return uncollectible()
        if self is InvoiceStatus.HELD:
            return held()
