# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations
from ....core.pydantic_utilities import UniversalBaseModel
from ...commons.types.service_line_id import ServiceLineId
import typing
from ....core.pydantic_utilities import IS_PYDANTIC_V2
import pydantic
from ...commons.types.claim_id import ClaimId
from ...commons.types.encounter_external_id import EncounterExternalId
from ...commons.types.provider_id import ProviderId
from ...commons.types.appointment_id import AppointmentId
from ...commons.types.patient_external_id import PatientExternalId


class AllocationTargetCreate_ServiceLineById(UniversalBaseModel):
    value: ServiceLineId
    type: typing.Literal["service_line_by_id"] = "service_line_by_id"

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True


class AllocationTargetCreate_ClaimById(UniversalBaseModel):
    value: ClaimId
    type: typing.Literal["claim_by_id"] = "claim_by_id"

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True


class AllocationTargetCreate_ClaimByEncounterExternalId(UniversalBaseModel):
    value: EncounterExternalId
    type: typing.Literal["claim_by_encounter_external_id"] = "claim_by_encounter_external_id"

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True


class AllocationTargetCreate_BillingProviderById(UniversalBaseModel):
    value: ProviderId
    type: typing.Literal["billing_provider_by_id"] = "billing_provider_by_id"

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True


class AllocationTargetCreate_AppointmentByIdAndPatientExternalId(UniversalBaseModel):
    """
    Allocation targets describe whether the portion of a payment is being applied toward a specific service line,
    claim, billing provider, or is unallocated.
    """

    type: typing.Literal["appointment_by_id_and_patient_external_id"] = "appointment_by_id_and_patient_external_id"
    appointment_id: AppointmentId
    patient_external_id: PatientExternalId

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class AllocationTargetCreate_Unattributed(UniversalBaseModel):
    """
    Allocation targets describe whether the portion of a payment is being applied toward a specific service line,
    claim, billing provider, or is unallocated.
    """

    type: typing.Literal["unattributed"] = "unattributed"

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


AllocationTargetCreate = typing.Union[
    AllocationTargetCreate_ServiceLineById,
    AllocationTargetCreate_ClaimById,
    AllocationTargetCreate_ClaimByEncounterExternalId,
    AllocationTargetCreate_BillingProviderById,
    AllocationTargetCreate_AppointmentByIdAndPatientExternalId,
    AllocationTargetCreate_Unattributed,
]
