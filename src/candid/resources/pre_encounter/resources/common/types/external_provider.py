# This file was auto-generated by Fern from our API Definition.

from ......core.pydantic_utilities import UniversalBaseModel
from .human_name import HumanName
import typing
from .external_provider_type import ExternalProviderType
import pydantic
from .contact_point import ContactPoint
from .address import Address
from .period import Period
from .canonical_provider_id import CanonicalProviderId
from ......core.pydantic_utilities import IS_PYDANTIC_V2


class ExternalProvider(UniversalBaseModel):
    name: HumanName
    type: typing.Optional[ExternalProviderType] = pydantic.Field(default=None)
    """
    Defaults to ATTENDING.
    """

    npi: typing.Optional[str] = None
    telecoms: typing.List[ContactPoint]
    addresses: typing.Optional[typing.List[Address]] = None
    period: typing.Optional[Period] = None
    canonical_id: typing.Optional[CanonicalProviderId] = None
    fax: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
