# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import typing

import typing_extensions

from .....commons.types.claim_id import ClaimId
from .....commons.types.provider_id import ProviderId
from .....commons.types.service_line_id import ServiceLineId

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class InsuranceWriteOffTarget_ServiceLineId(pydantic.BaseModel):
    type: typing_extensions.Literal["service_line_id"]
    value: ServiceLineId

    class Config:
        frozen = True
        smart_union = True


class InsuranceWriteOffTarget_ClaimId(pydantic.BaseModel):
    type: typing_extensions.Literal["claim_id"]
    value: ClaimId

    class Config:
        frozen = True
        smart_union = True


class InsuranceWriteOffTarget_BillingProviderId(pydantic.BaseModel):
    type: typing_extensions.Literal["billing_provider_id"]
    value: ProviderId

    class Config:
        frozen = True
        smart_union = True


InsuranceWriteOffTarget = typing.Union[
    InsuranceWriteOffTarget_ServiceLineId, InsuranceWriteOffTarget_ClaimId, InsuranceWriteOffTarget_BillingProviderId
]
