"""INGV Centro Nazionale Terremoti (Earthquakes) feed entry."""
from aio_quakeml_client.feed_entry import FeedEntry


class IngvCentroNazionaleTerremotiFeedQuakeMLEntry(FeedEntry):
    """INGV Centro Nazionale Terremoti feed entry."""

    @property
    def attribution(self) -> str | None:
        """Extract agency ID from this feed entry."""
        if self.creation_info and self.creation_info.agency_id:
            return self.creation_info.agency_id
        return None
