# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import typing

import pydantic
from ....core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...commons.types.invoice_id import InvoiceId


class InvoiceUpdate_Set(UniversalBaseModel):
    value: InvoiceId
    type: typing.Literal["set"] = "set"

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True


class InvoiceUpdate_Remove(UniversalBaseModel):
    type: typing.Literal["remove"] = "remove"

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


InvoiceUpdate = typing.Union[InvoiceUpdate_Set, InvoiceUpdate_Remove]
