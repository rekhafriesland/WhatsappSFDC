twilio-python Changelog
=======================

Here you can see the full list of changes between each twilio-python release.

[2019-06-26] Version 6.29.0
----------------------------
**Autopilot**
- Adds two new properties in Assistant i.e needs_model_build and development_stage

**Preview**
- Changed phone numbers from _URL|Path_ to `X-XCNAM-Sensitive` headers **(breaking change)**

**Verify**
- Add `MessagingConfiguration` resource to verify service


[2019-06-12] Version 6.28.0
----------------------------
**Autopilot**
- Add Webhooks resource to Autopilot Assistant.

**Flex**
- Added missing 'custom' type to Flex Flow
- Adding `integrations` to Flex Configuration

**Insights**
- Added attributes to summary.

**Messaging**
- Message API Create updated with conditional params **(breaking change)**

**Proxy**
- Document that Proxy will return a maximum of 100 records for read/list endpoints **(breaking change)**
- Remove non-updatable property parameters for Session update (mode, participants) **(breaking change)**

**Sync**
- Added reachability debouncing configuration options.

**Verify**
- Add `RateLimits` and `Buckets` resources to Verify Services
- Add `RateLimits` optional parameter on `Verification` creation.

**Twiml**
- Fix `<Room>` participantIdentity casing


[2019-05-29] Version 6.27.1
----------------------------
**Verify**
- Add `approved` to status enum


[2019-05-15] Version 6.27.0
----------------------------
**Api**
- Make `method` optional for queue members update

**Chat**
- Removed `webhook.*.format` update parameters in Service resource from public library visibility in v1 **(breaking change)**

**Insights**
- Added client metrics as sdk_edge to summary.
- Added optional query param processing_state.

**Numbers**
- Add addtional metadata fields on a Document
- Add status callback fields and parameters

**Taskrouter**
- Added `channel_optimized_routing` attribute to task-channel endpoint

**Video**
- [Rooms] Add Video Subscription API

**Wireless**
- Added `imei` to Data Session resource.
- Remove `imeisv` from Data Session resource. **(breaking change)**


[2019-05-01] Version 6.26.3
----------------------------
**Serverless**
- Documentation

**Wireless**
- Added `imeisv` to Data Session resource.


[2019-04-24] Version 6.26.2
----------------------------
**Library**
- PR #465: Prepend the repo root to the system paths during doc generation. Thanks to @childish-sambino!
- PR #463: Migrate the README to markdown. Thanks to @childish-sambino!

**Api**
- Add `verified` property to Addresses

**Numbers**
- Add API for Identites and documents

**Proxy**
- Add in use count on number instance


[2019-04-12] Version 6.26.1
----------------------------
**Library**
- PR #459: Add py37 to TravisCI config. Thanks to @childish-sambino!
- PR #458: Make the Yoyodyne watermark a raw string. Thanks to @childish-sambino!

**Flex**
- Adding PluginService to Flex Configuration

**Numbers**
- Add API for Proof of Addresses

**Proxy**
- Clarify documentation for Service and Session fetch

**Serverless**
- Serverless scaffolding


[2019-03-28] Version 6.26.0
----------------------------
**Api**
- Remove optional `if_machine` call create parameter from helper libraries **(breaking change)**
- Changed `call_sid` path parameter type on QueueMember fetch and update requests **(breaking change)**

**Voice**
- changed file names to dialing_permissions prefix **(breaking change)**

**Wireless**
- Added `ResetStatus` property to Sim resource to allow resetting connectivity via the API.


[2019-03-15] Version 6.25.2
----------------------------
**Library**
- PR #457: Add Help Center and Support Ticket links to the README. Thanks to @childish-sambino!

**Api**
- Add `machine_detection_speech_threshold`, `machine_detection_speech_end_threshold`, `machine_detection_silence_timeout` optional params to Call create request

**Flex**
- Adding Flex Channel Orchestration
- Adding Flex Flow


[2019-03-06] Version 6.25.1
----------------------------
**Twiml**
- Add `de1` to `<Conference>` regions


[2019-03-01] Version 6.25.0
----------------------------
**Api**
- Make conference participant preview parameters public

**Authy**
- Added support for FactorType and FactorStrength for Factors and Challenges

**Iam**
- First public release

**Verify**
- Add endpoint to update/cancel a Verification **(breaking change)**

**Video**
- [Composer] Make RoomSid mandatory **(breaking change)**
- [Composer] Add `enqueued` state to Composition

**Twiml**
- Update message body to not be required for TwiML `Dial` noun.


[2019-02-15] Version 6.24.1
----------------------------
**Api**
- Add `force_opt_in` optional param to Messages create request
- Add agent conference category to usage records

