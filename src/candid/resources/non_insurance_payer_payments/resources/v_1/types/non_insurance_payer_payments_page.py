# This file was auto-generated by Fern from our API Definition.

from .....commons.types.resource_page import ResourcePage
import typing
from .non_insurance_payer_payment import NonInsurancePayerPayment
from ......core.pydantic_utilities import IS_PYDANTIC_V2
import pydantic


class NonInsurancePayerPaymentsPage(ResourcePage):
    items: typing.List[NonInsurancePayerPayment]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
