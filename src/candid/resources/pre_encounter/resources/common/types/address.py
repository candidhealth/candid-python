# This file was auto-generated by Fern from our API Definition.

from ......core.pydantic_utilities import UniversalBaseModel
from .address_use import AddressUse
import typing
from .period import Period
from ......core.pydantic_utilities import IS_PYDANTIC_V2
import pydantic


class Address(UniversalBaseModel):
    use: AddressUse
    line: typing.List[str]
    city: str
    state: str
    postal_code: str
    country: str
    period: typing.Optional[Period] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
