# This file was auto-generated by Fern from our API Definition.

from .encounter_provider_base import EncounterProviderBase
import typing
import pydantic
from .....commons.types.street_address_long_zip import StreetAddressLongZip
from ......core.pydantic_utilities import IS_PYDANTIC_V2


class OrderingProviderUpdate(EncounterProviderBase):
    npi: typing.Optional[str] = pydantic.Field(default=None)
    """
    A National Provider Identifier is a unique 10-digit identification
    number issued to health care providers in the United States
    """

    taxonomy_code: typing.Optional[str] = None
    address: typing.Optional[StreetAddressLongZip] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