**Flex**
- First public release

**Taskrouter**
- Adding `reject_pending_reservations` to worker update endpoint
- Added `event_date_ms` and `worker_time_in_previous_activity_ms` to Events API response
- Add ability to filter events by TaskChannel

**Verify**
- Add `EnablePsd2` optional parameter for PSD2 on Service resource creation or update.
- Add `Amount`, `Payee` optional parameters for PSD2.


[2019-02-04] Version 6.24.0
----------------------------
**Library**
- PR #453: Switch body validator to use hex instead of base64. Thanks to @cjcodes!

**Video**
- [Recordings] Add media type filter to list operation
- [Composer] Filter Composition Hook resources by FriendlyName

**Twiml**
- Update `language` enum for `Gather` to fix language code for Filipino (Philippines) and include additional supported languages **(breaking change)**


[2019-01-11] Version 6.23.1
----------------------------
**Verify**
- Add `lookup` information in the response when creating a new verification (depends on the LookupEnabled flag being enabled at the service level)
- Add `VerificationSid` optional parameter on Verification check.


[2019-01-10] Version 6.23.0
----------------------------
**Chat**
- Mark Member attributes as PII

**Proxy**
- Remove unsupported query parameters **(breaking change)**
- Remove invalid session statuses in doc


[2019-01-02] Version 6.22.1
----------------------------
**Insights**
- Initial revision.


[2018-12-17] Version 6.22.0
----------------------------
**Authy**
- Reverted the change to `FactorType` and `FormType`, avoiding conflicts with Helper Libraries reserved words (`type`) **(breaking change)**

**Proxy**
- Remove incorrect parameter for Session List

**Studio**
- Support date created filtering on list of executions

**Taskrouter**
- Adding ability to Create, Modify and Delete Task Channels.

**Verify**
- Add `SkipSmsToLandlines`, `TtsName`, `DtmfInputRequired` optional parameters on Service resource creation or update.

**Wireless**
- Added delete action on Command resource.
- Added delete action on Sim resource.

**Twiml**
- Change `currency` from enum to string for `Pay` **(breaking change)**


[2018-11-30] Version 6.21.0
----------------------------
**Api**
- Add `interactive_data` optional param to Messages create request

**Authy**
- Required authentication for `/v1/Forms/{type}` endpoint **(breaking change)**
- Removed `Challenge.reason` to `Challenge.responded_reason`
- Removed `verification_sid` from Challenge responses
- Removed `config` param from the Factor creation
- Replaced all occurrences of `FactorType` and `FormType` in favor of a unified `Type` **(breaking change)**

**Chat**
- Add Member attributes

**Preview**
- Removed `Authy` version from `preview` subdomain in favor to `authy` subdomain. **(breaking change)**

**Verify**
- Add `CustomCode` optional parameter on Verication creation.


[2018-11-16] Version 6.20.0
----------------------------
**Messaging**
- Session API

**Twiml**
- Change `master-card` to `mastercard` as `cardType` for `Pay` and `Prompt`, remove attribute `credential_sid` from `Pay` **(breaking change)**


[2018-10-29] Version 6.19.2
----------------------------
**Api**
- Add new Balance resource:
    - url: '/v1/Accounts/{account sid}/Balance'
    - supported methods: GET
    - returns the balance of the account

**Proxy**
- Add chat_instance_sid to Service

**Verify**
- Add `Locale` optional parameter on Verification creation.


[2018-10-15] Version 6.19.1
----------------------------
**Api**
- Add <Pay> Verb Transactions category to usage records

**Twiml**
- Add support for `Pay` verb


[2018-10-15] Version 6.19.0
----------------------------
**Api**
- Add `coaching` and `call_sid_to_coach` to participant properties, create and update requests.

**Authy**
- Set public library visibility, and added PII stanza
- Dropped support for `FactorType` param given new Factor prefixes **(breaking change)**
- Supported `DELETE` actions for Authy resources
- Move Authy Services resources to `authy` subdomain

**Autopilot**
- Introduce `autopilot` subdomain with all resources from `preview.understand`

**Preview**
- Renamed Understand intent to task **(breaking change)**
- Deprecated Authy endpoints from `preview` to `authy` subdomain

**Taskrouter**
- Allow TaskQueue ReservationActivitySid and AssignmentActivitySid to not be configured for MultiTask Workspaces

**Verify**
- Add `LookupEnabled` optional parameter on Service resource creation or update.
- Add `SendDigits` optional parameter on Verification creation.
- Add delete action on Service resourse.

