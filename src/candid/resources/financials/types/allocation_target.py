# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import datetime as dt
import typing

import pydantic

from ....core.datetime_utils import serialize_datetime
from ....core.pydantic_utilities import deep_union_pydantic_dicts
from ...commons.types.appointment_id import AppointmentId
from ...commons.types.claim_id import ClaimId
from ...commons.types.encounter_id import EncounterId
from ...commons.types.patient_external_id import PatientExternalId
from ...commons.types.provider_id import ProviderId
from ...commons.types.service_line_id import ServiceLineId


class AllocationTarget_ServiceLine(pydantic.BaseModel):
    """
    Allocation targets describe whether the portion of a payment is being applied toward a specific service line,
    claim, billing provider, or is unallocated.
    """

    service_line_id: ServiceLineId
    claim_id: ClaimId
    encounter_id: EncounterId
    type: typing.Literal["service_line"] = "service_line"

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


class AllocationTarget_Claim(pydantic.BaseModel):
    """
    Allocation targets describe whether the portion of a payment is being applied toward a specific service line,
    claim, billing provider, or is unallocated.
    """

    claim_id: ClaimId
    encounter_id: EncounterId
    type: typing.Literal["claim"] = "claim"

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


class AllocationTarget_BillingProviderId(pydantic.BaseModel):
    """
    Allocation targets describe whether the portion of a payment is being applied toward a specific service line,
    claim, billing provider, or is unallocated.
    """

    billing_provider_id: ProviderId
    type: typing.Literal["billing_provider_id"] = "billing_provider_id"

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


class AllocationTarget_Appointment(pydantic.BaseModel):
    """
    Allocation targets describe whether the portion of a payment is being applied toward a specific service line,
    claim, billing provider, or is unallocated.
    """

    appointment_id: AppointmentId
    patient_external_id: PatientExternalId
    type: typing.Literal["appointment"] = "appointment"

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


class AllocationTarget_Unattributed(pydantic.BaseModel):
    """
    Allocation targets describe whether the portion of a payment is being applied toward a specific service line,
    claim, billing provider, or is unallocated.
    """

    type: typing.Literal["unattributed"] = "unattributed"

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


AllocationTarget = typing.Union[
    AllocationTarget_ServiceLine,
    AllocationTarget_Claim,
    AllocationTarget_BillingProviderId,
    AllocationTarget_Appointment,
    AllocationTarget_Unattributed,
]
