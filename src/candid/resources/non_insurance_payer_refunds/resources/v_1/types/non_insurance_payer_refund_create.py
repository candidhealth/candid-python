# This file was auto-generated by Fern from our API Definition.

from ......core.pydantic_utilities import UniversalBaseModel
from .....non_insurance_payers.resources.v_1.types.non_insurance_payer_id import NonInsurancePayerId
import typing
from .....commons.types.invoice_id import InvoiceId
import datetime as dt
from .....financials.types.allocation_create import AllocationCreate
from .....financials.types.refund_reason import RefundReason
from ......core.pydantic_utilities import IS_PYDANTIC_V2
import pydantic


class NonInsurancePayerRefundCreate(UniversalBaseModel):
    non_insurance_payer_id: NonInsurancePayerId
    invoice_id: typing.Optional[InvoiceId] = None
    amount_cents: int
    refund_timestamp: typing.Optional[dt.datetime] = None
    refund_note: typing.Optional[str] = None
    check_number: typing.Optional[str] = None
    allocations: typing.List[AllocationCreate]
    refund_reason: typing.Optional[RefundReason] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
