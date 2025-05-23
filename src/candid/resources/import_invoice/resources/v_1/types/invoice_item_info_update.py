# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic
from ......core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .....invoices.resources.v_2.types.invoice_item_create import InvoiceItemCreate
from .invoice_item_update_type import InvoiceItemUpdateType


class InvoiceItemInfoUpdate(UniversalBaseModel):
    update_type: InvoiceItemUpdateType = pydantic.Field()
    """
    The only supported update operations for invoice items is to either overwrite the entire list of invoice items
    or to append new invoice items
    """

    items: typing.List[InvoiceItemCreate]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
