# This file was auto-generated by Fern from our API Definition.

from .....core.client_wrapper import SyncClientWrapper
from .resources.v_1.client import V1Client
from .....core.client_wrapper import AsyncClientWrapper
from .resources.v_1.client import AsyncV1Client


class NotesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper
        self.v_1 = V1Client(client_wrapper=self._client_wrapper)


class AsyncNotesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper
        self.v_1 = AsyncV1Client(client_wrapper=self._client_wrapper)
