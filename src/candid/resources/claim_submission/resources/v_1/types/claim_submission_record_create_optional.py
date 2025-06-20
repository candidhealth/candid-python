# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import pydantic
from ......core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .....commons.types.claim_submission_payer_responsibility_type import ClaimSubmissionPayerResponsibilityType
from .....commons.types.intended_submission_medium import IntendedSubmissionMedium
from .claim_frequency_type_code import ClaimFrequencyTypeCode


class ClaimSubmissionRecordCreateOptional(UniversalBaseModel):
    """
    Data about each external submission.

    Examples
    --------
    import datetime

    from candid.resources.claim_submission.resources.v_1 import (
        ClaimFrequencyTypeCode,
        ClaimSubmissionRecordCreateOptional,
    )
    from candid.resources.commons import (
        ClaimSubmissionPayerResponsibilityType,
        IntendedSubmissionMedium,
    )

    ClaimSubmissionRecordCreateOptional(
        submitted_at=datetime.datetime.fromisoformat(
            "2023-01-01 13:00:00+00:00",
        ),
        claim_frequency_code=ClaimFrequencyTypeCode.ORIGINAL,
        payer_responsibility=ClaimSubmissionPayerResponsibilityType.PRIMARY,
        intended_submission_medium=IntendedSubmissionMedium.ELECTRONIC,
    )
    """

    submitted_at: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    When the claim was submitted to the payer.
    """

    claim_frequency_code: typing.Optional[ClaimFrequencyTypeCode] = None
    payer_responsibility: typing.Optional[ClaimSubmissionPayerResponsibilityType] = None
    intended_submission_medium: typing.Optional[IntendedSubmissionMedium] = pydantic.Field(default=None)
    """
    The medium by which the claim was submitted to the payer: paper or electronic.
    If omitted, defaults to electronic.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
