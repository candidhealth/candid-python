# This file was auto-generated by Fern from our API Definition.

from ......core.pydantic_utilities import UniversalBaseModel
from .patient_payment_id import PatientPaymentId
from .....commons.types.organization_id import OrganizationId
import typing
from .....financials.types.patient_transaction_source import PatientTransactionSource
from .....commons.types.patient_external_id import PatientExternalId
import datetime as dt
from .....financials.types.allocation import Allocation
from .....commons.types.invoice_id import InvoiceId
from ......core.pydantic_utilities import IS_PYDANTIC_V2
import pydantic


class PatientPayment(UniversalBaseModel):
    patient_payment_id: PatientPaymentId
    organization_id: OrganizationId
    source_internal_id: typing.Optional[str] = None
    payment_source: PatientTransactionSource
    amount_cents: int
    patient_external_id: PatientExternalId
    payment_timestamp: typing.Optional[dt.datetime] = None
    payment_note: typing.Optional[str] = None
    allocations: typing.List[Allocation]
    invoice: typing.Optional[InvoiceId] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
