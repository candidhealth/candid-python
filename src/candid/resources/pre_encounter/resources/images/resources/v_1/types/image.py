# This file was auto-generated by Fern from our API Definition.

from .....common.types.base_model import BaseModel
from .mutable_image import MutableImage
from .image_id import ImageId
import pydantic
from ........core.pydantic_utilities import IS_PYDANTIC_V2
import typing


class Image(BaseModel, MutableImage):
    """
    An Image object with immutable server-owned properties.
    """

    id: ImageId
    signed_url: str = pydantic.Field()
    """
    A signed URL to the image. This url can be used to upload an image to GCP storage or to read the image contents.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
