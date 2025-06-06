# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic
from ......core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .....organization_providers.resources.v_2.types.organization_provider_id import OrganizationProviderId
from .....payers.resources.v_3.types.payer_uuid import PayerUuid


class InNetworkStatus(UniversalBaseModel):
    routed_payer_uuid: PayerUuid
    routed_billing_provider_id: OrganizationProviderId

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
