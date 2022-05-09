"""INGV Centro Nazionale Terremoti (Earthquakes) feed entry."""
from __future__ import annotations

from aio_quakeml_client.feed_entry import FeedEntry

from .consts import XML_TAG_INGV_ID_LOCATOR


class IngvCentroNazionaleTerremotiFeedQuakeMLEntry(FeedEntry):
    """INGV Centro Nazionale Terremoti feed entry."""

    @property
    def attribution(self) -> str | None:
        """Extract agency ID from this feed entry."""
        if self.creation_info and self.creation_info.agency_id:
            return self.creation_info.agency_id
        return None

    @property
    def id_locator(self) -> str | None:
        """Return custom id locator."""
        if self.creation_info:
            return self.creation_info.attribute([XML_TAG_INGV_ID_LOCATOR])
        return None
