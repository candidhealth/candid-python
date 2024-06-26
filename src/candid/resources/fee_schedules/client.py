# This file was auto-generated by Fern from our API Definition.

from ...core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .resources.v_3.client import AsyncV3Client, V3Client


class FeeSchedulesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper
        self.v_3 = V3Client(client_wrapper=self._client_wrapper)


class AsyncFeeSchedulesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper
        self.v_3 = AsyncV3Client(client_wrapper=self._client_wrapper)
