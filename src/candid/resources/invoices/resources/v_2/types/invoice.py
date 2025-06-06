# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic
from ......core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .....commons.types.organization_id import OrganizationId
from .....commons.types.patient_external_id import PatientExternalId
from .invoice_destination_metadata import InvoiceDestinationMetadata
from .invoice_item_info import InvoiceItemInfo
from .invoice_status import InvoiceStatus


class Invoice(UniversalBaseModel):
    amount_cents: int = pydantic.Field()
    """
    Total monetary amount (in cents) of all Invoice Items
    """

    created_at: dt.datetime
    updated_at: dt.datetime
    organization_id: OrganizationId
    invoice_destination_metadata: InvoiceDestinationMetadata = pydantic.Field()
    """
    Contains all relevant information from the third-party service this invoice was created in
    """

    patient_external_id: PatientExternalId
    note: typing.Optional[str] = None
    due_date: dt.date
    status: InvoiceStatus
    url: typing.Optional[str] = pydantic.Field(default=None)
    """
    Link to the admin view of the invoice in the third-party service
    """

    customer_invoice_url: typing.Optional[str] = pydantic.Field(default=None)
    """
    Link to the patient view of the invoice in the third-party service
    """

    items: InvoiceItemInfo = pydantic.Field()
    """
    The InvoiceItem rollup which contains all claim and service line invoice items
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
