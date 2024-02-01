"""Constants for feeds and feed entries."""
from __future__ import annotations

from datetime import timedelta
from typing import Final

CUSTOM_NAMESPACES: Final = {
    "http://webservices.ingv.it/fdsnws/event/1": "ingv",
}

DEFAULT_STARTTIME_DELTA: Final = timedelta(hours=24)
DEFAULT_URL: Final = "https://webservices.ingv.it/fdsnws/event/1/query"

XML_TAG_INGV_ID_LOCATOR: Final = "ingv:id_locator"
