# Reference
## Auth V2
<details><summary><code>client.auth.v_2.<a href="src/candid/resources/auth/resources/v_2/client.py">get_token</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

<Callout intent="info">
Candid Health SDKs automatically handle authentication workflows after configuring them with the `client_id` and
`client_secret`.
</Callout>

Candid Health utilizes the [OAuth 2.0 bearer token authentication scheme](https://developer.mozilla.org/en-US/docs/Web/HTTP/Authentication) in our auth flow. You obtain the bearer token for all
subsequent API requests via the `/auth/token` endpoint defined below, which requires you to provide your `client_id` and `client_secret`. Your `client_id` and `client_secret` can be [generated](https://support.joincandidhealth.com/hc/en-us/articles/23065219476244--Generating-Candid-API-Keys) from the "Users & Credentials" tab by your org admin.

The bearer token is a signed [JWT](https://jwt.io/). The public key for the JWT can be found [here](https://candidhealth.auth0.com/pem) for any verification workflows.

The bearer token should be provided in the `Authorization` header for all subsequent API calls.

<Callout intent="warning">
The bearer token expires 5 hours after it has been created. After it has expired, the client will receive an "HTTP 401
Unauthorized" error, at which point the client should generate a new token. It is important that tokens be reused between
requests; if the client attempts to generate a token too often, it will be rate-limited and will receive an `HTTP 429 Too Many Requests` error.
</Callout>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from candid import CandidApiClient

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.auth.v_2.get_token(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**client_id:** `str` — Your application's Client ID.
    
</dd>
</dl>

<dl>
<dd>

**client_secret:** `str` — Your application's Client Secret.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## BillingNotes V2
<details><summary><code>client.billing_notes.v_2.<a href="src/candid/resources/billing_notes/resources/v_2/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import uuid

from candid import CandidApiClient

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.billing_notes.v_2.create(
    encounter_id=uuid.UUID(
        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
    ),
    text="string",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**encounter_id:** `EncounterId` 
    
</dd>
</dl>

<dl>
<dd>

**text:** `str` — Empty string not allowed.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.billing_notes.v_2.<a href="src/candid/resources/billing_notes/resources/v_2/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import uuid

from candid import CandidApiClient

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.billing_notes.v_2.delete(
    billing_note_id=uuid.UUID(
        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**billing_note_id:** `BillingNoteId` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.billing_notes.v_2.<a href="src/candid/resources/billing_notes/resources/v_2/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import uuid

from candid import CandidApiClient

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.billing_notes.v_2.update(
    billing_note_id=uuid.UUID(
        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
    ),
    text="string",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**billing_note_id:** `BillingNoteId` 
    
</dd>
</dl>

<dl>
<dd>

**text:** `str` — Empty string not allowed.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## ChargeCaptureBundles V1
<details><summary><code>client.charge_capture_bundles.v_1.<a href="src/candid/resources/charge_capture_bundles/resources/v_1/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import uuid

from candid import CandidApiClient

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.charge_capture_bundles.v_1.get(
    charge_capture_bundle_id=uuid.UUID(
        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**charge_capture_bundle_id:** `ChargeCaptureBundleId` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.charge_capture_bundles.v_1.<a href="src/candid/resources/charge_capture_bundles/resources/v_1/client.py">get_summary</a>()</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from candid import CandidApiClient

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.charge_capture_bundles.v_1.get_summary()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.charge_capture_bundles.v_1.<a href="src/candid/resources/charge_capture_bundles/resources/v_1/client.py">resubmit</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import uuid

from candid import CandidApiClient

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.charge_capture_bundles.v_1.resubmit(
    charge_capture_bundle_id=uuid.UUID(
        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**charge_capture_bundle_id:** `ChargeCaptureBundleId` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.charge_capture_bundles.v_1.<a href="src/candid/resources/charge_capture_bundles/resources/v_1/client.py">get_all</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import datetime
import uuid

from candid import CandidApiClient
from candid.resources.charge_capture.resources.v_1 import ChargeCaptureStatus
from candid.resources.charge_capture_bundles.resources.v_1 import (
    ChargeCaptureBundleSortField,
    ChargeCaptureBundleStatus,
)
from candid.resources.commons import SortDirection

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.charge_capture_bundles.v_1.get_all(
    limit=1,
    sort=ChargeCaptureBundleSortField.CREATED_AT,
    sort_direction=SortDirection.ASC,
    page_token="eyJ0b2tlbiI6IjEiLCJwYWdlX3Rva2VuIjoiMiJ9",
    patient_external_id="string",
    bundle_status=ChargeCaptureBundleStatus.NOT_STARTED,
    charge_status=ChargeCaptureStatus.PLANNED,
    charge_external_id="string",
    date_of_service_min=datetime.date.fromisoformat(
        "2023-01-15",
    ),
    date_of_service_max=datetime.date.fromisoformat(
        "2023-01-15",
    ),
    claim_ids=uuid.UUID(
        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
    ),
    bundle_ids=uuid.UUID(
        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
    ),
    billing_provider_npis="string",
    service_facility_name="string",
    primary_payer_ids="string",
    rendering_provider_npis="string",
    rendering_provider_names="string",
    supervising_provider_npis="string",
    supervising_provider_names="string",
    has_charge_capture_updates=True,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Maximum number of entities per page, defaults to 100.
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[ChargeCaptureBundleSortField]` — Defaults to created_at
    
</dd>
</dl>

<dl>
<dd>

**sort_direction:** `typing.Optional[SortDirection]` — Sort direction. Defaults to descending order if not provided.
    
</dd>
</dl>

<dl>
<dd>

**page_token:** `typing.Optional[PageToken]` 
    
</dd>
</dl>

<dl>
<dd>

**patient_external_id:** `typing.Optional[str]` — The patient ID from the external EMR platform for the patient
    
</dd>
</dl>

<dl>
<dd>

**bundle_status:** `typing.Optional[ChargeCaptureBundleStatus]` — the status of the charge capture bundle, refers to whether it was able to create an encounter.
    
</dd>
</dl>

<dl>
<dd>

**charge_status:** `typing.Optional[ChargeCaptureStatus]` — the status of the charge captures
    
</dd>
</dl>

<dl>
<dd>

**charge_external_id:** `typing.Optional[str]` 

A client-specified unique ID to associate with this encounter;
for example, your internal encounter ID or a Dr. Chrono encounter ID.
This field should not contain PHI.
    
</dd>
</dl>

<dl>
<dd>

**date_of_service_min:** `typing.Optional[dt.date]` 

Date formatted as YYYY-MM-DD; eg: 2019-08-24.
This date must be the local date in the timezone where the service occurred.
    
</dd>
</dl>

<dl>
<dd>

**date_of_service_max:** `typing.Optional[dt.date]` 

Date formatted as YYYY-MM-DD; eg: 2019-08-24.
This date must be the local date in the timezone where the service occurred.
    
</dd>
</dl>

<dl>
<dd>

**claim_ids:** `typing.Optional[typing.Union[EncounterId, typing.Sequence[EncounterId]]]` — A list of claim IDs to filter by. This will return all charge capture bundles that have a resulting claim with one of the IDs in this list.
    
</dd>
</dl>

<dl>
<dd>

**bundle_ids:** `typing.Optional[
    typing.Union[ChargeCaptureBundleId, typing.Sequence[ChargeCaptureBundleId]]
]` — A list of bundle IDs to filter by.
    
</dd>
</dl>

<dl>
<dd>

**billing_provider_npis:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A list of billing provider NPIs to filter by. This will return all charge capture bundles which include one or more charges with one of the NPIs in this list.
    
</dd>
</dl>

<dl>
<dd>

**service_facility_name:** `typing.Optional[str]` — A string to filter by. This will return all charge capture bundles which include one or more charges with this service facility name.
    
</dd>
</dl>

<dl>
<dd>

**primary_payer_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A list of primary payer IDs to filter by. This will return all charge capture bundles which include one or more charges with one of the primary payer IDs in this list.
    
</dd>
</dl>

<dl>
<dd>

**rendering_provider_npis:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A list of rendering provider NPIs to filter by. This will return all charge capture bundles which include one or more charges with one of the NPIs in this list.
    
</dd>
</dl>

<dl>
<dd>

**rendering_provider_names:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A list of rendering provider names to filter by. This will return all charge capture bundles which include one or more charges with one of the names in this list.
    
</dd>
</dl>

<dl>
<dd>

**supervising_provider_npis:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A list of supervising provider NPIs to filter by. This will return all charge capture bundles which include one or more charges with one of the NPIs in this list.
    
</dd>
</dl>

<dl>
<dd>

**supervising_provider_names:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A list of supervising provider names to filter by. This will return all charge capture bundles which include one or more charges with one of the names in this list.
    
</dd>
</dl>

<dl>
<dd>

**has_charge_capture_updates:** `typing.Optional[bool]` — If true, only return bundles that have charge captures that have been updated since the bundle has had a status of BILLED. See the updates property on ChargeCapture for more details.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## ChargeCapture V1
<details><summary><code>client.charge_capture.v_1.<a href="src/candid/resources/charge_capture/resources/v_1/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from candid import CandidApiClient
from candid.resources.charge_capture.resources.v_1 import (
    ChargeCaptureData,
    ChargeCaptureStatus,
)

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.charge_capture.v_1.create(
    data=ChargeCaptureData(),
    charge_external_id="string",
    ehr_source_url="string",
    patient_external_id="string",
    status=ChargeCaptureStatus.PLANNED,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**data:** `ChargeCaptureData` — Charge Capture data contains all the fields needed to create an encounter, but listed as optional. Candid will use this data when attempting to bundle multiple Charge Captures into a single encounter.

    
</dd>
</dl>

<dl>
<dd>

**charge_external_id:** `str` — A client-specified unique ID to associate with this encounter; for example, your internal encounter ID or a Dr. Chrono encounter ID. This field should not contain PHI.

    
</dd>
</dl>

<dl>
<dd>

**patient_external_id:** `str` — The patient ID from the external EMR platform for the patient
    
</dd>
</dl>

<dl>
<dd>

**status:** `ChargeCaptureStatus` — the status of the charge capture
    
</dd>
</dl>

<dl>
<dd>

**ehr_source_url:** `typing.Optional[str]` — External URL reference that links to Charge Capture details within the external system (e.g. the EHR visit page). Send full URL format for the external link (e.g. https://emr_charge_capture_url.com/123).

    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.charge_capture.v_1.<a href="src/candid/resources/charge_capture/resources/v_1/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import uuid

from candid import CandidApiClient

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.charge_capture.v_1.delete(
    charge_capture_id=uuid.UUID(
        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**charge_capture_id:** `ChargeCaptureId` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.charge_capture.v_1.<a href="src/candid/resources/charge_capture/resources/v_1/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import uuid

from candid import CandidApiClient
from candid.resources.charge_capture.resources.v_1 import (
    ChargeCaptureData,
    ChargeCaptureStatus,
)

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.charge_capture.v_1.update(
    charge_capture_id=uuid.UUID(
        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
    ),
    data=ChargeCaptureData(),
    charge_external_id="string",
    ehr_source_url="string",
    patient_external_id="string",
    status=ChargeCaptureStatus.PLANNED,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**charge_capture_id:** `ChargeCaptureId` 
    
</dd>
</dl>

<dl>
<dd>

**data:** `typing.Optional[ChargeCaptureData]` 
    
</dd>
</dl>

<dl>
<dd>

**charge_external_id:** `typing.Optional[str]` 

A client-specified unique ID to associate with this encounter;
for example, your internal encounter ID or a Dr. Chrono encounter ID.
This field should not contain PHI.

    
</dd>
</dl>

<dl>
<dd>

**ehr_source_url:** `typing.Optional[str]` 

External URL reference that links to Charge Capture details within the external system (e.g. the EHR visit page).
Send full URL format for the external link (e.g. https://emr_charge_capture_url.com/123).

    
</dd>
</dl>

<dl>
<dd>

**patient_external_id:** `typing.Optional[str]` — The patient ID from the external EMR platform for the patient
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[ChargeCaptureStatus]` — the status of the charge capture
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.charge_capture.v_1.<a href="src/candid/resources/charge_capture/resources/v_1/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import uuid

from candid import CandidApiClient

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.charge_capture.v_1.get(
    charge_capture_id=uuid.UUID(
        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**charge_capture_id:** `ChargeCaptureId` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.charge_capture.v_1.<a href="src/candid/resources/charge_capture/resources/v_1/client.py">get_all</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import datetime
import uuid

from candid import CandidApiClient
from candid.resources.charge_capture.resources.v_1 import (
    ChargeCaptureSortField,
    ChargeCaptureStatus,
)
from candid.resources.commons import SortDirection

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.charge_capture.v_1.get_all(
    limit=1,
    sort=ChargeCaptureSortField.CREATED_AT,
    sort_direction=SortDirection.ASC,
    page_token="eyJ0b2tlbiI6IjEiLCJwYWdlX3Rva2VuIjoiMiJ9",
    patient_external_id="string",
    status=ChargeCaptureStatus.PLANNED,
    charge_external_id="string",
    date_of_service_min=datetime.date.fromisoformat(
        "2023-01-15",
    ),
    date_of_service_max=datetime.date.fromisoformat(
        "2023-01-15",
    ),
    claim_ids=uuid.UUID(
        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
    ),
    bundle_id=uuid.UUID(
        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
    ),
    bundle_ids=uuid.UUID(
        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
    ),
    billing_provider_npis="string",
    service_facility_name="string",
    primary_payer_ids="string",
    rendering_provider_npis="string",
    rendering_provider_names="string",
    supervising_provider_npis="string",
    supervising_provider_names="string",
    exclude_charges_linked_to_claims=True,
    patient_external_id_ranked_sort="string",
    status_ranked_sort=ChargeCaptureStatus.PLANNED,
    charge_external_id_ranked_sort="string",
    date_of_service_min_ranked_sort=datetime.date.fromisoformat(
        "2023-01-15",
    ),
    date_of_service_max_ranked_sort=datetime.date.fromisoformat(
        "2023-01-15",
    ),
    claim_ids_ranked_sort=uuid.UUID(
        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
    ),
    bundle_ids_ranked_sort=uuid.UUID(
        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
    ),
    billing_provider_npis_ranked_sort="string",
    service_facility_name_ranked_sort="string",
    primary_payer_ids_ranked_sort="string",
    rendering_provider_npis_ranked_sort="string",
    rendering_provider_names_ranked_sort="string",
    supervising_provider_npis_ranked_sort="string",
    supervising_provider_names_ranked_sort="string",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Maximum number of entities per page, defaults to 100.
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[ChargeCaptureSortField]` — Defaults to created_at
    
</dd>
</dl>

<dl>
<dd>

**sort_direction:** `typing.Optional[SortDirection]` — Sort direction. Defaults to descending order if not provided.
    
</dd>
</dl>

<dl>
<dd>

**page_token:** `typing.Optional[PageToken]` 
    
</dd>
</dl>

<dl>
<dd>

**patient_external_id:** `typing.Optional[str]` — The patient ID from the external EMR platform for the patient
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[ChargeCaptureStatus]` — the status of the charge captures
    
</dd>
</dl>

<dl>
<dd>

**charge_external_id:** `typing.Optional[str]` 

A client-specified unique ID to associate with this encounter;
for example, your internal encounter ID or a Dr. Chrono encounter ID.
This field should not contain PHI.
    
</dd>
</dl>

<dl>
<dd>

**date_of_service_min:** `typing.Optional[dt.date]` 

Date formatted as YYYY-MM-DD; eg: 2019-08-24.
This date must be the local date in the timezone where the service occurred.
    
</dd>
</dl>

<dl>
<dd>

**date_of_service_max:** `typing.Optional[dt.date]` 

Date formatted as YYYY-MM-DD; eg: 2019-08-24.
This date must be the local date in the timezone where the service occurred.
    
</dd>
</dl>

<dl>
<dd>

**claim_ids:** `typing.Optional[typing.Union[EncounterId, typing.Sequence[EncounterId]]]` — A list of claim IDs to filter by. This will return all charge captures that have a resulting claim with one of the IDs in this list.
    
</dd>
</dl>

<dl>
<dd>

**bundle_id:** `typing.Optional[ChargeCaptureBundleId]` — A list of bundle IDs to filter by. Use `bundle_ids` instead.
    
</dd>
</dl>

<dl>
<dd>

**bundle_ids:** `typing.Optional[
    typing.Union[ChargeCaptureBundleId, typing.Sequence[ChargeCaptureBundleId]]
]` — A list of bundle IDs to filter by.
    
</dd>
</dl>

<dl>
<dd>

**billing_provider_npis:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A list of billing provider NPIs to filter by. This will return all charge captures with one of the NPIs in this list.
    
</dd>
</dl>

<dl>
<dd>

**service_facility_name:** `typing.Optional[str]` — A string to filter by. This will return all charge captures with this service facility name.
    
</dd>
</dl>

<dl>
<dd>

**primary_payer_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A list of primary payer IDs to filter by. This will return all charge captures with one of the primary payer IDs in this list.
    
</dd>
</dl>

<dl>
<dd>

**rendering_provider_npis:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A list of rendering provider NPIs to filter by. This will return all charge captures with one of the NPIs in this list.
    
</dd>
</dl>

<dl>
<dd>

**rendering_provider_names:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A list of rendering provider names to filter by. This will return all charge captures with one of the names in this list.
    
</dd>
</dl>

<dl>
<dd>

**supervising_provider_npis:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A list of supervising provider NPIs to filter by. This will return all charge captures with one of the NPIs in this list.
    
</dd>
</dl>

<dl>
<dd>

**supervising_provider_names:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A list of supervising provider names to filter by. This will return all charge captures with one of the names in this list.
    
</dd>
</dl>

<dl>
<dd>

**exclude_charges_linked_to_claims:** `typing.Optional[bool]` — Whether to exclude charge captures which are part of a claim creation.
    
</dd>
</dl>

<dl>
<dd>

**patient_external_id_ranked_sort:** `typing.Optional[str]` — The patient ID from the external EMR platform for the patient
    
</dd>
</dl>

<dl>
<dd>

**status_ranked_sort:** `typing.Optional[ChargeCaptureStatus]` — The charge capture status to show first
    
</dd>
</dl>

<dl>
<dd>

**charge_external_id_ranked_sort:** `typing.Optional[str]` 

A client-specified unique ID to associate with this encounter;
for example, your internal encounter ID or a Dr. Chrono encounter ID.
This field should not contain PHI.
    
</dd>
</dl>

<dl>
<dd>

**date_of_service_min_ranked_sort:** `typing.Optional[dt.date]` 

Date formatted as YYYY-MM-DD; eg: 2019-08-24.
This date must be the local date in the timezone where the service occurred.
    
</dd>
</dl>

<dl>
<dd>

**date_of_service_max_ranked_sort:** `typing.Optional[dt.date]` 

Date formatted as YYYY-MM-DD; eg: 2019-08-24.
This date must be the local date in the timezone where the service occurred.
    
</dd>
</dl>

<dl>
<dd>

**claim_ids_ranked_sort:** `typing.Optional[typing.Union[EncounterId, typing.Sequence[EncounterId]]]` — A list of claim IDs to show first. This will return all charge captures that have a resulting claim with one of the IDs in this list.
    
</dd>
</dl>

<dl>
<dd>

**bundle_ids_ranked_sort:** `typing.Optional[
    typing.Union[ChargeCaptureBundleId, typing.Sequence[ChargeCaptureBundleId]]
]` — A list of bundle IDs to show first.
    
</dd>
</dl>

<dl>
<dd>

**billing_provider_npis_ranked_sort:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A list of billing provider NPIs to show first. This will return all charge captures with one of the NPIs in this list.
    
</dd>
</dl>

<dl>
<dd>

**service_facility_name_ranked_sort:** `typing.Optional[str]` — A string to show first. This will return all charge captures with this service facility name.
    
</dd>
</dl>

<dl>
<dd>

**primary_payer_ids_ranked_sort:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A list of primary payer IDs to show first. This will return all charge captures with one of the primary payer IDs in this list.
    
</dd>
</dl>

<dl>
<dd>

**rendering_provider_npis_ranked_sort:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A list of rendering provider NPIs to show first. This will return all charge captures with one of the NPIs in this list.
    
</dd>
</dl>

<dl>
<dd>

**rendering_provider_names_ranked_sort:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A list of rendering provider names to show first. This will return all charge captures with one of the names in this list.
    
</dd>
</dl>

<dl>
<dd>

**supervising_provider_npis_ranked_sort:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A list of supervising provider NPIs to show first. This will return all charge captures with one of the NPIs in this list.
    
</dd>
</dl>

<dl>
<dd>

**supervising_provider_names_ranked_sort:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A list of supervising provider names to show first. This will return all charge captures with one of the names in this list.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.charge_capture.v_1.<a href="src/candid/resources/charge_capture/resources/v_1/client.py">update_post_billed_change</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import uuid

from candid import CandidApiClient

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.charge_capture.v_1.update_post_billed_change(
    charge_capture_change_id=uuid.UUID(
        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
    ),
    resolved=True,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**charge_capture_change_id:** `ChargeCapturePostBilledChangeId` 
    
</dd>
</dl>

<dl>
<dd>

**resolved:** `bool` 

Whether the change has been resolved. If true, the change will be marked as resolved.
If false, the change will be marked as unresolved.

    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Contracts V2
<details><summary><code>client.contracts.v_2.<a href="src/candid/resources/contracts/resources/v_2/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import uuid

from candid import CandidApiClient

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.contracts.v_2.get(
    contract_id=uuid.UUID(
        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**contract_id:** `ContractId` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.contracts.v_2.<a href="src/candid/resources/contracts/resources/v_2/client.py">get_multi</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import uuid

from candid import CandidApiClient
from candid.resources.commons import State
from candid.resources.contracts.resources.v_2 import ContractStatus

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.contracts.v_2.get_multi(
    page_token="eyJ0b2tlbiI6IjEiLCJwYWdlX3Rva2VuIjoiMiJ9",
    limit=1,
    contracting_provider_id=uuid.UUID(
        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
    ),
    rendering_provider_ids=uuid.UUID(
        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
    ),
    payer_names="string",
    states=State.AA,
    contract_status=ContractStatus.PENDING,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**page_token:** `typing.Optional[PageToken]` 
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Max number of contracts returned. Defaults to 1000. Max is 1000.
    
</dd>
</dl>

<dl>
<dd>

**contracting_provider_id:** `typing.Optional[ContractingProviderId]` 
    
</dd>
</dl>

<dl>
<dd>

**rendering_provider_ids:** `typing.Optional[
    typing.Union[RenderingProviderid, typing.Sequence[RenderingProviderid]]
]` 
    
</dd>
</dl>

<dl>
<dd>

**payer_names:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Filter to contracts that include any of the included payer names.
    
</dd>
</dl>

<dl>
<dd>

**states:** `typing.Optional[typing.Union[State, typing.Sequence[State]]]` 
    
</dd>
</dl>

<dl>
<dd>

**contract_status:** `typing.Optional[ContractStatus]` — The status of the contract. Defaults to `pending`
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.contracts.v_2.<a href="src/candid/resources/contracts/resources/v_2/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a new contract within the user's current organization
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import uuid

from candid import CandidApiClient
from candid.resources.commons import Regions_States
from candid.resources.contracts.resources.v_2 import (
    AuthorizedSignatory,
    ContractStatus,
    InsuranceTypes,
)

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.contracts.v_2.create(
    contracting_provider_id=uuid.UUID(
        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
    ),
    rendering_provider_ids=[
        uuid.UUID(
            "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
        )
    ],
    payer_uuid=uuid.UUID(
        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
    ),
    effective_date="string",
    expiration_date="string",
    regions=Regions_States(),
    contract_status=ContractStatus.PENDING,
    authorized_signatory=AuthorizedSignatory(
        first_name="string",
        last_name="string",
        title="string",
        email="string",
        phone="string",
        fax="string",
    ),
    commercial_insurance_types=InsuranceTypes(),
    medicare_insurance_types=InsuranceTypes(),
    medicaid_insurance_types=InsuranceTypes(),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**contracting_provider_id:** `ContractingProviderId` — The UUID of the provider under agreement to the contract
    
</dd>
</dl>

<dl>
<dd>

**rendering_provider_ids:** `typing.Set[RenderingProviderid]` 

A rendering provider isn't contracted directly with the payer but can render
services under the contract held by the contracting provider.
Max items is 100.

    
</dd>
</dl>

<dl>
<dd>

**payer_uuid:** `uuid.UUID` — The UUID of the insurance company under agreement to the contract
    
</dd>
</dl>

<dl>
<dd>

**effective_date:** `Date` — The starting day upon which the contract is effective
    
</dd>
</dl>

<dl>
<dd>

**regions:** `Regions` 

The state(s) to which the contract's coverage extends.
It may also be set to "national" for the entirety of the US.
    
</dd>
</dl>

<dl>
<dd>

**commercial_insurance_types:** `InsuranceTypes` — The commercial plan insurance types this contract applies.
    
</dd>
</dl>

<dl>
<dd>

**medicare_insurance_types:** `InsuranceTypes` — The Medicare plan insurance types this contract applies.
    
</dd>
</dl>

<dl>
<dd>

**medicaid_insurance_types:** `InsuranceTypes` — The Medicaid plan insurance types this contract applies.
    
</dd>
</dl>

<dl>
<dd>

**expiration_date:** `typing.Optional[Date]` — An optional end day upon which the contract expires
    
</dd>
</dl>

<dl>
<dd>

**contract_status:** `typing.Optional[ContractStatus]` 
    
</dd>
</dl>

<dl>
<dd>

**authorized_signatory:** `typing.Optional[AuthorizedSignatory]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.contracts.v_2.<a href="src/candid/resources/contracts/resources/v_2/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import uuid

from candid import CandidApiClient

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.contracts.v_2.delete(
    contract_id=uuid.UUID(
        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**contract_id:** `ContractId` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.contracts.v_2.<a href="src/candid/resources/contracts/resources/v_2/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import uuid

from candid import CandidApiClient
from candid.resources.commons import Regions_States, State
from candid.resources.contracts.resources.v_2 import (
    AuthorizedSignatoryUpdate_Set,
    ContractStatus,
    DateUpdate_Set,
    InsuranceTypes,
    RegionsUpdate_Set,
)

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.contracts.v_2.update(
    contract_id=uuid.UUID(
        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
    ),
    rendering_provider_ids=[
        uuid.UUID(
            "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
        )
    ],
    effective_date="string",
    expiration_date=DateUpdate_Set(value="string"),
    regions=RegionsUpdate_Set(
        value=Regions_States(
            states=[State.AA],
        )
    ),
    contract_status=ContractStatus.PENDING,
    authorized_signatory=AuthorizedSignatoryUpdate_Set(
        first_name="string",
        last_name="string",
        title="string",
        email="string",
        phone="string",
        fax="string",
    ),
    commercial_insurance_types=InsuranceTypes(),
    medicare_insurance_types=InsuranceTypes(),
    medicaid_insurance_types=InsuranceTypes(),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**contract_id:** `ContractId` 
    
</dd>
</dl>

<dl>
<dd>

**rendering_provider_ids:** `typing.Optional[typing.Set[RenderingProviderid]]` 

A rendering provider isn't contracted directly with the payer but can render
services under the contract held by the contracting provider.
Max items is 100.

    
</dd>
</dl>

<dl>
<dd>

**effective_date:** `typing.Optional[Date]` — The starting day upon which the contract is effective
    
</dd>
</dl>

<dl>
<dd>

**expiration_date:** `typing.Optional[DateUpdate]` — An optional end day upon which the contract expires
    
</dd>
</dl>

<dl>
<dd>

**regions:** `typing.Optional[RegionsUpdate]` 

If present, the contract's rendering providers will be patched to this exact
value, overriding what was set before.

    
</dd>
</dl>

<dl>
<dd>

**contract_status:** `typing.Optional[ContractStatus]` 
    
</dd>
</dl>

<dl>
<dd>

**authorized_signatory:** `typing.Optional[AuthorizedSignatoryUpdate]` 
    
</dd>
</dl>

<dl>
<dd>

**commercial_insurance_types:** `typing.Optional[InsuranceTypes]` 
    
</dd>
</dl>

<dl>
<dd>

**medicare_insurance_types:** `typing.Optional[InsuranceTypes]` 
    
</dd>
</dl>

<dl>
<dd>

**medicaid_insurance_types:** `typing.Optional[InsuranceTypes]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Credentialing V2
<details><summary><code>client.credentialing.v_2.<a href="src/candid/resources/credentialing/resources/v_2/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import datetime
import uuid

from candid import CandidApiClient
from candid.resources.commons import Regions_States, State

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.credentialing.v_2.create(
    rendering_provider_id=uuid.UUID(
        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
    ),
    contracting_provider_id=uuid.UUID(
        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
    ),
    payer_uuid=uuid.UUID(
        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
    ),
    start_date=datetime.date.fromisoformat(
        "2023-01-15",
    ),
    end_date=datetime.date.fromisoformat(
        "2023-01-15",
    ),
    regions=Regions_States(
        states=[State.AA],
    ),
    submitted_date=datetime.date.fromisoformat(
        "2023-01-15",
    ),
    payer_loaded_date=datetime.date.fromisoformat(
        "2023-01-15",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**rendering_provider_id:** `uuid.UUID` — The ID of the rendering provider covered by the credentialing span.
    
</dd>
</dl>

<dl>
<dd>

**contracting_provider_id:** `uuid.UUID` — The ID of the practice location at which the rendering provider is covered by the credentialing span.

    
</dd>
</dl>

<dl>
<dd>

**payer_uuid:** `uuid.UUID` — The ID of the payer covered by the credentialing span.
    
</dd>
</dl>

<dl>
<dd>

**regions:** `Regions` — The states covered by the credentialing span. A span may be national and cover all states.

    
</dd>
</dl>

<dl>
<dd>

**start_date:** `typing.Optional[dt.date]` — Start date of the credentialing span.
    
</dd>
</dl>

<dl>
<dd>

**end_date:** `typing.Optional[dt.date]` — End date of the credentialing span.
    
</dd>
</dl>

<dl>
<dd>

**submitted_date:** `typing.Optional[dt.date]` — Date that the credential paperwork was submitted.
    
</dd>
</dl>

<dl>
<dd>

**payer_loaded_date:** `typing.Optional[dt.date]` — Date that the payer loaded the credentialing span into their system.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.credentialing.v_2.<a href="src/candid/resources/credentialing/resources/v_2/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import uuid

from candid import CandidApiClient

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.credentialing.v_2.get(
    provider_credentialing_id=uuid.UUID(
        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**provider_credentialing_id:** `ProviderCredentialingSpanId` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.credentialing.v_2.<a href="src/candid/resources/credentialing/resources/v_2/client.py">get_all</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import uuid

from candid import CandidApiClient

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.credentialing.v_2.get_all(
    limit=1,
    page_token="eyJ0b2tlbiI6IjEiLCJwYWdlX3Rva2VuIjoiMiJ9",
    payer_uuid=uuid.UUID(
        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
    ),
    provider_id=uuid.UUID(
        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
    ),
    as_rendering_provider=True,
    as_contracting_provider=True,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Maximum number of entities per page, defaults to 100.
    
</dd>
</dl>

<dl>
<dd>

**page_token:** `typing.Optional[PageToken]` 
    
</dd>
</dl>

<dl>
<dd>

**payer_uuid:** `typing.Optional[uuid.UUID]` — Filter by payer.
    
</dd>
</dl>

<dl>
<dd>

**provider_id:** `typing.Optional[uuid.UUID]` — Filter to a particular provider. Use in conjunction as_rendering_provider and as_contracting_provider.
    
</dd>
</dl>

<dl>
<dd>

**as_rendering_provider:** `typing.Optional[bool]` — Filter to credentialing spans where the provider is a rendering provider. To use this filter provider_id is required.
    
</dd>
</dl>

<dl>
<dd>

**as_contracting_provider:** `typing.Optional[bool]` — Filter to credentialing spans where the provider is a contracting provider. To use this filter provider_id is required.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.credentialing.v_2.<a href="src/candid/resources/credentialing/resources/v_2/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Soft deletes a credentialing span rate from the system.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import uuid

from candid import CandidApiClient

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.credentialing.v_2.delete(
    provider_credentialing_id=uuid.UUID(
        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**provider_credentialing_id:** `ProviderCredentialingSpanId` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.credentialing.v_2.<a href="src/candid/resources/credentialing/resources/v_2/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import datetime
import uuid

from candid import CandidApiClient
from candid.resources.commons import Regions_States, State

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.credentialing.v_2.update(
    provider_credentialing_id=uuid.UUID(
        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
    ),
    contracting_provider_id=uuid.UUID(
        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
    ),
    payer_uuid=uuid.UUID(
        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
    ),
    start_date=datetime.date.fromisoformat(
        "2023-01-15",
    ),
    end_date=datetime.date.fromisoformat(
        "2023-01-15",
    ),
    regions=Regions_States(
        states=[State.AA],
    ),
    submitted_date=datetime.date.fromisoformat(
        "2023-01-15",
    ),
    payer_loaded_date=datetime.date.fromisoformat(
        "2023-01-15",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**provider_credentialing_id:** `ProviderCredentialingSpanId` 
    
</dd>
</dl>

<dl>
<dd>

**contracting_provider_id:** `typing.Optional[uuid.UUID]` — The ID of the practice location at which the rendering provider is covered by the credentialing span.

    
</dd>
</dl>

<dl>
<dd>

**payer_uuid:** `typing.Optional[uuid.UUID]` — The ID of the payer doing the credentialing.
    
</dd>
</dl>

<dl>
<dd>

**start_date:** `typing.Optional[dt.date]` — Start date of the credentialing span.
    
</dd>
</dl>

<dl>
<dd>

**end_date:** `typing.Optional[dt.date]` — End date of the credentialing span.
    
</dd>
</dl>

<dl>
<dd>

**regions:** `typing.Optional[Regions]` — The states covered by the credentialing span. A span may be national and cover all states.

    
</dd>
</dl>

<dl>
<dd>

**submitted_date:** `typing.Optional[dt.date]` — Date that the credential paperwork was submitted.
    
</dd>
</dl>

<dl>
<dd>

**payer_loaded_date:** `typing.Optional[dt.date]` — Date that the payer loaded the credentialing span into their system.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## CustomSchemas V1
<details><summary><code>client.custom_schemas.v_1.<a href="src/candid/resources/custom_schemas/resources/v_1/client.py">get_multi</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns all custom schemas.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from candid import CandidApiClient

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.custom_schemas.v_1.get_multi()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.custom_schemas.v_1.<a href="src/candid/resources/custom_schemas/resources/v_1/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Return a custom schema with a given ID.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import uuid

from candid import CandidApiClient

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.custom_schemas.v_1.get(
    schema_id=uuid.UUID(
        "ec096b13-f80a-471d-aaeb-54b021c9d582",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**schema_id:** `SchemaId` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.custom_schemas.v_1.<a href="src/candid/resources/custom_schemas/resources/v_1/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create custom schema with a set of typed keys. Schema keys can be referenced as inputs in user-configurable rules in the Rules
Engine, and key-value pairs can be attached to claims via the Encounters API.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from candid import CandidApiClient
from candid.resources.commons import Primitive
from candid.resources.custom_schemas.resources.v_1 import SchemaField

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.custom_schemas.v_1.create(
    name="General Medicine",
    description="Values associated with a generic visit",
    fields=[
        SchemaField(
            key="provider_category",
            type=Primitive.STRING,
        ),
        SchemaField(
            key="is_urgent_care",
            type=Primitive.BOOLEAN,
        ),
        SchemaField(
            key="bmi",
            type=Primitive.DOUBLE,
        ),
        SchemaField(
            key="age",
            type=Primitive.INTEGER,
        ),
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**fields:** `typing.Sequence[SchemaField]` 
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.custom_schemas.v_1.<a href="src/candid/resources/custom_schemas/resources/v_1/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update the name, description, or keys on a preexisting schema.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import uuid

from candid import CandidApiClient
from candid.resources.commons import Primitive
from candid.resources.custom_schemas.resources.v_1 import SchemaField

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.custom_schemas.v_1.update(
    schema_id=uuid.UUID(
        "ec096b13-f80a-471d-aaeb-54b021c9d582",
    ),
    name="General Medicine and Health",
    description="Values collected during all visits",
    fields_to_add=[
        SchemaField(
            key="visit_type",
            type=Primitive.STRING,
        )
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**schema_id:** `SchemaId` 
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**fields_to_add:** `typing.Optional[typing.Sequence[SchemaField]]` — A list of typed entries to add to schema. Only additive modifications are permitted.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Eligibility V2
<details><summary><code>client.eligibility.v_2.<a href="src/candid/resources/eligibility/resources/v_2/client.py">submit_eligibility_check</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

<Tip>Candid is deprecating support for this endpoint. It is instead recommended to use [Candid's Stedi passthrough endpoint](https://docs.joincandidhealth.com/api-reference/pre-encounter/eligibility-checks/v-1/post).
For assistance with the transition, please reference the [Transitioning to Candid's New Eligibility Endpoint](https://support.joincandidhealth.com/hc/en-us/articles/34918552872980) document in the Candid Support Center.</Tip>

This API is a wrapper around Change Healthcare's eligibility API. Below are some helpful documentation links:

- [Change Healthcare - Guides: Contents of the Eligibility Request Body](https://developers.changehealthcare.com/eligibilityandclaims/docs/contents-of-the-eligibility-request-body)
- [Change Healthcare - Guides: Use "Bare Minimum" Eligibility Requests](https://developers.changehealthcare.com/eligibilityandclaims/docs/use-bare-minimum-eligibility-requests)
- [Change Healthcare - Guides: Contents of the Eligibility Response](https://developers.changehealthcare.com/eligibilityandclaims/docs/contents-of-the-eligibility-response)
- [Change Healthcare - Guides: Eligibility JSON-to-EDI API Contents](https://developers.changehealthcare.com/eligibilityandclaims/docs/eligibility-json-to-edi-api-contents)
- [Change Healthcare - Guides: Eligibility Error Messages](https://developers.changehealthcare.com/eligibilityandclaims/docs/eligibility-error-messages)
- [Change Healthcare - Guides: FAQ](https://developers.changehealthcare.com/eligibilityandclaims/docs/frequently-asked-questions)
- [Change Healthcare - Guides: Eligibility FAQs](https://developers.changehealthcare.com/eligibilityandclaims/docs/eligibility-api-requests)
- [Change Healthcare - Guides: Sandbox API Values and Test Responses](https://developers.changehealthcare.com/eligibilityandclaims/docs/eligibility-sandbox-api-values-and-test-responses)
- [Change Healthcare - Guides: Sandbox Predefined Fields and Values](https://developers.changehealthcare.com/eligibilityandclaims/docs/sandbox-predefined-fields-and-values)
- [Change Healthcare - Guides: Using Test Payers in the Sandbox](https://developers.changehealthcare.com/eligibilityandclaims/docs/use-the-test-payers-in-the-sandbox-api)

A schema of the response object can be found here: [Change Healthcare Docs](https://developers.changehealthcare.com/eligibilityandclaims/reference/medicaleligibility)
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from candid import CandidApiClient

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.eligibility.v_2.submit_eligibility_check(
    request={"key": "value"},
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `typing.Optional[typing.Any]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.eligibility.v_2.<a href="src/candid/resources/eligibility/resources/v_2/client.py">submit_eligibility_check_availity</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

<Tip>Candid is deprecating support for this endpoint. It is instead recommended to use [Candid's Stedi passthrough endpoint](https://docs.joincandidhealth.com/api-reference/pre-encounter/eligibility-checks/v-1/post).
For assistance with the transition, please reference the [Transitioning to Candid's New Eligibility Endpoint](https://support.joincandidhealth.com/hc/en-us/articles/34918552872980) document in the Candid Support Center.</Tip>

**Availity has transitioned their GET endpoint to a POST endpoint. Candid has updated their pass-through integration to enable backwards compatibility for the GET endpoint so that customers do not have to immediately update their integrations.**

**Candid recommends integrations with the [POST endpoint](https://docs.joincandidhealth.com/api-reference/eligibility/v-2/submit-eligibility-check-availity-post) to ensure the best possible integration experience. Given the transition, Availity’s documentation will be out of sync with this endpoint.**

If you'd like access to this endpoint, please reach out to support@joincandidhealth.com with the subject line "Action: Activate Availity Eligibility API Endpoint

This API is a wrapper around Availity's coverages API. Below are some helpful documentation links:

- [Availity - Coverages 1.0.0 API](https://developer.availity.com/partner/documentation#c_coverages_references)
- [Candid Availity Eligibility Integration Guide](https://support.joincandidhealth.com/hc/en-us/articles/24218441631892--Availity-Eligibility-Integration-Guide)

A schema of the response object can be found here: [Availity Docs](https://developer.availity.com/partner/product/191210/api/190898#/Coverages_100/operation/%2Fcoverages%2F{id}/get)

- Note Availity requires a free developer account to access this documentation.

Check connection status of Availity API and partners here:

- [Availity Trading Partner Connection Status](https://www.availity.com/status/)
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from candid import CandidApiClient

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.eligibility.v_2.submit_eligibility_check_availity()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.eligibility.v_2.<a href="src/candid/resources/eligibility/resources/v_2/client.py">submit_eligibility_check_availity_post</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

<Tip>Candid is deprecating support for this endpoint. It is instead recommended to use [Candid's Stedi passthrough endpoint](https://docs.joincandidhealth.com/api-reference/pre-encounter/eligibility-checks/v-1/post).
For assistance with the transition, please reference the [Transitioning to Candid's New Eligibility Endpoint](https://support.joincandidhealth.com/hc/en-us/articles/34918552872980) document in the Candid Support Center.</Tip>

If you'd like access to this endpoint, please reach out to support@joincandidhealth.com with the subject line "Action: Activate Availity Eligibility API Endpoint

This API is a wrapper around Availity's coverages API. Below are some helpful documentation links:

- [Availity - Coverages 1.0.0 API](https://developer.availity.com/partner/documentation#c_coverages_references)
- [Candid Availity Eligibility Integration Guide](https://support.joincandidhealth.com/hc/en-us/articles/24218441631892--Availity-Eligibility-Integration-Guide)

A schema of the response object can be found here: [Availity Docs](https://developer.availity.com/partner/product/191210/api/190898#/Coverages_100/operation/%2Fcoverages%2F{id}/get)

- Note Availity requires a free developer account to access this documentation.

Check connection status of Availity API and partners here:

- [Availity Trading Partner Connection Status](https://www.availity.com/status/)
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from candid import CandidApiClient

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.eligibility.v_2.submit_eligibility_check_availity_post(
    request={"key": "value"},
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `typing.Optional[typing.Any]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## EncounterProviders V2
<details><summary><code>client.encounter_providers.v_2.<a href="src/candid/resources/encounter_providers/resources/v_2/client.py">update_referring_provider</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import uuid

from candid import CandidApiClient
from candid.resources.commons import State, StreetAddressLongZip
from candid.resources.encounter_providers.resources.v_2 import (
    ReferringProviderUpdate,
)

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.encounter_providers.v_2.update_referring_provider(
    encounter_id=uuid.UUID(
        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
    ),
    request=ReferringProviderUpdate(
        npi="string",
        taxonomy_code="string",
        address=StreetAddressLongZip(
            address_1="123 Main St",
            address_2="Apt 1",
            city="New York",
            state=State.NY,
            zip_code="10001",
            zip_plus_four_code="1234",
        ),
        first_name="string",
        last_name="string",
        organization_name="string",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**encounter_id:** `EncounterId` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `ReferringProviderUpdate` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.encounter_providers.v_2.<a href="src/candid/resources/encounter_providers/resources/v_2/client.py">update_initial_referring_provider</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import uuid

from candid import CandidApiClient
from candid.resources.commons import QualifierCode, State, StreetAddressLongZip
from candid.resources.encounter_providers.resources.v_2 import (
    InitialReferringProviderUpdate,
)

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.encounter_providers.v_2.update_initial_referring_provider(
    encounter_id=uuid.UUID(
        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
    ),
    request=InitialReferringProviderUpdate(
        npi="string",
        taxonomy_code="string",
        address=StreetAddressLongZip(
            address_1="123 Main St",
            address_2="Apt 1",
            city="New York",
            state=State.NY,
            zip_code="10001",
            zip_plus_four_code="1234",
        ),
        qualifier=QualifierCode.DQ,
        first_name="string",
        last_name="string",
        organization_name="string",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**encounter_id:** `EncounterId` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `InitialReferringProviderUpdate` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.encounter_providers.v_2.<a href="src/candid/resources/encounter_providers/resources/v_2/client.py">update_supervising_provider</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import uuid

from candid import CandidApiClient
from candid.resources.commons import State, StreetAddressLongZip
from candid.resources.encounter_providers.resources.v_2 import (
    SupervisingProviderUpdate,
)

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.encounter_providers.v_2.update_supervising_provider(
    encounter_id=uuid.UUID(
        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
    ),
    request=SupervisingProviderUpdate(
        npi="string",
        taxonomy_code="string",
        address=StreetAddressLongZip(
            address_1="123 Main St",
            address_2="Apt 1",
            city="New York",
            state=State.NY,
            zip_code="10001",
            zip_plus_four_code="1234",
        ),
        first_name="string",
        last_name="string",
        organization_name="string",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**encounter_id:** `EncounterId` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `SupervisingProviderUpdate` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.encounter_providers.v_2.<a href="src/candid/resources/encounter_providers/resources/v_2/client.py">update_ordering_provider</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import uuid

from candid import CandidApiClient
from candid.resources.commons import State, StreetAddressLongZip
from candid.resources.encounter_providers.resources.v_2 import (
    OrderingProviderUpdate,
)

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.encounter_providers.v_2.update_ordering_provider(
    service_line_id=uuid.UUID(
        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
    ),
    request=OrderingProviderUpdate(
        npi="string",
        taxonomy_code="string",
        address=StreetAddressLongZip(
            address_1="123 Main St",
            address_2="Apt 1",
            city="New York",
            state=State.NY,
            zip_code="10001",
            zip_plus_four_code="1234",
        ),
        first_name="string",
        last_name="string",
        organization_name="string",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**service_line_id:** `ServiceLineId` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `OrderingProviderUpdate` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.encounter_providers.v_2.<a href="src/candid/resources/encounter_providers/resources/v_2/client.py">create_referring_provider</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import uuid

from candid import CandidApiClient
from candid.resources.commons import State, StreetAddressLongZip
from candid.resources.encounter_providers.resources.v_2 import ReferringProvider

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.encounter_providers.v_2.create_referring_provider(
    encounter_id=uuid.UUID(
        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
    ),
    request=ReferringProvider(
        npi="string",
        taxonomy_code="string",
        address=StreetAddressLongZip(
            address_1="123 Main St",
            address_2="Apt 1",
            city="New York",
            state=State.NY,
            zip_code="10001",
            zip_plus_four_code="1234",
        ),
        first_name="string",
        last_name="string",
        organization_name="string",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**encounter_id:** `EncounterId` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `ReferringProvider` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.encounter_providers.v_2.<a href="src/candid/resources/encounter_providers/resources/v_2/client.py">create_initial_referring_provider</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import uuid

from candid import CandidApiClient
from candid.resources.commons import QualifierCode, State, StreetAddressLongZip
from candid.resources.encounter_providers.resources.v_2 import (
    InitialReferringProvider,
)

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.encounter_providers.v_2.create_initial_referring_provider(
    encounter_id=uuid.UUID(
        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
    ),
    request=InitialReferringProvider(
        npi="string",
        taxonomy_code="string",
        address=StreetAddressLongZip(
            address_1="123 Main St",
            address_2="Apt 1",
            city="New York",
            state=State.NY,
            zip_code="10001",
            zip_plus_four_code="1234",
        ),
        qualifier=QualifierCode.DQ,
        first_name="string",
        last_name="string",
        organization_name="string",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**encounter_id:** `EncounterId` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `InitialReferringProvider` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.encounter_providers.v_2.<a href="src/candid/resources/encounter_providers/resources/v_2/client.py">create_supervising_provider</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import uuid

from candid import CandidApiClient
from candid.resources.commons import State, StreetAddressLongZip
from candid.resources.encounter_providers.resources.v_2 import (
    SupervisingProvider,
)

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.encounter_providers.v_2.create_supervising_provider(
    encounter_id=uuid.UUID(
        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
    ),
    request=SupervisingProvider(
        npi="string",
        taxonomy_code="string",
        address=StreetAddressLongZip(
            address_1="123 Main St",
            address_2="Apt 1",
            city="New York",
            state=State.NY,
            zip_code="10001",
            zip_plus_four_code="1234",
        ),
        first_name="string",
        last_name="string",
        organization_name="string",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**encounter_id:** `EncounterId` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `SupervisingProvider` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.encounter_providers.v_2.<a href="src/candid/resources/encounter_providers/resources/v_2/client.py">create_ordering_provider</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import uuid

from candid import CandidApiClient
from candid.resources.commons import State, StreetAddressLongZip
from candid.resources.encounter_providers.resources.v_2 import OrderingProvider

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.encounter_providers.v_2.create_ordering_provider(
    service_line_id=uuid.UUID(
        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
    ),
    request=OrderingProvider(
        npi="string",
        taxonomy_code="string",
        address=StreetAddressLongZip(
            address_1="123 Main St",
            address_2="Apt 1",
            city="New York",
            state=State.NY,
            zip_code="10001",
            zip_plus_four_code="1234",
        ),
        first_name="string",
        last_name="string",
        organization_name="string",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**service_line_id:** `ServiceLineId` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `OrderingProvider` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.encounter_providers.v_2.<a href="src/candid/resources/encounter_providers/resources/v_2/client.py">delete_referring_provider</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import uuid

from candid import CandidApiClient

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.encounter_providers.v_2.delete_referring_provider(
    encounter_id=uuid.UUID(
        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**encounter_id:** `EncounterId` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.encounter_providers.v_2.<a href="src/candid/resources/encounter_providers/resources/v_2/client.py">delete_initial_referring_provider</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import uuid

from candid import CandidApiClient

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.encounter_providers.v_2.delete_initial_referring_provider(
    encounter_id=uuid.UUID(
        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**encounter_id:** `EncounterId` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.encounter_providers.v_2.<a href="src/candid/resources/encounter_providers/resources/v_2/client.py">delete_supervising_provider</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import uuid

from candid import CandidApiClient

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.encounter_providers.v_2.delete_supervising_provider(
    encounter_id=uuid.UUID(
        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**encounter_id:** `EncounterId` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.encounter_providers.v_2.<a href="src/candid/resources/encounter_providers/resources/v_2/client.py">delete_ordering_provider</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import uuid

from candid import CandidApiClient

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.encounter_providers.v_2.delete_ordering_provider(
    service_line_id=uuid.UUID(
        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**service_line_id:** `ServiceLineId` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Encounters V4
<details><summary><code>client.encounters.v_4.<a href="src/candid/resources/encounters/resources/v_4/client.py">get_all</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import datetime

from candid import CandidApiClient
from candid.resources.claims import ClaimStatus
from candid.resources.encounters.resources.v_4 import EncounterSortOptions

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.encounters.v_4.get_all(
    limit=100,
    claim_status=ClaimStatus.BILLER_RECEIVED,
    sort=EncounterSortOptions.CREATED_AT_ASC,
    page_token="eyJ0b2tlbiI6IjEiLCJwYWdlX3Rva2VuIjoiMiJ9",
    date_of_service_min=datetime.date.fromisoformat(
        "2019-08-24",
    ),
    date_of_service_max=datetime.date.fromisoformat(
        "2019-08-25",
    ),
    primary_payer_names="Medicare,Medicaid",
    search_term="doe",
    external_id="123456",
    diagnoses_updated_since=datetime.datetime.fromisoformat(
        "2019-08-24 14:15:22+00:00",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Maximum number of entities per page, defaults to 100.
    
</dd>
</dl>

<dl>
<dd>

**claim_status:** `typing.Optional[ClaimStatus]` — Indicates the current status of an insurance claim within the billing process.
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[EncounterSortOptions]` — Defaults to created_at:desc.
    
</dd>
</dl>

<dl>
<dd>

**page_token:** `typing.Optional[PageToken]` 
    
</dd>
</dl>

<dl>
<dd>

**date_of_service_min:** `typing.Optional[dt.date]` — Date formatted as YYYY-MM-DD; eg: 2019-08-25.
    
</dd>
</dl>

<dl>
<dd>

**date_of_service_max:** `typing.Optional[dt.date]` — Date formatted as YYYY-MM-DD; eg: 2019-08-25.
    
</dd>
</dl>

<dl>
<dd>

**primary_payer_names:** `typing.Optional[str]` — Comma delimited string.
    
</dd>
</dl>

<dl>
<dd>

**search_term:** `typing.Optional[str]` 

Filter by any of the following fields: encounter_id, claim_id, patient external_id,
patient date of birth, patient first name, patient last name,
or encounter external id.
    
</dd>
</dl>

<dl>
<dd>

**external_id:** `typing.Optional[EncounterExternalId]` — Filter to an exact match on encounter external_id, if one exists.
    
</dd>
</dl>

<dl>
<dd>

**diagnoses_updated_since:** `typing.Optional[dt.datetime]` — ISO 8601 timestamp; ideally in UTC (although not required): 2019-08-24T14:15:22Z.
    
</dd>
</dl>

<dl>
<dd>

**tag_ids:** `typing.Optional[typing.Union[TagId, typing.Sequence[TagId]]]` — Filter by name of tags on encounters.
    
</dd>
</dl>

<dl>
<dd>

**work_queue_id:** `typing.Optional[WorkQueueId]` 
    
</dd>
</dl>

<dl>
<dd>

**billable_status:** `typing.Optional[BillableStatusType]` — Defines if the Encounter is to be billed by Candid to the responsible_party. Examples for when this should be set to NOT_BILLABLE include if the Encounter has not occurred yet or if there is no intention of ever billing the responsible_party.
    
</dd>
</dl>

<dl>
<dd>

**responsible_party:** `typing.Optional[ResponsiblePartyType]` — Defines the party to be billed with the initial balance owed on the claim. Use SELF_PAY if you intend to bill self pay/cash pay.
    
</dd>
</dl>

<dl>
<dd>

**owner_of_next_action:** `typing.Optional[EncounterOwnerOfNextActionType]` — The party who is responsible for taking the next action on an Encounter, as defined by ownership of open Tasks.
    
</dd>
</dl>

<dl>
<dd>

**patient_external_id:** `typing.Optional[str]` — The patient ID from the external EMR platform for the patient
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.encounters.v_4.<a href="src/candid/resources/encounters/resources/v_4/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import uuid

from candid import CandidApiClient

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.encounters.v_4.get(
    encounter_id=uuid.UUID(
        "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**encounter_id:** `EncounterId` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.encounters.v_4.<a href="src/candid/resources/encounters/resources/v_4/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import datetime
import uuid

from candid import CandidApiClient
from candid.resources.billing_notes.resources.v_2 import BillingNoteBase
from candid.resources.claim_submission.resources.v_1 import (
    ClaimFrequencyTypeCode,
    ClaimSubmissionRecordCreate,
    ExternalClaimSubmissionCreate,
)
from candid.resources.commons import (
    BillingProviderCommercialLicenseType,
    ClaimSubmissionPayerResponsibilityType,
    DelayReasonCode,
    EmrPayerCrosswalk,
    EpsdtReferralConditionIndicatorCode,
    FacilityTypeCode,
    InsuranceTypeCode,
    IntendedSubmissionMedium,
    PatientRelationshipToInsuredCodeAll,
    PhoneNumber,
    PhoneNumberType,
    QualifierCode,
    ServiceLineUnits,
    SourceOfPaymentCode,
    State,
    StreetAddressLongZip,
    StreetAddressShortZip,
)
from candid.resources.custom_schemas.resources.v_1 import SchemaInstance
from candid.resources.diagnoses import DiagnosisCreate, DiagnosisTypeCode
from candid.resources.encounter_providers.resources.v_2 import (
    BillingProvider,
    InitialReferringProvider,
    ReferringProvider,
    RenderingProvider,
    SupervisingProvider,
)
from candid.resources.encounters.resources.v_4 import (
    BillableStatusType,
    ClaimSupplementalInformation,
    ClinicalNoteCategoryCreate,
    EpsdtReferral,
    IntakeFollowUp,
    IntakeQuestion,
    IntakeResponseAndFollowUps,
    Intervention,
    InterventionCategory,
    Lab,
    LabCodeType,
    Medication,
    NoteCategory,
    PatientHistoryCategory,
    PatientHistoryCategoryEnum,
    ReportTransmissionCode,
    ReportTypeCode,
    ResponsiblePartyType,
    ServiceAuthorizationExceptionCode,
    SynchronicityType,
    Vitals,
)
from candid.resources.guarantor.resources.v_1 import GuarantorCreate
from candid.resources.individual import (
    Gender,
    PatientClinicalTrialInfoCreate,
    PatientCreate,
    PatientNonInsurancePayerInfoCreate,
    SubscriberCreate,
)
from candid.resources.insurance_cards.resources.v_2 import InsuranceCardCreate
from candid.resources.service_facility import EncounterServiceFacilityBase
from candid.resources.service_lines.resources.v_2 import ServiceLineCreate

client = CandidApiClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
)
client.encounters.v_4.create(
    patient=PatientCreate(
        phone_numbers=[
            PhoneNumber(
                number="1234567890",
                type=PhoneNumberType.HOME,
            )
        ],
        phone_consent=True,
        email="johndoe@joincandidhealth.com",
        non_insurance_payers=[
            uuid.UUID(
                "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
            )
        ],
        non_insurance_payers_info=[
            PatientNonInsurancePayerInfoCreate(
                non_insurance_payer_id=uuid.UUID(
                    "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
                ),
                member_id="string",
                clinical_trial_info=[
                    PatientClinicalTrialInfoCreate(
                        clinical_trial_id=uuid.UUID(
                            "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
                        ),
                    )
                ],
            )
        ],
        email_consent=True,
        external_id="string",
        date_of_birth=datetime.date.fromisoformat(
            "2023-01-15",
        ),
        address=StreetAddressShortZip(
            address_1="123 Main St",
            address_2="Apt 1",
            city="New York",
            state=State.NY,
            zip_code="10001",
            zip_plus_four_code="1234",
        ),
        first_name="string",
        last_name="string",
        gender=Gender.MALE,
    ),
    billing_provider=BillingProvider(
        address=StreetAddressLongZip(
            address_1="123 Main St",
            address_2="Apt 1",
            city="New York",
            state=State.NY,
            zip_code="10001",
            zip_plus_four_code="1234",
        ),
        tax_id="string",
        npi="string",
        taxonomy_code="string",
        provider_commercial_license_type=BillingProviderCommercialLicenseType.LICENSED_CLINICAL_SOCIAL_WORKER,
        first_name="string",
        last_name="string",
        organization_name="string",
    ),
    rendering_provider=RenderingProvider(
        npi="string",
        taxonomy_code="string",
        address=StreetAddressLongZip(
            address_1="123 Main St",
            address_2="Apt 1",
            city="New York",
            state=State.NY,
            zip_code="10001",
            zip_plus_four_code="1234",
        ),
        first_name="string",
        last_name="string",
        organization_name="string",
    ),
    referring_provider=ReferringProvider(
        npi="string",
        taxonomy_code="string",
        address=StreetAddressLongZip(
            address_1="123 Main St",
            address_2="Apt 1",
            city="New York",
            state=State.NY,
            zip_code="10001",
            zip_plus_four_code="1234",
        ),
        first_name="string",
        last_name="string",
        organization_name="string",
    ),
    initial_referring_provider=InitialReferringProvider(
        npi="string",
        taxonomy_code="string",
        address=StreetAddressLongZip(
            address_1="123 Main St",
            address_2="Apt 1",
            city="New York",
            state=State.NY,
            zip_code="10001",
            zip_plus_four_code="1234",
        ),
        qualifier=QualifierCode.DQ,
        first_name="string",
        last_name="string",
        organization_name="string",
    ),
    supervising_provider=SupervisingProvider(
        npi="string",
        taxonomy_code="string",
        address=StreetAddressLongZip(
            address_1="123 Main St",
            address_2="Apt 1",
            city="New York",
            state=State.NY,
            zip_code="10001",
            zip_plus_four_code="1234",
        ),
        first_name="string",
        last_name="string",
        organization_name="string",
    ),
    service_facility=EncounterServiceFacilityBase(
        organization_name="string",
        npi="string",
        address=StreetAddressLongZip(
            address_1="123 Main St",
            address_2="Apt 1",
            city="New York",
            state=State.NY,
            zip_code="10001",
            zip_plus_four_code="1234",
        ),
        secondary_identification="string",
    ),
    subscriber_primary=SubscriberCreate(
        insurance_card=InsuranceCardCreate(
            member_id="string",
            payer_name="string",
            payer_id="string",
            rx_bin="string",
            rx_pcn="string",
            image_url_front="string",
            image_url_back="string",
            emr_payer_crosswalk=EmrPayerCrosswalk.HEALTHIE,
            group_number="string",
            plan_name="string",
            plan_type=SourceOfPaymentCode.SELF_PAY,
            insurance_type=InsuranceTypeCode.C_01,
            payer_plan_group_id=uuid.UUID(
                "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
            ),
        ),
        patient_relationship_to_subscriber_code=PatientRelationshipToInsuredCodeAll.SPOUSE,
        date_of_birth=datetime.date.fromisoformat(
            "2023-01-15",
        ),
        address=StreetAddressShortZip(
            address_1="123 Main St",
            address_2="Apt 1",
            city="New York",
            state=State.NY,
            zip_code="10001",
            zip_plus_four_code="1234",
        ),
        first_name="string",
        last_name="string",
        gender=Gender.MALE,
    ),
    subscriber_secondary=SubscriberCreate(
        insurance_card=InsuranceCardCreate(
            member_id="string",
            payer_name="string",
            payer_id="string",
            rx_bin="string",
            rx_pcn="string",
            image_url_front="string",
            image_url_back="string",
            emr_payer_crosswalk=EmrPayerCrosswalk.HEALTHIE,
            group_number="string",
            plan_name="string",
            plan_type=SourceOfPaymentCode.SELF_PAY,
            insurance_type=InsuranceTypeCode.C_01,
            payer_plan_group_id=uuid.UUID(
                "d5e9c84f-c2b2-4bf4-b4b0-7ffd7a9ffc32",
            ),
        ),
        patient_relationship_to_subscriber_code=PatientRelationshipToInsuredCodeAll.SPOUSE,
        date_of_birth=datetime.date.fromisoformat(
            "2023-01-15",
        ),
        address=StreetAddressShortZip(
            address_1="123 Main St",
            address_2="Apt 1",
            ci