# This file was auto-generated by Fern from our API Definition.

from ......core.pydantic_utilities import UniversalBaseModel
from .invoice_destination import InvoiceDestination
import pydantic
import typing
from ......core.pydantic_utilities import IS_PYDANTIC_V2


class InvoiceDestinationMetadata(UniversalBaseModel):
    invoice_destination: InvoiceDestination = pydantic.Field()
    """
    Defines which third-party service this invoice was created in
    """

    source_id: str = pydantic.Field()
    """
    The id of the invoice in the third-party service
    """

    source_customer_id: str = pydantic.Field()
    """
    The id of the customer that the invoice is attributed to in the third-party service
    """

    destination_status: typing.Optional[str] = pydantic.Field(default=None)
    """
    The status of the invoice in the third-party service
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
