# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic
from ......core.pydantic_utilities import IS_PYDANTIC_V2
from .....commons.types.clinical_trial_id import ClinicalTrialId
from .....non_insurance_payers.resources.v_1.types.non_insurance_payer_id import NonInsurancePayerId
from .mutable_clinical_trial import MutableClinicalTrial


class ClinicalTrial(MutableClinicalTrial):
    clinical_trial_id: ClinicalTrialId
    non_insurance_payer_id: NonInsurancePayerId
    is_active: bool

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