**Twiml**
- Add custom parameters to TwiML `Client` noun and renamed the optional `name` field to `identity`. This is a breaking change in Ruby, and applications will need to transition from `dial.client ''` and `dial.client 'alice'` formats to `dial.client` and `dial.client(identity: alice)` formats. **(breaking change)**


[2018-10-04] Version 6.18.1
----------------------------
**Preview**
- Renamed response headers for Challenge and Factors Signatures

**Video**
- [Composer] Add Composition Hook resources

**Twiml**
- Add `debug` to `Gather`
- Add `participantIdentity` to `Room`


[2018-09-28] Version 6.18.0
----------------------------
**Api**
- Set `call_sid_to_coach` parameter in participant to be `preview`

**Preview**
- Supported `totp` in Authy preview endpoints
- Allowed `latest` in Authy Challenges endpoints

**Voice**
- changed path param name from parent_iso_code to iso_code for highrisk_special_prefixes api **(breaking change)**
- added geo permissions public api


[2018-09-20] Version 6.17.0
----------------------------
**Preview**
- Add `Form` resource to Authy preview given a `form_type`
- Add Authy initial api-definitions in the 4 main resources: Services, Entities, Factors, Challenges

**Pricing**
- add voice_numbers resource (v2)

**Verify**
- Move from preview to beta **(breaking change)**


[2018-08-31] Version 6.16.4
----------------------------
**Library**
- PR #444: VCORE-3651 Add support for *for* attribute in twiml element. Thanks to @nmahure!

**Api**
- Add `call_sid_to_coach` parameter to participant create request
- Add `voice_receive_mode` param to IncomingPhoneNumbers create

**Video**
- [Recordings] Expose `offset` property in resource


[2018-08-23] Version 6.16.3
----------------------------
**Chat**
- Add User Channel instance resource


[2018-08-17] Version 6.16.2
----------------------------
**Api**
- Add Proxy Active Sessions category to usage records

**Preview**
- Add `Actions` endpoints and remove `ResponseUrl` from assistants on the Understand api

**Pricing**
- add voice_country resource (v2)


[2018-08-09] Version 6.16.1
----------------------------
**Library**
- PR #443: move index and readme_include to root. Thanks to @mbichoffe!

**Studio**
- Studio is now GA


[2018-08-03] Version 6.16.0
----------------------------
**Library**
- PR #442: Auto generate docs with sphinx. Thanks to @mbichoffe!
- PR #437: Tag and push Docker latest image when deploying with TravisCI. Thanks to @jonatasbaldin!

**Chat**
- Make message From field updatable
- Add REST API webhooks

**Notify**
- Removing deprecated `segments`, `users`, `segment_memberships`, `user_bindings` classes from helper libraries. **(breaking change)**

**Preview**
- Add new Intent Statistics endpoint
- Remove `ttl` from Assistants

**Twiml**
- Add `Connect` and `Room` for Programmable Video Rooms


[2018-07-27] Version 6.15.2
----------------------------
**Api**
- Add support for sip domains to map credential lists for registrations

**Preview**
- Remove `ttl` from Assistants

**Proxy**
- Enable setting a proxy number as reserved

**Twiml**
- Add support for SSML lang tag on Say verb


[2018-07-17] Version 6.15.1
----------------------------
**Library**
- PR #439: Override generated attributes when generating TwiML. Thanks to @cjcodes!

**Video**
- Add `group-small` room type


[2018-07-16] Version 6.15.0
----------------------------
**Library**
- PR #436: Add request body validation. Thanks to @cjcodes!

**Twiml**
- Add support for SSML on Say verb, the message body is changed to be optional **(breaking change)**


[2018-07-11] Version 6.14.10
-----------------------------
**Api**
- Add `cidr_prefix_length` param to SIP IpAddresses API

**Studio**
- Add new /Execution endpoints to begin Engagement -> Execution migration

**Video**
- [Rooms] Allow deletion of individual recordings from a room


[2018-07-05] Version 6.14.9
----------------------------
**Library**
- PR #434: Escape DOCKER_PASSWORD and DOCKER_USERNAME when logging into Docker Hub. Thanks to @jonatasbaldin!


[2018-07-05] Version 6.14.8
----------------------------
**Library**
- PR #433: Fix all Docker image build and push issues. Thanks to @jonatasbaldin!
- PR #432: Add docker to TravisCI. Thanks to @jonatasbaldin!
- PR #431: Add provider to TravisCI. Thanks to @jonatasbaldin!
- PR #430: Deploy just on tags and Python 3.6. Thanks to @jonatasbaldin!

**Api**
- Release `Call Recording Controls` feature support in helper libraries
- Add Voice Insights sub-category keys to usage records


