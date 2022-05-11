# python-quakeml-ingv-centro-nazionale-terremoti-client

[![Build Status](https://github.com/exxamalte/python-aio-quakeml-ingv-centro-nazionale-terremoti-client/workflows/CI/badge.svg?branch=main)](https://github.com/exxamalte/python-aio-quakeml-ingv-centro-nazionale-terremoti-client/actions?workflow=CI)
[![codecov](https://codecov.io/gh/exxamalte/python-aio-quakeml-ingv-centro-nazionale-terremoti-client/branch/main/graph/badge.svg?token=15DT06IN30)](https://codecov.io/gh/exxamalte/python-aio-quakeml-ingv-centro-nazionale-terremoti-client)
[![PyPi](https://img.shields.io/pypi/v/aio-quakeml-ingv-centro-nazionale-terremoti-client.svg)](https://pypi.python.org/pypi/aio-quakeml-ingv-centro-nazionale-terremoti-client)
[![Version](https://img.shields.io/pypi/pyversions/aio-quakeml-ingv-centro-nazionale-terremoti-client.svg)](https://pypi.python.org/pypi/aio-quakeml-ingv-centro-nazionale-terremoti-client)

This library provides convenient async access to the INGV Centro Nazionale Terremoti (Earthquakes) QuakeML feeds.


**Examples**

Retrieve all events from the last 24 hours (default timeframe):
```python
import asyncio
from aiohttp import ClientSession
from aio_quakeml_ingv_centro_nazionale_terremoti_client import IngvCentroNazionaleTerremotiQuakeMLFeed
async def main() -> None:
    async with ClientSession() as websession:    
        # Home Coordinates: Latitude: 43.7, Longitude: 11.2
        feed = IngvCentroNazionaleTerremotiQuakeMLFeed(websession, 
                                                       (43.7, 11.2))
        status, entries = await feed.update()
        print(status)
        if entries:
            for entry in entries:
                print(f"- ID: {entry.external_id} - Magnitude: {entry.magnitude.mag} - Distance: {entry.distance_to_home:.2f}")
asyncio.get_event_loop().run_until_complete(main())
```

Retrieve all events from the last 24 hours (default timeframe) and within a radius of
100km around the provided home coordinates:
```python
import asyncio
from aiohttp import ClientSession
from aio_quakeml_ingv_centro_nazionale_terremoti_client import IngvCentroNazionaleTerremotiQuakeMLFeed
async def main() -> None:
    async with ClientSession() as websession:    
        # Home Coordinates: Latitude: 43.7, Longitude: 11.2
        # Filter radius: 100 km
        feed = IngvCentroNazionaleTerremotiQuakeMLFeed(websession, 
                                                       (43.7, 11.2),
                                                       filter_radius=100)
        status, entries = await feed.update()
        print(status)
        if entries:
            for entry in entries:
                print(f"- ID: {entry.external_id} - Magnitude: {entry.magnitude.mag} - Distance: {entry.distance_to_home:.2f}")
asyncio.get_event_loop().run_until_complete(main())
```

Retrieve all events from the last 24 hours (default timeframe), within a radius of
100km around the provided home coordinates, and with a magnitude of 2.0 or higher:
```python
import asyncio
from aiohttp import ClientSession
from aio_quakeml_ingv_centro_nazionale_terremoti_client import IngvCentroNazionaleTerremotiQuakeMLFeed
async def main() -> None:
    async with ClientSession() as websession:    
        # Home Coordinates: Latitude: 43.7, Longitude: 11.2
        # Filter radius: 100 km
        # Filter minimum magnitude: 2.0
        feed = IngvCentroNazionaleTerremotiQuakeMLFeed(websession, 
                                                       (43.7, 11.2),
                                                       filter_radius=100,
                                                       filter_minimum_magnitude=2.0)
        status, entries = await feed.update()
        print(status)
        if entries:
            for entry in entries:
                print(f"- ID: {entry.external_id} - Magnitude: {entry.magnitude.mag} - Distance: {entry.distance_to_home:.2f}")
asyncio.get_event_loop().run_until_complete(main())
```
