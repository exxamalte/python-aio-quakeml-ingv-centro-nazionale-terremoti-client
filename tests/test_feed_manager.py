"""Test for the INGV Centro Nazionale Terremoti (Earthquakes) QuakeML feed manager."""

import asyncio
from datetime import datetime
from http import HTTPStatus

import aiohttp
from freezegun import freeze_time
import pytest
import pytz

from aio_quakeml_ingv_centro_nazionale_terremoti_client import (
    IngvCentroNazionaleTerremotiQuakeMLFeedManager,
)
from tests.utils import load_fixture


@pytest.mark.asyncio
@freeze_time("2024-01-31 11:12:13")
async def test_feed_manager(mock_aioresponse):
    """Test the feed manager."""
    home_coordinates = (42.0, 13.0)
    mock_aioresponse.get(
        "https://webservices.ingv.it/fdsnws/event/1/query?starttime=2024-01-30T11%253A12%253A00",
        status=HTTPStatus.OK,
        body=load_fixture("ingv-terremoti-3.xml"),
    )

    async with aiohttp.ClientSession(loop=asyncio.get_running_loop()) as websession:
        # This will just record calls and keep track of external ids.
        generated_entity_external_ids = []
        updated_entity_external_ids = []
        removed_entity_external_ids = []

        async def _generate_entity(external_id: str) -> None:
            """Generate new entity."""
            generated_entity_external_ids.append(external_id)

        async def _update_entity(external_id: str) -> None:
            """Update entity."""
            updated_entity_external_ids.append(external_id)

        async def _remove_entity(external_id: str) -> None:
            """Remove entity."""
            removed_entity_external_ids.append(external_id)

        feed_manager = IngvCentroNazionaleTerremotiQuakeMLFeedManager(
            websession,
            home_coordinates,
            generate_async_callback=_generate_entity,
            update_async_callback=_update_entity,
            remove_async_callback=_remove_entity,
        )
        assert (
            repr(feed_manager) == "<IngvCentroNazionaleTerremotiQuakeMLFeedManager("
            "feed=<IngvCentroNazionaleTerremotiQuakeMLFeed(home=(42.0, 13.0), "
            "url=https://webservices.ingv.it/fdsnws/event/1/query, "
            "radius=None, magnitude=None)>)>"
        )
        await feed_manager.update()
        entries = feed_manager.feed_entries
        assert entries is not None
        assert len(entries) == 4
        assert feed_manager.last_timestamp == datetime(
            2022, 3, 5, 22, 54, 12, tzinfo=pytz.utc
        )
        assert len(generated_entity_external_ids) == 4
        assert len(updated_entity_external_ids) == 0
        assert len(removed_entity_external_ids) == 0
