# This file was auto-generated by Fern from our API Definition.

from .....core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .raw_client import AsyncRawImagesClient, RawImagesClient
from .resources.v_1.client import AsyncV1Client, V1Client


class ImagesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawImagesClient(client_wrapper=client_wrapper)
        self.v_1 = V1Client(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawImagesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawImagesClient
        """
        return self._raw_client


class AsyncImagesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawImagesClient(client_wrapper=client_wrapper)
        self.v_1 = AsyncV1Client(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawImagesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawImagesClient
        """
        return self._raw_client
