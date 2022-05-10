"""Constants for feeds and feed entries."""
from __future__ import annotations

from datetime import timedelta

CUSTOM_NAMESPACES = {
    "http://webservices.ingv.it/fdsnws/event/1": "ingv",
}

DEFAULT_STARTTIME_DELTA = timedelta(hours=24)
DEFAULT_URL = "https://webservices.ingv.it/fdsnws/event/1/query"

XML_TAG_INGV_ID_LOCATOR = "ingv:id_locator"
