# This file was auto-generated by Fern from our API Definition.

from ......core.pydantic_utilities import UniversalBaseModel
import datetime as dt
import pydantic
import typing
from .claim_submission_record_create import ClaimSubmissionRecordCreate
from ......core.pydantic_utilities import IS_PYDANTIC_V2


class ExternalClaimSubmissionCreate(UniversalBaseModel):
    """
    Examples
    --------
    import datetime

    from candid.resources.claim_submission.resources.v_1 import (
        ClaimFrequencyTypeCode,
        ClaimSubmissionRecordCreate,
        ExternalClaimSubmissionCreate,
    )
    from candid.resources.commons import (
        ClaimSubmissionPayerResponsibilityType,
        IntendedSubmissionMedium,
    )

    ExternalClaimSubmissionCreate(
        claim_created_at=datetime.datetime.fromisoformat(
            "2023-01-01 12:00:00+00:00",
        ),
        patient_control_number="PATIENT_CONTROL_NUMBER",
        submission_records=[
            ClaimSubmissionRecordCreate(
                submitted_at=datetime.datetime.fromisoformat(
                    "2023-01-01 13:00:00+00:00",
                ),
                claim_frequency_code=ClaimFrequencyTypeCode.ORIGINAL,
                payer_responsibility=ClaimSubmissionPayerResponsibilityType.PRIMARY,
                intended_submission_medium=IntendedSubmissionMedium.ELECTRONIC,
            ),
            ClaimSubmissionRecordCreate(
                submitted_at=datetime.datetime.fromisoformat(
                    "2023-01-04 12:00:00+00:00",
                ),
                claim_frequency_code=ClaimFrequencyTypeCode.REPLACEMENT,
                payer_responsibility=ClaimSubmissionPayerResponsibilityType.PRIMARY,
                intended_submission_medium=IntendedSubmissionMedium.PAPER,
            ),
        ],
    )
    """

    claim_created_at: dt.datetime = pydantic.Field()
    """
    When the claim was created in the external system.
    """

    patient_control_number: str = pydantic.Field()
    """
    The Patient Control Number sent on the claim to the payer. To guarantee compatibility with all payers, this field must consist
    only of uppercase letters and numbers and be no more than 14 characters long.
    """

    submission_records: typing.List[ClaimSubmissionRecordCreate] = pydantic.Field()
    """
    A successful claim submission record will be created for each value provided.
    An empty list may be provided for cases where the claim originated in an external system but was never submitted to a payer.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
