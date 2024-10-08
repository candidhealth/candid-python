# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import datetime as dt
import typing

import pydantic

from ......core.datetime_utils import serialize_datetime
from ......core.pydantic_utilities import deep_union_pydantic_dicts
from .....organization_providers.resources.v_2.types.organization_provider_id import OrganizationProviderId
from .....payers.resources.v_3.types.payer_uuid import PayerUuid
from .explanation import Explanation


class ComputeAllInNetworkRenderingProvidersResult_RenderingProviders(pydantic.BaseModel):
    rendering_providers: typing.List[OrganizationProviderId]
    routed_payer_uuid: PayerUuid
    routed_billing_provider_id: OrganizationProviderId
    type: typing.Literal["rendering_providers"] = "rendering_providers"

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults_exclude_unset: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        kwargs_with_defaults_exclude_none: typing.Any = {"by_alias": True, "exclude_none": True, **kwargs}

        return deep_union_pydantic_dicts(
            super().dict(**kwargs_with_defaults_exclude_unset), super().dict(**kwargs_with_defaults_exclude_none)
        )

    class Config:
        frozen = True
        smart_union = True
        extra = pydantic.Extra.allow
        json_encoders = {dt.datetime: serialize_datetime}


class ComputeAllInNetworkRenderingProvidersResult_Indeterminate(pydantic.BaseModel):
    error: str
    explanation: Explanation
    routed_payer_uuid: typing.Optional[PayerUuid] = None
    routed_billing_provider_id: typing.Optional[OrganizationProviderId] = None
    type: typing.Literal["indeterminate"] = "indeterminate"

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults_exclude_unset: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        kwargs_with_defaults_exclude_none: typing.Any = {"by_alias": True, "exclude_none": True, **kwargs}

        return deep_union_pydantic_dicts(
            super().dict(**kwargs_with_defaults_exclude_unset), super().dict(**kwargs_with_defaults_exclude_none)
        )

    class Config:
        frozen = True
        smart_union = True
        extra = pydantic.Extra.allow
        json_encoders = {dt.datetime: serialize_datetime}


class ComputeAllInNetworkRenderingProvidersResult_OutOfNetwork(pydantic.BaseModel):
    explanation: Explanation
    routed_payer_uuid: PayerUuid
    routed_billing_provider_id: OrganizationProviderId
    type: typing.Literal["out_of_network"] = "out_of_network"

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults_exclude_unset: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        kwargs_with_defaults_exclude_none: typing.Any = {"by_alias": True, "exclude_none": True, **kwargs}

        return deep_union_pydantic_dicts(
            super().dict(**kwargs_with_defaults_exclude_unset), super().dict(**kwargs_with_defaults_exclude_none)
        )

    class Config:
        frozen = True
        smart_union = True
        extra = pydantic.Extra.allow
        json_encoders = {dt.datetime: serialize_datetime}


ComputeAllInNetworkRenderingProvidersResult = typing.Union[
    ComputeAllInNetworkRenderingProvidersResult_RenderingProviders,
    ComputeAllInNetworkRenderingProvidersResult_Indeterminate,
    ComputeAllInNetworkRenderingProvidersResult_OutOfNetwork,
]
