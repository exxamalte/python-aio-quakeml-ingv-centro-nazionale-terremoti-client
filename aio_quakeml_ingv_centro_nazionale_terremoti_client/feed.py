"""INGV Centro Nazionale Terremoti (Earthquakes) QuakeML feed."""
from __future__ import annotations

import urllib.parse
from datetime import datetime, timedelta
from typing import Dict, Tuple

from aio_quakeml_client.feed import QuakeMLFeed
from aio_quakeml_client.xml_parser.event import Event
from aiohttp import ClientSession

from .consts import CUSTOM_NAMESPACES, DEFAULT_STARTTIME_DELTA, DEFAULT_URL
from .feed_entry import IngvCentroNazionaleTerremotiFeedQuakeMLEntry


class IngvCentroNazionaleTerremotiQuakeMLFeed(
    QuakeMLFeed[IngvCentroNazionaleTerremotiFeedQuakeMLEntry]
):
    """INGV Centro Nazionale Terremoti (Earthquakes) QuakeML feed."""

    def __init__(
        self,
        websession: ClientSession,
        home_coordinates: Tuple[float, float],
        filter_radius: float = None,
        filter_minimum_magnitude: float = None,
        starttime_delta: timedelta = DEFAULT_STARTTIME_DELTA,
    ):
        """Initialise this service."""
        super().__init__(websession, home_coordinates)
        # Store radius and minimum magnitude separately to use these in the URL instead of through post filter feed entries.
        self._dynamic_filter_radius = filter_radius
        self._dynamic_filter_minimum_magnitude = filter_minimum_magnitude
        self._starttime_delta = starttime_delta

    def __repr__(self):
        """Return string representation of this feed."""
        return "<{}(home={}, url={}, radius={}, magnitude={})>".format(
            self.__class__.__name__,
            self._home_coordinates,
            DEFAULT_URL,
            self._dynamic_filter_radius,
            self._dynamic_filter_minimum_magnitude,
        )

    def _new_entry(
        self, home_coordinates: Tuple[float, float], event: Event, global_data: Dict
    ) -> IngvCentroNazionaleTerremotiFeedQuakeMLEntry:
        """Generate a new entry."""
        return IngvCentroNazionaleTerremotiFeedQuakeMLEntry(home_coordinates, event)

    def _additional_namespaces(self) -> Dict | None:
        """Return additional XML namespaces."""
        return CUSTOM_NAMESPACES

    def _fetch_url(self):
        """Dynamically construct URL based on parameters."""
        url_parameters = {}
        if self._dynamic_filter_radius:
            url_parameters["lat"] = self._home_coordinates[0]
            url_parameters["lon"] = self._home_coordinates[1]
            url_parameters["maxradiuskm"] = self._dynamic_filter_radius
        if self._dynamic_filter_minimum_magnitude:
            url_parameters["minmag"] = self._dynamic_filter_minimum_magnitude
        if self._starttime_delta:
            # Calculate start time based on now but normalised to the last full minute.
            starttime = (
                datetime.utcnow().replace(second=0, microsecond=0)
                - self._starttime_delta
            )
            # Format required: YYYY-MM-DDThh:mm:ss
            url_parameters["starttime"] = starttime.strftime("%Y-%m-%dT%H:%M:%S")
        # Build URL.
        if len(url_parameters) > 0:
            return DEFAULT_URL + "?" + urllib.parse.urlencode(url_parameters, safe=":")
        else:
            return DEFAULT_URL
