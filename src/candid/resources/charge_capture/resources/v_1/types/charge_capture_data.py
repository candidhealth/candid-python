# This file was auto-generated by Fern from our API Definition.

from .....encounters.resources.v_4.types.encounter_optional import EncounterOptional
import typing
from .....diagnoses.types.diagnosis_create import DiagnosisCreate
import pydantic
from .....encounters.resources.v_4.types.intervention import Intervention
from .....claim_submission.resources.v_1.types.external_claim_submission_create import ExternalClaimSubmissionCreate
from .....service_lines.resources.v_2.types.service_line_create import ServiceLineCreate
from .....encounters.resources.v_4.types.patient_history_category import PatientHistoryCategory
from .....billing_notes.resources.v_2.types.billing_note import BillingNote
from ......core.pydantic_utilities import IS_PYDANTIC_V2


class ChargeCaptureData(EncounterOptional):
    diagnoses: typing.Optional[typing.List[DiagnosisCreate]] = pydantic.Field(default=None)
    """
    Ideally, this field should contain no more than 12 diagnoses. However, more diagnoses
    may be submitted at this time, and coders will later prioritize the 12 that will be
    submitted to the payor.
    """

    interventions: typing.Optional[typing.List[Intervention]] = None
    external_claim_submission: typing.Optional[ExternalClaimSubmissionCreate] = pydantic.Field(default=None)
    """
    **_This field is in beta._**
    To be included for claims that have been submitted outside of Candid.
    Candid supports posting remits and payments to these claims and working them in-platform (e.g. editing, resubmitting).
    """

    service_lines: typing.Optional[typing.List[ServiceLineCreate]] = pydantic.Field(default=None)
    """
    Each service line must be linked to a diagnosis. Concretely,
    `service_line.diagnosis_pointers`must contain at least one entry which should be
    in bounds of the diagnoses list field.
    """

    patient_histories: typing.Optional[typing.List[PatientHistoryCategory]] = None
    billing_notes: typing.Optional[typing.List[BillingNote]] = pydantic.Field(default=None)
    """
    Spot to store misc, human-readable, notes about this encounter to be
    used in the billing process.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
