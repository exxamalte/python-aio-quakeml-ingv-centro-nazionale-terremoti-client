# python-quakeml-ingv-centro-nazionale-terremoti-client

[![Build Status](https://github.com/exxamalte/python-aio-quakeml-ingv-centro-nazionale-terremoti-client/workflows/CI/badge.svg?branch=main)](https://github.com/exxamalte/python-aio-quakeml-ingv-centro-nazionale-terremoti-client/actions?workflow=CI)
[![PyPi](https://img.shields.io/pypi/v/aio-quakeml-ingv-centro-nazionale-terremoti-client.svg)](https://pypi.python.org/pypi/aio-quakeml-ingv-centro-nazionale-terremoti-client)
[![Version](https://img.shields.io/pypi/pyversions/aio-quakeml-ingv-centro-nazionale-terremoti-client.svg)](https://pypi.python.org/pypi/aio-quakeml-ingv-centro-nazionale-terremoti-client)

This library provides convenient async access to the INGV Centro Nazionale Terremoti (Earthquakes) QuakeML feeds.


**Example**
```python
import asyncio
from aiohttp import ClientSession
from aio_quakeml_ingv_centro_nazionale_terremoti_client import IngvCentroNazionaleTerremotiQuakeMLFeed
async def main() -> None:
    async with ClientSession() as websession:    
        # Home Coordinates: Latitude: -33.0, Longitude: 150.0
        # Filter radius: 500 km
        feed = IngvCentroNazionaleTerremotiQuakeMLFeed(websession, 
                                                       (-33.0, 150.0),
                                                       filter_radius=50000,
                                                       filter_minimum_magnitude=2.0)
        status, entries = await feed.update()
        print(status)
        print(entries)
asyncio.get_event_loop().run_until_complete(main())
```
