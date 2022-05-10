"""INGV Centro Nazionale Terremoti (Earthquakes) feed manager."""
from __future__ import annotations

from datetime import timedelta
from typing import Awaitable, Callable, Tuple

from aio_quakeml_client.feed_manager import QuakeMLFeedManagerBase
from aio_quakeml_client.status_update import StatusUpdate
from aiohttp import ClientSession

from .consts import DEFAULT_STARTTIME_DELTA
from .feed import IngvCentroNazionaleTerremotiQuakeMLFeed


class IngvCentroNazionaleTerremotiQuakeMLFeedManager(QuakeMLFeedManagerBase):
    """INGV Centro Nazionale Terremoti (Earthquakes) feed manager."""

    def __init__(
        self,
        websession: ClientSession,
        coordinates: Tuple[float, float],
        filter_radius: float = None,
        filter_minimum_magnitude: float = None,
        starttime_delta: timedelta = DEFAULT_STARTTIME_DELTA,
        generate_async_callback: Callable[[str], Awaitable[None]] = None,
        update_async_callback: Callable[[str], Awaitable[None]] = None,
        remove_async_callback: Callable[[str], Awaitable[None]] = None,
        status_async_callback: Callable[[StatusUpdate], Awaitable[None]] = None,
    ):
        """Initialize the INGV Centro Nazionale Terremoti Feed Manager."""
        feed = IngvCentroNazionaleTerremotiQuakeMLFeed(
            websession,
            coordinates,
            filter_radius=filter_radius,
            filter_minimum_magnitude=filter_minimum_magnitude,
            starttime_delta=starttime_delta,
        )
        super().__init__(
            feed,
            generate_async_callback,
            update_async_callback,
            remove_async_callback,
            status_async_callback,
        )
