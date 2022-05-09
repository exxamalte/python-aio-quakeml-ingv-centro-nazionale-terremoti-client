"""INGV Centro Nazionale Terremoti (Earthquakes) QuakeML feed."""
from __future__ import annotations

from typing import Dict, Tuple

from aio_quakeml_client.feed import QuakeMLFeed
from aio_quakeml_client.xml_parser.event import Event
from aiohttp import ClientSession

from .consts import (
    CUSTOM_NAMESPACES,
    URL_DEFAULT,
    URL_PATTERN_MAGNITUDE,
    URL_PATTERN_RADIUS,
    URL_PATTERN_RADIUS_MAGNITUDE,
)
from .feed_entry import IngvCentroNazionaleTerremotiFeedQuakeMLEntry


class IngvCentroNazionaleTerremotiQuakeMLFeed(
    QuakeMLFeed[IngvCentroNazionaleTerremotiFeedQuakeMLEntry]
):
    def __init__(
        self,
        websession: ClientSession,
        home_coordinates: Tuple[float, float],
        filter_radius: float = None,
        filter_minimum_magnitude: float = None,
    ):
        """Initialise this service."""
        super().__init__(websession, home_coordinates)
        # Store radius and minimum magnitude separately to use these in the URL instead of through post filter feed entries.
        self._dynamic_filter_radius = filter_radius
        self._dynamic_filter_minimum_magnitude = filter_minimum_magnitude

    def __repr__(self):
        """Return string representation of this feed."""
        return "<{}(home={}, url={}, radius={}, magnitude={})>".format(
            self.__class__.__name__,
            self._home_coordinates,
            self._fetch_url(),
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
        if self._dynamic_filter_radius and self._dynamic_filter_minimum_magnitude:
            return URL_PATTERN_RADIUS_MAGNITUDE.format(
                self._home_coordinates[0],
                self._home_coordinates[1],
                self._dynamic_filter_radius,
                self._dynamic_filter_minimum_magnitude,
            )
        else:
            if self._dynamic_filter_radius:
                return URL_PATTERN_RADIUS.format(
                    self._home_coordinates[0],
                    self._home_coordinates[1],
                    self._dynamic_filter_radius,
                )
            if self._dynamic_filter_minimum_magnitude:
                return URL_PATTERN_MAGNITUDE.format(
                    self._dynamic_filter_minimum_magnitude
                )
        return URL_DEFAULT
