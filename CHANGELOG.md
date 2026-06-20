# Changes

## 2026.6.0 (20/06/2026)
* Added Python 3.13 and 3.14 support.
* Removed Python 3.9 and 3.10 support.
* Bumped aio_quakeml_client to 2026.6.0.
* Code quality improvements.
* Changing to date-based versioning

## 0.4 (02/02/2024)
* Added Python 3.12 support.
* Bumped aio_quakeml_client to v0.7.
* Bumped library versions: black, flake8, isort.
* Migrated to pytest.
* Code quality improvements.

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
