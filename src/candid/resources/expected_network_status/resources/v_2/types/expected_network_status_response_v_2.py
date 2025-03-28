# This file was auto-generated by Fern from our API Definition.

from ......core.pydantic_utilities import UniversalBaseModel
from .network_status_check_id import NetworkStatusCheckId
from .expected_network_status_v_2 import ExpectedNetworkStatusV2
from ......core.pydantic_utilities import IS_PYDANTIC_V2
import typing
import pydantic


class ExpectedNetworkStatusResponseV2(UniversalBaseModel):
    network_status_check_id: NetworkStatusCheckId
    network_status: ExpectedNetworkStatusV2

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
