# This file was auto-generated by Fern from our API Definition.

from ........core.pydantic_utilities import UniversalBaseModel
from .....common.types.payer_id import PayerId
import typing
from .....common.types.additional_payer_information import AdditionalPayerInformation
import pydantic
from .authorization_unit import AuthorizationUnit
from .....common.types.period import Period
from ........core.pydantic_utilities import IS_PYDANTIC_V2


class Authorization(UniversalBaseModel):
    payer_id: PayerId
    payer_name: str
    additional_payer_information: typing.Optional[AdditionalPayerInformation] = None
    authorization_number: str
    cpt_code: str
    apply_for_all_cpt_codes: typing.Optional[bool] = pydantic.Field(default=None)
    """
    If true, then the authorization will apply for all claims for the payer that fall in range the `period`.
    """

    units: AuthorizationUnit
    quantity: typing.Optional[int] = None
    period: typing.Optional[Period] = None
    notes: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
