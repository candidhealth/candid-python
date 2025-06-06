# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from .....core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .....core.request_options import RequestOptions
from ....commons.types.encounter_id import EncounterId
from ....commons.types.page_token import PageToken
from ....commons.types.task_id import TaskId
from ....commons.types.user_id import UserId
from ..commons.types.task_status import TaskStatus
from ..commons.types.task_type import TaskType
from .raw_client import AsyncRawV3Client, RawV3Client
from .types.task import Task
from .types.task_actions import TaskActions
from .types.task_create_v_3 import TaskCreateV3
from .types.task_page import TaskPage
from .types.task_sort_options import TaskSortOptions
from .types.task_update_v_3 import TaskUpdateV3

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class V3Client:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawV3Client(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawV3Client:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawV3Client
        """
        return self._raw_client

    def get_actions(self, task_id: TaskId, *, request_options: typing.Optional[RequestOptions] = None) -> TaskActions:
        """
        Parameters
        ----------
        task_id : TaskId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TaskActions

        Examples
        --------
        import uuid

        from candid import CandidApiClient

        client = CandidApiClient(
            client_id="YOUR_CLIENT_ID",
            client_secret="YOUR_CLIENT_SECRET",
        )
        client.tasks.v_3.get_actions(
            task_id=uuid.UUID(
                "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
            ),
        )
        """
        _response = self._raw_client.get_actions(task_id, request_options=request_options)
        return _response.data

    def get_multi(
        self,
        *,
        limit: typing.Optional[int] = None,
        page_token: typing.Optional[PageToken] = None,
        status: typing.Optional[TaskStatus] = None,
        task_type: typing.Optional[TaskType] = None,
        categories: typing.Optional[str] = None,
        updated_since: typing.Optional[dt.datetime] = None,
        encounter_id: typing.Optional[EncounterId] = None,
        search_term: typing.Optional[str] = None,
        assigned_to_id: typing.Optional[UserId] = None,
        date_of_service_min: typing.Optional[dt.date] = None,
        date_of_service_max: typing.Optional[dt.date] = None,
        billing_provider_npi: typing.Optional[str] = None,
        sort: typing.Optional[TaskSortOptions] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TaskPage:
        """
        Parameters
        ----------
        limit : typing.Optional[int]
            Defaults to 100

        page_token : typing.Optional[PageToken]

        status : typing.Optional[TaskStatus]

        task_type : typing.Optional[TaskType]

        categories : typing.Optional[str]
            Only return tasks with categories that match one in this comma-separated list.

        updated_since : typing.Optional[dt.datetime]
            Only return tasks updated on or after this date-time

        encounter_id : typing.Optional[EncounterId]
            Only return tasks associated with this encounter

        search_term : typing.Optional[str]
            Query tasks by encounter_id, claim_id, task_id, or external_id

        assigned_to_id : typing.Optional[UserId]
            Only return tasks assigned to this user

        date_of_service_min : typing.Optional[dt.date]
            The minimum date of service for the linked encounter

        date_of_service_max : typing.Optional[dt.date]
            The maximum date of service for the linked encounter

        billing_provider_npi : typing.Optional[str]
            The NPI of the billing provider associated with the task's claim

        sort : typing.Optional[TaskSortOptions]
            Defaults to updated_at:desc

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TaskPage

        Examples
        --------
        from candid import CandidApiClient

        client = CandidApiClient(
            client_id="YOUR_CLIENT_ID",
            client_secret="YOUR_CLIENT_SECRET",
        )
        client.tasks.v_3.get_multi()
        """
        _response = self._raw_client.get_multi(
            limit=limit,
            page_token=page_token,
            status=status,
            task_type=task_type,
            categories=categories,
            updated_since=updated_since,
            encounter_id=encounter_id,
            search_term=search_term,
            assigned_to_id=assigned_to_id,
            date_of_service_min=date_of_service_min,
            date_of_service_max=date_of_service_max,
            billing_provider_npi=billing_provider_npi,
            sort=sort,
            request_options=request_options,
        )
        return _response.data

    def get(self, task_id: TaskId, *, request_options: typing.Optional[RequestOptions] = None) -> Task:
        """
        Parameters
        ----------
        task_id : TaskId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Task

        Examples
        --------
        import uuid

        from candid import CandidApiClient

        client = CandidApiClient(
            client_id="YOUR_CLIENT_ID",
            client_secret="YOUR_CLIENT_SECRET",
        )
        client.tasks.v_3.get(
            task_id=uuid.UUID(
                "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
            ),
        )
        """
        _response = self._raw_client.get(task_id, request_options=request_options)
        return _response.data

    def create(self, *, request: TaskCreateV3, request_options: typing.Optional[RequestOptions] = None) -> Task:
        """
        Parameters
        ----------
        request : TaskCreateV3

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Task

        Examples
        --------
        import uuid

        from candid import CandidApiClient
        from candid.resources.tasks.resources.commons import TaskType
        from candid.resources.tasks.resources.v_3 import TaskCreateV3

        client = CandidApiClient(
            client_id="YOUR_CLIENT_ID",
            client_secret="YOUR_CLIENT_SECRET",
        )
        client.tasks.v_3.create(
            request=TaskCreateV3(
                encounter_id=uuid.UUID(
                    "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
                ),
                task_type=TaskType.CUSTOMER_DATA_REQUEST,
                description="description",
                work_queue_id="work_queue_id",
            ),
        )
        """
        _response = self._raw_client.create(request=request, request_options=request_options)
        return _response.data

    def update(
        self, task_id: TaskId, *, request: TaskUpdateV3, request_options: typing.Optional[RequestOptions] = None
    ) -> Task:
        """
        Parameters
        ----------
        task_id : TaskId

        request : TaskUpdateV3

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Task

        Examples
        --------
        import uuid

        from candid import CandidApiClient
        from candid.resources.tasks.resources.v_3 import TaskUpdateV3

        client = CandidApiClient(
            client_id="YOUR_CLIENT_ID",
            client_secret="YOUR_CLIENT_SECRET",
        )
        client.tasks.v_3.update(
            task_id=uuid.UUID(
                "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
            ),
            request=TaskUpdateV3(),
        )
        """
        _response = self._raw_client.update(task_id, request=request, request_options=request_options)
        return _response.data


class AsyncV3Client:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawV3Client(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawV3Client:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawV3Client
        """
        return self._raw_client

    async def get_actions(
        self, task_id: TaskId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> TaskActions:
        """
        Parameters
        ----------
        task_id : TaskId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TaskActions

        Examples
        --------
        import asyncio
        import uuid

        from candid import AsyncCandidApiClient

        client = AsyncCandidApiClient(
            client_id="YOUR_CLIENT_ID",
            client_secret="YOUR_CLIENT_SECRET",
        )


        async def main() -> None:
            await client.tasks.v_3.get_actions(
                task_id=uuid.UUID(
                    "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_actions(task_id, request_options=request_options)
        return _response.data

    async def get_multi(
        self,
        *,
        limit: typing.Optional[int] = None,
        page_token: typing.Optional[PageToken] = None,
        status: typing.Optional[TaskStatus] = None,
        task_type: typing.Optional[TaskType] = None,
        categories: typing.Optional[str] = None,
        updated_since: typing.Optional[dt.datetime] = None,
        encounter_id: typing.Optional[EncounterId] = None,
        search_term: typing.Optional[str] = None,
        assigned_to_id: typing.Optional[UserId] = None,
        date_of_service_min: typing.Optional[dt.date] = None,
        date_of_service_max: typing.Optional[dt.date] = None,
        billing_provider_npi: typing.Optional[str] = None,
        sort: typing.Optional[TaskSortOptions] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TaskPage:
        """
        Parameters
        ----------
        limit : typing.Optional[int]
            Defaults to 100

        page_token : typing.Optional[PageToken]

        status : typing.Optional[TaskStatus]

        task_type : typing.Optional[TaskType]

        categories : typing.Optional[str]
            Only return tasks with categories that match one in this comma-separated list.

        updated_since : typing.Optional[dt.datetime]
            Only return tasks updated on or after this date-time

        encounter_id : typing.Optional[EncounterId]
            Only return tasks associated with this encounter

        search_term : typing.Optional[str]
            Query tasks by encounter_id, claim_id, task_id, or external_id

        assigned_to_id : typing.Optional[UserId]
            Only return tasks assigned to this user

        date_of_service_min : typing.Optional[dt.date]
            The minimum date of service for the linked encounter

        date_of_service_max : typing.Optional[dt.date]
            The maximum date of service for the linked encounter

        billing_provider_npi : typing.Optional[str]
            The NPI of the billing provider associated with the task's claim

        sort : typing.Optional[TaskSortOptions]
            Defaults to updated_at:desc

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TaskPage

        Examples
        --------
        import asyncio

        from candid import AsyncCandidApiClient

        client = AsyncCandidApiClient(
            client_id="YOUR_CLIENT_ID",
            client_secret="YOUR_CLIENT_SECRET",
        )


        async def main() -> None:
            await client.tasks.v_3.get_multi()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_multi(
            limit=limit,
            page_token=page_token,
            status=status,
            task_type=task_type,
            categories=categories,
            updated_since=updated_since,
            encounter_id=encounter_id,
            search_term=search_term,
            assigned_to_id=assigned_to_id,
            date_of_service_min=date_of_service_min,
            date_of_service_max=date_of_service_max,
            billing_provider_npi=billing_provider_npi,
            sort=sort,
            request_options=request_options,
        )
        return _response.data

    async def get(self, task_id: TaskId, *, request_options: typing.Optional[RequestOptions] = None) -> Task:
        """
        Parameters
        ----------
        task_id : TaskId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Task

        Examples
        --------
        import asyncio
        import uuid

        from candid import AsyncCandidApiClient

        client = AsyncCandidApiClient(
            client_id="YOUR_CLIENT_ID",
            client_secret="YOUR_CLIENT_SECRET",
        )


        async def main() -> None:
            await client.tasks.v_3.get(
                task_id=uuid.UUID(
                    "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get(task_id, request_options=request_options)
        return _response.data

    async def create(self, *, request: TaskCreateV3, request_options: typing.Optional[RequestOptions] = None) -> Task:
        """
        Parameters
        ----------
        request : TaskCreateV3

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Task

        Examples
        --------
        import asyncio
        import uuid

        from candid import AsyncCandidApiClient
        from candid.resources.tasks.resources.commons import TaskType
        from candid.resources.tasks.resources.v_3 import TaskCreateV3

        client = AsyncCandidApiClient(
            client_id="YOUR_CLIENT_ID",
            client_secret="YOUR_CLIENT_SECRET",
        )


        async def main() -> None:
            await client.tasks.v_3.create(
                request=TaskCreateV3(
                    encounter_id=uuid.UUID(
                        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
                    ),
                    task_type=TaskType.CUSTOMER_DATA_REQUEST,
                    description="description",
                    work_queue_id="work_queue_id",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create(request=request, request_options=request_options)
        return _response.data

    async def update(
        self, task_id: TaskId, *, request: TaskUpdateV3, request_options: typing.Optional[RequestOptions] = None
    ) -> Task:
        """
        Parameters
        ----------
        task_id : TaskId

        request : TaskUpdateV3

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Task

        Examples
        --------
        import asyncio
        import uuid

        from candid import AsyncCandidApiClient
        from candid.resources.tasks.resources.v_3 import TaskUpdateV3

        client = AsyncCandidApiClient(
            client_id="YOUR_CLIENT_ID",
            client_secret="YOUR_CLIENT_SECRET",
        )


        async def main() -> None:
            await client.tasks.v_3.update(
                task_id=uuid.UUID(
                    "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
                ),
                request=TaskUpdateV3(),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update(task_id, request=request, request_options=request_options)
        return _response.data
