# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations
from ......core.pydantic_utilities import UniversalBaseModel
import typing
from .....payers.resources.v_3.types.payer_uuid import PayerUuid
from .....organization_providers.resources.v_2.types.organization_provider_id import OrganizationProviderId
from ......core.pydantic_utilities import IS_PYDANTIC_V2
import pydantic
from .explanation import Explanation


class ExpectedNetworkStatusV2_InNetwork(UniversalBaseModel):
    type: typing.Literal["in_network"] = "in_network"
    routed_payer_uuid: PayerUuid
    routed_billing_provider_id: OrganizationProviderId

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class ExpectedNetworkStatusV2_OutOfNetwork(UniversalBaseModel):
    type: typing.Literal["out_of_network"] = "out_of_network"
    explanation: Explanation
    routed_payer_uuid: PayerUuid
    routed_billing_provider_id: OrganizationProviderId

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class ExpectedNetworkStatusV2_Indeterminate(UniversalBaseModel):
    type: typing.Literal["indeterminate"] = "indeterminate"
    error: str
    explanation: Explanation
    routed_payer_uuid: typing.Optional[PayerUuid] = None
    routed_billing_provider_id: typing.Optional[OrganizationProviderId] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


ExpectedNetworkStatusV2 = typing.Union[
    ExpectedNetworkStatusV2_InNetwork, ExpectedNetworkStatusV2_OutOfNetwork, ExpectedNetworkStatusV2_Indeterminate
]
