# This file was auto-generated by Fern from our API Definition.

from ......core.pydantic_utilities import UniversalBaseModel
from .invoice_item_attribution_create import InvoiceItemAttributionCreate
from ......core.pydantic_utilities import IS_PYDANTIC_V2
import typing
import pydantic


class InvoiceItemCreate(UniversalBaseModel):
    attribution: InvoiceItemAttributionCreate
    amount_cents: int

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