[2018-06-29] Version 6.14.7
----------------------------
**Library**
- PR #428: Add Dockerfile and related changes to build the Docker image. Thanks to @jonatasbaldin!


[2018-06-21] Version 6.14.6
----------------------------
**Library**
- PR #429: Do not use ElementTree.__nonzero__; add test for mixed content. Thanks to @ekarson!

**Api**
- Add Fraud Lookups category to usage records

**Video**
- Allow user to set `ContentDisposition` when obtaining media URLs for Room Recordings and Compositions
- Add Composition Settings resource


[2018-06-19] Version 6.14.5
----------------------------
**Library**
- PR #425: Allow adding TwiML children with generic tag names. Thanks to @mbichoffe!
- PR #422: Allow adding text to TwiML nodes. Thanks to @ekarson!
- PR #421: Add method to validate ssl certificate. Thanks to @yannieyip!

**Twiml**
- Add methods to helper libraries to inject arbitrary text under a TwiML node


[2018-06-04] Version 6.14.4
----------------------------
**Lookups**
- Add back support for `fraud` lookup type


[2018-05-25] Version 6.14.3
----------------------------
**Library**
- PR #417: Migrate readme to rst and load it in with setup.py. Thanks to @cjcodes!


[2018-05-25] Version 6.14.2
----------------------------
**Chat**
- Add Binding and UserBinding documentation


[2018-05-25] Version 6.14.1
----------------------------
**Library**
- PR #416: Remove Python 3.3 support. Thanks to @cjcodes!

**Api**
- Add more programmable video categories to usage records
- Add 'include_subaccounts' parameter to all variation of usage_record fetch

**Studio**
- Add endpoint to delete engagements

**Trunking**
- Added cnam_lookup_enabled parameter to Trunk resource.
- Added case-insensitivity for recording parameter to Trunk resource.


[2018-05-11] Version 6.14.0
----------------------------
**Chat**
- Add Channel Webhooks resource

**Monitor**
- Update event filtering to support date/time **(breaking change)**

**Wireless**
- Updated `maturity` to `ga` for all wireless apis


[2018-04-28] Version 6.13.0
----------------------------
**Video**
- Redesign API by adding custom `VideoLayout` object. **(breaking change)**


[2018-04-20] Version 6.12.1
----------------------------
**Twiml**
- Gather input Enum: remove unnecessary "dtmf speech" value as you can now specify multiple enum values for this parameter and both "dtmf" and "speech" are already available.


[2018-04-13] Version 6.12.0
----------------------------
**Library**
- PR #413: Add incoming.allow to AccessToken VoiceGrant. Thanks to @ryan-rowland!

**Preview**
- Support for Understand V2 APIs - renames various resources and adds new fields

**Studio**
- Change parameters type from string to object in engagement resource

**Video**
- [Recordings] Change `size` type to `long`. **(breaking change)**


[2018-03-22] Version 6.11.0
----------------------------
**Lookups**
- Disable support for `fraud` lookups *(breaking change)*

**Preview**
- Add `BuildDuration` and `ErrorCode` to Understand ModelBuild

**Studio**
- Add new /Context endpoint for step and engagement resources.


[2018-03-12] Version 6.10.5
----------------------------
**Api**
- Add `caller_id` param to Outbound Calls API
- Release `trim` recording Outbound Calls API functionality in helper libraries

**Video**
- [composer] Add `room_sid` to Composition resource.

**Twiml**
- Adds support for passing in multiple input type enums when setting `input` on `Gather`


[2018-02-23] Version 6.10.4
----------------------------
**Api**
- Add `trim` param to Outbound Calls API

**Lookups**
- Add support for `fraud` lookup type

**Numbers**
- Initial Release

**Video**
- [composer] Add `SEQUENCE` value to available layouts, and `trim` and `reuse` params.


[2018-02-09] Version 6.10.3
----------------------------
**Api**
- Add `AnnounceUrl` and `AnnounceMethod` params for conference announce

**Chat**
- Add support to looking up user channels by identity in v1


[2018-01-30] Version 6.10.2
----------------------------
**Preview**
- Remove Studio Engagement Deletion

**Studio**
- Initial Release


[2018-01-30] Version 6.10.1
----------------------------
**Api**
- Add `studio-engagements` usage key

**Video**
- [omit] Beta: Allow updates to `SubscribedTracks`.
- Add `SubscribedTracks`.
- Add track name to Video Recording resource
- Add Composition and Composition Media resources


[2018-01-19] Version 6.10.1
----------------------------
**Api**
- Add `conference_sid` property on Recordings
- Add proxy and sms usage key

