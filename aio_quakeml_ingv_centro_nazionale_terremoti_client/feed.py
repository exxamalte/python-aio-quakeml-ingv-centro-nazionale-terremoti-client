"""INGV Centro Nazionale Terremoti (Earthquakes) QuakeML feed."""
from typing import Dict, Tuple

from aio_quakeml_client.feed import QuakeMLFeed
from aio_quakeml_client.xml_parser.event import Event

from .feed_entry import IngvCentroNazionaleTerremotiFeedQuakeMLEntry


class IngvCentroNazionaleTerremotiQuakeMLFeed(QuakeMLFeed):
    def _new_entry(
        self, home_coordinates: Tuple[float, float], event: Event, global_data: Dict
    ) -> IngvCentroNazionaleTerremotiFeedQuakeMLEntry:
        """Generate a new entry."""
        return IngvCentroNazionaleTerremotiFeedQuakeMLEntry(home_coordinates, event)
