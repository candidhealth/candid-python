# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import datetime as dt
import typing

import pydantic
import typing_extensions

from ....core.datetime_utils import serialize_datetime
from ....core.pydantic_utilities import deep_union_pydantic_dicts
from ...commons.types.claim_id import ClaimId
from ...commons.types.encounter_external_id import EncounterExternalId
from ...commons.types.provider_id import ProviderId
from ...commons.types.service_line_id import ServiceLineId

T_Result = typing.TypeVar("T_Result")


class _Factory:
    def service_line_by_id(self, value: ServiceLineId) -> AllocationTargetCreate:
        return AllocationTargetCreate(
            __root__=_AllocationTargetCreate.ServiceLineById(type="service_line_by_id", value=value)
        )

    def claim_by_id(self, value: ClaimId) -> AllocationTargetCreate:
        return AllocationTargetCreate(__root__=_AllocationTargetCreate.ClaimById(type="claim_by_id", value=value))

    def claim_by_encounter_external_id(self, value: EncounterExternalId) -> AllocationTargetCreate:
        return AllocationTargetCreate(
            __root__=_AllocationTargetCreate.ClaimByEncounterExternalId(
                type="claim_by_encounter_external_id", value=value
            )
        )

    def billing_provider_by_id(self, value: ProviderId) -> AllocationTargetCreate:
        return AllocationTargetCreate(
            __root__=_AllocationTargetCreate.BillingProviderById(type="billing_provider_by_id", value=value)
        )

    def unattributed(self) -> AllocationTargetCreate:
        return AllocationTargetCreate(__root__=_AllocationTargetCreate.Unattributed(type="unattributed"))


class AllocationTargetCreate(pydantic.BaseModel):
    """
    Allocation targets describe whether the portion of a payment is being applied toward a specific service line,
    claim, billing provider, or is unallocated.
    """

    factory: typing.ClassVar[_Factory] = _Factory()

    def get_as_union(
        self,
    ) -> typing.Union[
        _AllocationTargetCreate.ServiceLineById,
        _AllocationTargetCreate.ClaimById,
        _AllocationTargetCreate.ClaimByEncounterExternalId,
        _AllocationTargetCreate.BillingProviderById,
        _AllocationTargetCreate.Unattributed,
    ]:
        return self.__root__

    def visit(
        self,
        service_line_by_id: typing.Callable[[ServiceLineId], T_Result],
        claim_by_id: typing.Callable[[ClaimId], T_Result],
        claim_by_encounter_external_id: typing.Callable[[EncounterExternalId], T_Result],
        billing_provider_by_id: typing.Callable[[ProviderId], T_Result],
        unattributed: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self.__root__.type == "service_line_by_id":
            return service_line_by_id(self.__root__.value)
        if self.__root__.type == "claim_by_id":
            return claim_by_id(self.__root__.value)
        if self.__root__.type == "claim_by_encounter_external_id":
            return claim_by_encounter_external_id(self.__root__.value)
        if self.__root__.type == "billing_provider_by_id":
            return billing_provider_by_id(self.__root__.value)
        if self.__root__.type == "unattributed":
            return unattributed()

    __root__: typing_extensions.Annotated[
        typing.Union[
            _AllocationTargetCreate.ServiceLineById,
            _AllocationTargetCreate.ClaimById,
            _AllocationTargetCreate.ClaimByEncounterExternalId,
            _AllocationTargetCreate.BillingProviderById,
            _AllocationTargetCreate.Unattributed,
        ],
        pydantic.Field(discriminator="type"),
    ]

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
        extra = pydantic.Extra.forbid
        json_encoders = {dt.datetime: serialize_datetime}


class _AllocationTargetCreate:
    class ServiceLineById(pydantic.BaseModel):
        type: typing.Literal["service_line_by_id"] = "service_line_by_id"
        value: ServiceLineId

        class Config:
            frozen = True
            smart_union = True

    class ClaimById(pydantic.BaseModel):
        type: typing.Literal["claim_by_id"] = "claim_by_id"
        value: ClaimId

        class Config:
            frozen = True
            smart_union = True

    class ClaimByEncounterExternalId(pydantic.BaseModel):
        type: typing.Literal["claim_by_encounter_external_id"] = "claim_by_encounter_external_id"
        value: EncounterExternalId

        class Config:
            frozen = True
            smart_union = True

    class BillingProviderById(pydantic.BaseModel):
        type: typing.Literal["billing_provider_by_id"] = "billing_provider_by_id"
        value: ProviderId

        class Config:
            frozen = True
            smart_union = True

    class Unattributed(pydantic.BaseModel):
        type: typing.Literal["unattributed"] = "unattributed"

        class Config:
            frozen = True
            smart_union = True


AllocationTargetCreate.update_forward_refs()