**Chat**
- Make user channels accessible by identity
- Add notifications logs flag parameter

**Fax**
- Added `ttl` parameter
  `ttl` is the number of minutes a fax is considered valid.

**Preview**
- Add `call_delay`, `extension`, `verification_code`, and `verification_call_sids`.
- Add `failure_reason` to HostedNumberOrders.
- Add DependentHostedNumberOrders endpoint for AuthorizationDocuments preview API.

**Taskrouter**
- Less verbose naming of cumulative and real time statistics *(breaking change)*


[2017-12-15] Version 6.10.0
----------------------------
**Library**
- Fix camelCased custom twiml parameters getting converted to lower case. (Issue #349)

**Api**
- Add `voip`, `national`, `shared_cost`, and `machine_to_machine` sub-resources to `/2010-04-01/Accounts/{AccountSid}/AvailablePhoneNumbers/{IsoCountryCode}/`
- Add programmable video keys

**Preview**
- Add `verification_type` and `verification_document_sid` to HostedNumberOrders.

**Proxy**
- Fixed typo in session status enum value

**Twiml**
- Fix Dial record property incorrectly typed as accepting TrimEnum values when it actually has its own enum of values. *(breaking change)*
- Add `priority` and `timeout` properties to Task TwiML.
- Add support for `recording_status_callback_event` for Dial verb and for Conference


[2017-12-01] Version 6.9.1
---------------------------
**Api**
- Use the correct properties for Dependent Phone Numbers of an Address *(breaking change)*
- Update Call Recordings with the correct properties

**Preview**
- Add `status` and `email` query param filters for AuthorizationDocument list endpoint

**Proxy**
- Added DELETE support to Interaction
- Standardized enum values to dash-case
- Rename Service#friendly_name to Service#unique_name

**Video**
- Remove beta flag from `media_region` and `video_codecs`

**Wireless**
- Bug fix: Changed `operator_mcc` and `operator_mnc` in `DataSessions` subresource from `integer` to `string`


[2017-11-17] Version 6.9.0
---------------------------
**Sync**
- Add TTL support for Sync objects *(breaking change)*
  - The required `data` parameter on the following actions is now optional: "Update Document", "Update Map Item", "Update List Item"
  - New actions available for updating TTL of Sync objects: "Update List", "Update Map", "Update Stream"

**Video**
- [bi] Rename `RoomParticipant` to `Participant`
- Add Recording Settings resource
- Expose EncryptionKey and MediaExternalLocation properties in Recording resource


[2017-11-10] Version 6.8.4
---------------------------
**Accounts**
- Add AWS credential type

**Preview**
- Removed `iso_country` as required field for creating a HostedNumberOrder.

**Proxy**
- Added new fields to Service: geo_match_level, number_selection_behavior, intercept_callback_url, out_of_session_callback_url


[2017-11-03] Version 6.8.3
---------------------------
**Api**
- Add programmable video keys

**Video**
- Add `Participants`


[2017-10-27] Version 6.8.2
---------------------------
**Chat**
- Add Binding resource
- Add UserBinding resource


[2017-10-20] Version 6.8.1
---------------------------
**Library**
- #394 Update request validator to remove port numbers from https urls. Thanks @Brodan!
- #385 Add request logging and hooking. Thanks @tysonholub!

**Api**
- Add `address_sid` param to IncomingPhoneNumbers create and update
- Add 'fax_enabled' option for Phone Number Search


[2017-10-13] Version 6.8.0
---------------------------
**Api**
- Add `smart_encoded` param for Messages
- Add `identity_sid` param to IncomingPhoneNumbers create and update

**Preview**
- Make 'address_sid' and 'email' optional fields when creating a HostedNumberOrder
- Add AuthorizationDocuments preview API.

**Proxy**
- Initial Release

**Wireless**
- Added `ip_address` to sim resource

**Twiml**
- Rename `number` to `phone_number` in Voice Number TwiML. *(breaking change)*
- Rename `message` to `body` in Messaging TwiML. *(breaking change)*


[2017-10-06] Version 6.7.1
---------------------------
**Preview**
- Add `acc_security` (authy-phone-verification) initial api-definitions

**Taskrouter**
- [bi] Less verbose naming of cumulative and real time statistics


[2017-09-28] Version 6.7.0
---------------------------
**Chat**
- Make member accessible through identity
- Make channel subresources accessible by channel unique name
- Set get list 'max_page_size' parameter to 100
- Add service instance webhook retry configuration
- Add media message capability
- Make `body` an optional parameter on Message creation. *(breaking change)*

**Notify**
- `data`, `apn`, `gcm`, `fcm`, `sms` parameters in `Notifications` create resource are dicts/objects instead of strings. Passing manually stringified json will continue to work.

**Taskrouter**
- Add new query ability by TaskChannelSid or TaskChannelUniqueName
- Move Events, Worker, Workers endpoint over to CPR
- Add new RealTime and Cumulative Statistics endpoints

**Video**
- Create should allow an array of video_codecs.
- Add video_codecs as a property of room to make it externally visible.


[2017-09-15] Version 6.6.3
---------------------------
**Api**
- Add `sip_registration` property on SIP Domains
- Add new video and market usage category keys


[2017-09-01] Version 6.6.2
---------------------------
- Added last_response and last_request to http_client

[2017-09-01] Version 6.6.1
---------------------------
**Sync**
- Add support for Streams

**Wireless**
- Added DataSessions sub-resource to Sims.


[2017-08-25] Version 6.6.0
---------------------------
**Library**
- Allow creating AccessTokens/Jwts without generating `nbf`. Passing `None` in the constructor will remove `nbf` from jwt payload.

**Api**
- Update `status` enum for Recordings to include 'failed'
- Add `error_code` property on Recordings

**Chat**
- Add mutable parameters for channel, members and messages

**Video**
- New `media_region` parameter when creating a room, which controls which region media will be served out of.

**Twiml**
- Add support for `speech_timeout`, `max_speech_time`, and `profanity_filter` attributes on Gather verb.


[2017-08-18] Version 6.5.2
---------------------------
**Library**
- Remove bundled certificates, use `certifi` package via `requests`.
- Add option to use connection pooling. This is enabled by default and will use one Session for all requests
in Client.
    - To disable this, pass `pool_connections` parameter when creating your Twilio client.
```python
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient

client = Client(
    username,
    password,
    http_client=TwilioHttpClient(pool_connections=False)
)
```

**Api**
- Add VoiceReceiveMode {'voice', 'fax'} option to IncomingPhoneNumber UPDATE requests

**Chat**
- Add channel message media information
- Add service instance message media information

**Preview**
- Removed 'email' from bulk_exports configuration api [bi]. No migration plan needed because api has not been used yet.
- Add DeployedDevices.

**Sync**
- Add support for Service Instance unique names

[2017-08-10] Version 6.5.1
---------------------------
Fixed PyJWT >= 1.5.1 exception


**Api**
- Add New wireless usage keys added
- Add `auto_correct_address` param for Addresses create and update
- Add ChatGrant grant and deprecate IpMessagingGrant

**Video**
- Add `video_codec` enum and `video_codecs` parameter, which can be set to either `VP8` or `H264` during room creation.
- Restrict recordings page size to 100

[2017-07-27] Version 6.5.0
---------------------------
This release adds Beta and Preview products to main artifact.

Previously, Beta and Preview products were only included in the `alpha`
artifact. They are now being included in the main artifact to ease product
discoverability and the collective operational overhead of maintaining multiple
artifacts per library.

**Api**
- Remove unused `encryption_type` property on Recordings *(breaking change)*
- Update `status` enum for Messages to include 'accepted'

**Messaging**
- Fix incorrectly typed capabilities property for PhoneNumbers.

**Notify**
- Add `ToBinding` optional parameter on Notifications resource creation. Accepted values are json strings.

**Preview**
- Add `sms_application_sid` to HostedNumberOrders.

**Taskrouter**
- Fully support conference functionality in reservations.


[2017-07-12] Version 6.4.3
---------------------------
**Api**
- Update `AnnounceMethod` parameter naming for consistency

**Notify**
- Add `ToBinding` optional parameter on Notifications resource creation. Accepted values are json strings.

**Preview**
- Add `verification_attempts` to HostedNumberOrders.
- Add `status_callback_url` and `status_callback_method` to HostedNumberOrders.

**Video**
- Filter recordings by date using the parameters `DateCreatedAfter` and `DateCreatedBefore`.
- Override the default time-to-live of a recording's media URL through the `Ttl` parameter (in seconds, default value is 3600).
- Add query parameters `SourceSid`, `Status`, `DateCreatedAfter` and `DateCreatedBefore` to the convenience method for retrieving Room recordings.

**Wireless**
- Added national and international data limits to the RatePlans resource.


[2017-06-27] Version 6.4.2
--------------------------

- Pin PyJWT to below version `1.5.1` to fix broken build.
- Fix json load error for python 3.3 - 3.5

[2017-06-16] Version 6.4.1
--------------------------

- Add several missing `<Gather>` attributes.
    - `partial_result_callback`
    - `partial_result_callback_method`
    - `language`
    - `hints`
    - `barge_in`
    - `acknowledge_sound_url`
    - `input`
- Remove client-side max page size validation.
- Support `announce_url` and `announce_url_method` on Conference Participants.
- TwiML docstring corrections.

[2017-06-15] Version 6.4.0
--------------------------

- Remove support for Python 2.6.
- Add `locality` field to `AvailablePhoneNumbers`.
- Add `origin` field to `IncomingPhoneNumbers`.
- Add `in_locality` parameter to `AvailablePhoneNumbers`.
- Add `origin` parameter to `IncomingPhoneNumbers`.
- Add new sync categories to `UsageRecords`.
- Support unicode in `validation_client`.
- Add `muted` parameter to `<Conference>` Twiml.

[2017-05-24] Version 6.3.0
--------------------------

- Rename RoomList to RoomRecordingsList.

[2017-05-19] Version 6.2.0
--------------------------

- Add video domain.
- Update usage record categories.
- Add `get_page` method for reentrant paging.

[2017-05-12] Version 6.1.2
----------------------------------

- Allow *kwargs in TwiML Gather

[2017-05-10] Version 6.1.1
----------------------------------

- Add Task verb to VoiceResponse
- Add Echo verb to VoiceResponse
- Add Sim verb to VoiceResponse

[2017-04-27] Version 6.1.0
--------------------------

- Add v2 of chat.twilio.com.
- Add `recording_channels` parameter to Participant create and update.
- Add `recording_status_callback` parameter to Participant create and update.
- Add `recording_status_callback_method` parameter to Participant create and update.
- Add `sip_auth_username` parameter to Participant create and update.
- Add `region` parameter to Participant create and update.
- Add `conference_recording_status_callback` parameter to Participant create and update.
- Add `conference_recording_status_callback_method` parameter to Participant create and update.
- Add `validity_period` parameter to Messages.

[2017-04-03] Version 6.0.0
--------------------------
**New Major Version**

The newest version of the `twilio-python` helper library!

This version brings a host of changes to update and modernize the `twilio-python` helper library. It is auto-generated to produce a more consistent and correct product.

- [Full API Documentation](https://twilio.github.io/twilio-python/)
- [General Documentation](https://www.twilio.com/docs/libraries/python)

Version 4.4.0
-------------

Released May 19, 2015:

- Add support for the beta field to IncomingPhoneNumbers and AvailablePhoneNumbers

Version 4.3.0
-------------

Released May 14, 2015:

- Add support for Call Status Events in TwiML

Version 4.2.0
-------------

Released May 7, 2015:

- Add support for the Twilio Monitor APIs: Events and Alerts

Version 4.1.0
-------------

Released May 6, 2015:

- Add support for the Twilio Pricing API

Version 4.0.0
-------------

Released April 16, 2015:

- Remove the deprecated count function from ListResource

Version 3.8.0
-------------

Released March 31, 2015:

- Support for the new Twilio Lookups API

Version 3.7.3
-------------

Released March 10, 2015:

- Add missing docstrings and examples for TaskRouter

Version 3.7.2
-------------

Released February 24, 2015:

- Restore Tokens resource to TwilioRestClient

Version 3.7.1
-------------

Released February 20, 2015:

- Restore Python 2.6 and 3.x support

Version 3.7.0
-------------

Released February 18, 2015:

- Add TaskRouterClient and resources to support the new TaskRouter API
- Stop prepending numeric error code to exception error messages

Version 3.6.15
--------------

Released January 14, 2015

- Update request construction for Tokens

Version 3.6.14
--------------

Released December 22, 2014

- Specify Python 3 dependencies in wheel package

Version 3.6.12
--------------

Released November 24, 2014

- Fix compatibility issue for Python 3.4

Version 3.6.11
--------------

Released November 21, 2014

- Add support for the new Tokens endpoint

Version 3.6.10
--------------

Released November 13, 2014

- Add support for DELETE to Call and Message records
- Add support for redacting Message body fields

Version 3.6.9
-------------

Released October 30, 2014

- Add Python 3.4 support
- Add wheel packaging
- Fix compatibility with earlier Python 2 releases

Version 3.6.8
-------------

Released October 9, 2014

- Remove unneeded unittest2py3k dependency.
- Restore backwards-compatible exception import paths.

Version 3.6.7
-------------

Released August 6, 2014

- Fix Python 2.5 compatibility.
- Add CallFeedback resources.
- Typo fixes and formatting cleanup.
- Refactor exception hierarchy and imports.
- Documentation improvements.

Version 3.6.6
--------------

Released on February 27, 2014

- Previously the error message was set based on the `tty` value; instead now we
  detect `tty` when you try to print the error message. The `msg` property of
  the exception is set to a decent value.
- `twilio-python` now uses entirely relative imports, so it may be easier to
  include it as a part of another package.

Version 3.6.5
--------------

- Remove unittest2 dependency.
- Tests no longer run against Python 2.5.
- update(), delete() work on Application, Transcription and UsageTrigger
  instance classes.

Version 3.6.4
-------------

Released November 5, 2013

- Adds support for the 'digits' attribute of Play verbs in TwiML creation.
- Updates documentation for Message TwiML verb
- Bugfix for tty detection in error formatting

Version 3.6.3
-------------

Released October 21, 2013

- Adds support for filtering by type to IncomingPhoneNumbers.

- Adds support for filtering for mobile numbers to both IncomingPhoneNumbers
  and AvailablePhoneNumbers.


Version 3.6.2
-------------

Released on September 24, 2013

- Adds support for HTTP and SOCKS4/5 proxies to the REST client.


Version 3.6.0, 3.6.1
--------------------

Released on September 18, 2013

- Adds support for the new Message and SIP resources to the REST API client.
- Adds support for the new Message verb to the TwiML generator.


Version 3.5.3, 3.5.4
--------------------

Released on September 6, 2013

- twilio-python now includes an SSL certfication file to ensure that
  connections to api.twilio.com don't fail with SSLError.

Version 3.5.2
-------------

Released on August 26, 2013

- You can now delete transcriptions

Version 3.5.1
-------------

Released on May 21, 2013

- Fixes an issue in the 3.5.0 release where null dates would cause the library
  to raise a TypeError.

Version 3.5.0
-------------

Released on May 21, 2013

- `date_created` and `date_updated` objects are now returned as Python
  `datetime.datetime` objects instead of as RFC 2822 formatted strings. This is
  a backwards incompatible change. (via [@abrinsmead](/abrinsmead))
- The library will not throw a UnicodeDecodeError when parsing API responses
  with Python 3.
- You can pass integers to Twiml arguments. (via [@jvankoten](/jvankoten))
- Ensuring the tests always pass on Python 3. (via [@ftobia](/ftobia))
- Add the list of AUTHORS
- Fixes a timing attack vector in signature validation. (via [@zacharyvoase](/zacharyvoase))

Version 3.4.5
-------------

Released on April 1, 2013

Allow the Account object to access usage records and usage trigger data, in
addition to the client. Reporter: Trenton McManus

Version 3.4.4
-------------

Adds support for Sip

Version 3.4.3
-------------

Adds correct dependencies to the `setup.py` file.

Version 3.4.2
-------------

Released on January 2, 2013

Adds a convenience function to retrieve the members of a queue by running
client.members("QU123").

Version 3.4.1
-------------

Python3 support!

Version 3.3.11
--------------

- Fix a bug where participants could not be kicked from a Conference


Version 3.3.10
--------------

- Add support for Queue. Fix a bug where the library wouldn't work in Python 2.5


Version 3.3.9
-------------

- Fix an error introduced in 3.3.7 that prevented validation calls from
  succeeding.

Version 3.3.8
-------------

- Use next_page_uri when iterating over a list resource


Version 3.3.7
-------------

- Allow arbitrary keyword arguments on resource creation and listing

Version 3.3.6
-------------

- Remove doc/tmp directory which was preventing installation on certain Windows machines
- Add Travis CI integration
- Update httplib2 dependency

Version 3.3.5
-------------

Released on January 18, 2011

- Fix a bug with the deprecated `TwilioRestClient.request` method
- Fix a bug in filtering SMS messages by DateSent

Version 3.3.4
-------------

Released on December 16, 2011

- Allow both unicode strings and encoded byte strings in request data
- Add support for SMS and Voice application sids to phone number updating
- Fix documentation error relating to phone number purchasing
- Include doc string information for decorated functions

Version 3.3.3
-------------

Released on November 3, 2011

- Support unicode characters when validating requests
- Add support for Great Britain language on the Say verb
- Set Sms Application, Voice Application, and/or a Friendly
  Name when purchasing a number
- Add missing parameters for resource creation and update

Version 3.3.2
-------------

Released on September 29, 2011

- TwiML verbs can now be used as context managers

Version 3.3.1
-------------

Released on September 27, 2011

- Allow phone numbers to be transferred between accounts and subaccounts

Version 3.3.0
-------------

Released on September 21, 2011

- Add support for Twilio Connect. Connect applications and authorized Connect
  applications are now availble via the REST client.
- Fix a problem where date and datetimes weren't coverted to strings when
  querying list resources
