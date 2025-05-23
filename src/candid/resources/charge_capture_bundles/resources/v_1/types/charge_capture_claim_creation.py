# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic
from ......core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .....charge_capture.resources.v_1.types.charge_capture_data import ChargeCaptureData
from .....charge_capture.resources.v_1.types.charge_capture_error import ChargeCaptureError
from .....commons.types.charge_capture_claim_creation_id import ChargeCaptureClaimCreationId
from .....commons.types.encounter_id import EncounterId
from .charge_capture_claim_creation_status import ChargeCaptureClaimCreationStatus


class ChargeCaptureClaimCreation(UniversalBaseModel):
    id: ChargeCaptureClaimCreationId
    created_encounter_id: typing.Optional[EncounterId] = None
    status: ChargeCaptureClaimCreationStatus = pydantic.Field()
    """
    Status of the Claim Creation, Successful means that the Claim Creation created a corresponding Claim
    """

    characteristics: typing.Dict[str, typing.Optional[typing.Optional[typing.Any]]] = pydantic.Field()
    """
    A dictionary of characteristics that are used to group charge captures together based on the bundling configuration.
    Example: {"service_facility.npi": "99999999", "date_of_service": "2023-01-01"}
    """

    errors: typing.List[ChargeCaptureError] = pydantic.Field()
    """
    All errors that were found when the Claim was attempted to be created.
    Errors can correspond to the Claim Creation as a whole or specific underlying Charge Captures.
    """

    encounter_creation_input: typing.Optional[ChargeCaptureData] = pydantic.Field(default=None)
    """
    If a ChargeCaptureBundle attempts creation, this is the input that was created from the underlying charges and used to attempt encounter creation.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
