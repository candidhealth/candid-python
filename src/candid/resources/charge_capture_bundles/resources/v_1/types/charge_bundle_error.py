# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing
import uuid

import pydantic

from ......core.datetime_utils import serialize_datetime
from ......core.pydantic_utilities import deep_union_pydantic_dicts
from .....commons.types.charge_capture_bundle_id import ChargeCaptureBundleId
from .....commons.types.charge_capture_id import ChargeCaptureId


class ChargeBundleError(pydantic.BaseModel):
    id: uuid.UUID
    charge_capture_id: typing.Optional[ChargeCaptureId] = pydantic.Field(default=None)
    """
    The underlying Charge Capture that this error object references.
    The Charge Capture referenced will be a part of the bundle tied to this error.
    Errors may also refer to all charge_captures present in a bundle, in which case this field will be null.
    """

    message: str = pydantic.Field()
    """
    A human readable error explaining why this charge capture bundle failed to create a claim.
    """

    field_in_error: typing.Optional[str] = pydantic.Field(default=None)
    """
    The field of the corresponding underlying ChargeCapture that has a field that is failing validations,
    is not present but marked as required, or otherwise in error.
    """

    bundle_id: ChargeCaptureBundleId = pydantic.Field()
    """
    The ID of the ChargeCaptureBundle associated with this Error.
    """

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
