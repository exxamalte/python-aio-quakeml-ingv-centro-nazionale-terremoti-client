"""Constants for feeds and feed entries."""
from __future__ import annotations

CUSTOM_NAMESPACES = {
    "http://webservices.ingv.it/fdsnws/event/1": "ingv",
}

URL_DEFAULT = "https://webservices.ingv.it/fdsnws/event/1/query"

XML_TAG_INGV_ID_LOCATOR = "ingv:id_locator"
