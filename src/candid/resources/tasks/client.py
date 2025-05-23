# This file was auto-generated by Fern from our API Definition.

from ...core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .raw_client import AsyncRawTasksClient, RawTasksClient
from .resources.v_3.client import AsyncV3Client, V3Client


class TasksClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawTasksClient(client_wrapper=client_wrapper)
        self.v_3 = V3Client(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawTasksClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawTasksClient
        """
        return self._raw_client


class AsyncTasksClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawTasksClient(client_wrapper=client_wrapper)
        self.v_3 = AsyncV3Client(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawTasksClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawTasksClient
        """
        return self._raw_client
