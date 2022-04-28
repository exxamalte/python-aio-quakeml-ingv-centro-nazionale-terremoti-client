"""INGV Centro Nazionale Terremoti (Earthquakes) feed manager."""
from typing import Awaitable, Callable, Tuple

from aio_quakeml_client.feed_manager import QuakeMLFeedManagerBase
from aio_quakeml_client.status_update import StatusUpdate
from aiohttp import ClientSession

from .feed import IngvCentroNazionaleTerremotiQuakeMLFeed


class IngvCentroNazionaleTerremotiQuakeMLFeedManager(QuakeMLFeedManagerBase):
    def __init__(
        self,
        websession: ClientSession,
        coordinates: Tuple[float, float],
        filter_radius: float = None,
        filter_minimum_magnitude: float = None,
        generate_async_callback: Callable[[str], Awaitable[None]] = None,
        update_async_callback: Callable[[str], Awaitable[None]] = None,
        remove_async_callback: Callable[[str], Awaitable[None]] = None,
        status_async_callback: Callable[[StatusUpdate], Awaitable[None]] = None,
    ):
        """Initialize the INGV Centro Nazionale Terremoti Feed Manager."""
        feed = IngvCentroNazionaleTerremotiQuakeMLFeed(
            websession,
            coordinates,
            "URL",
            filter_radius=filter_radius,
            filter_minimum_magnitude=filter_minimum_magnitude,
        )
        super().__init__(
            feed,
            generate_async_callback,
            update_async_callback,
            remove_async_callback,
            status_async_callback,
        )
