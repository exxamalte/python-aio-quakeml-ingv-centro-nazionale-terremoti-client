# Changes

## 0.3 (28/01/2023)
* Added Python 3.11 support.
* Removed deprecated asynctest dependency.
* Bumped aio_quakeml_client to v0.6.
* Bumped library versions: black.

## 0.2 (11/05/2022)
* Fetching events from the last 24 hours now by default.
* Time delta configurable to retrieve more (older) or fewer (recent) events.

## 0.1 (10/05/2022)
* Initial release as base for the INGV Centro Nazionale Terremoti (Earthquakes) QuakeML feed.
* Extracts some custom attributes specific to this feed.
* Calculating distance to home coordinates.
* Support for filtering by distance and magnitude.
* Filter out entries without any geo location data.
* Simple Feed Manager.
