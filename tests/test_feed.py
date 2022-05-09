"""Test for the INGV Centro Nazionale Terremoti (Earthquakes) QuakeML feed."""
import datetime

import aiohttp
import pytest
from aio_quakeml_client.consts import UPDATE_OK, UPDATE_OK_NO_DATA

from aio_quakeml_ingv_centro_nazionale_terremoti_client.feed import (
    IngvCentroNazionaleTerremotiQuakeMLFeed,
)
from tests.utils import load_fixture


@pytest.mark.asyncio
async def test_update_ok(aresponses, event_loop):
    """Test updating feed is ok."""
    home_coordinates = (42.0, 13.0)
    aresponses.add(
        "webservices.ingv.it",
        "/fdsnws/event/1/query",
        "get",
        aresponses.Response(text=load_fixture("ingv-terremoti-1.xml"), status=200),
        match_querystring=True,
    )

    async with aiohttp.ClientSession(loop=event_loop) as websession:

        feed = IngvCentroNazionaleTerremotiQuakeMLFeed(websession, home_coordinates)
        assert (
            repr(feed) == "<IngvCentroNazionaleTerremotiQuakeMLFeed(home=(42.0, 13.0), "
            "url=https://webservices.ingv.it/fdsnws/event/1/query, "
            "radius=None, magnitude=None)>"
        )
        status, entries = await feed.update()
        assert status == UPDATE_OK
        assert entries is not None
        assert len(entries) == 1

        feed_entry = entries[0]
        assert feed_entry is not None
        assert (
            repr(feed_entry)
            == "<IngvCentroNazionaleTerremotiFeedQuakeMLEntry(id=smi:webservices.ingv.it/fdsnws/event/1/query?eventId=30116321)>"
        )
        assert (
            feed_entry.external_id
            == "smi:webservices.ingv.it/fdsnws/event/1/query?eventId=30116321"
        )
        assert feed_entry.coordinates[0] == pytest.approx(42.5218)
        assert feed_entry.coordinates[1] == pytest.approx(13.3833)
        assert round(abs(feed_entry.distance_to_home - 66.0), 1) == 0

        assert feed_entry.origin.type == "hypocenter"
        assert feed_entry.origin.evaluation_mode == "manual"
        assert feed_entry.origin.depth == 14500
        assert feed_entry.origin.depth_type == "from location"

        assert feed_entry.description == "Region name: 4 km S Campotosto (AQ)"
        assert feed_entry.type == "earthquake"

        assert (
            feed_entry.magnitude.public_id
            == "smi:webservices.ingv.it/fdsnws/event/1/query?magnitudeId=108867501"
        )
        assert feed_entry.magnitude.type == "ML"
        assert feed_entry.magnitude.mag == 2.6
        assert feed_entry.magnitude.station_count == 72
        assert (
            repr(feed_entry.magnitude)
            == "<Magnitude(smi:webservices.ingv.it/fdsnws/event/1/query?magnitudeId=108867501)>"
        )

        assert feed_entry.creation_info.agency_id == "INGV"
        assert feed_entry.creation_info.author == "hew10_mole#MOD_EQASSEMBLE"
        assert feed_entry.creation_info.creation_time == datetime.datetime(
            2022, 3, 1, 22, 54, 13, tzinfo=datetime.timezone.utc
        )

        assert feed_entry.attribution == "INGV"
        assert feed_entry.id_locator == "411691"


@pytest.mark.asyncio
async def test_update_ok_with_radius_filter(aresponses, event_loop):
    """Test updating feed is ok with radius filter."""
    home_coordinates = (42.0, 13.0)
    async with aiohttp.ClientSession(loop=event_loop) as websession:

        feed = IngvCentroNazionaleTerremotiQuakeMLFeed(
            websession, home_coordinates, filter_radius=100.0
        )
        assert (
            repr(feed) == "<IngvCentroNazionaleTerremotiQuakeMLFeed(home=(42.0, 13.0), "
            "url=https://webservices.ingv.it/fdsnws/event/1/query?lat=42.0&lon=13.0&maxradiuskm=100.0, "
            "radius=100.0, magnitude=None)>"
        )


@pytest.mark.asyncio
async def test_update_ok_with_minimum_magnitude_filter(aresponses, event_loop):
    """Test updating feed is ok with minimum magnitude filter."""
    home_coordinates = (42.0, 13.0)
    async with aiohttp.ClientSession(loop=event_loop) as websession:

        feed = IngvCentroNazionaleTerremotiQuakeMLFeed(
            websession, home_coordinates, filter_minimum_magnitude=3.0
        )
        assert (
            repr(feed) == "<IngvCentroNazionaleTerremotiQuakeMLFeed(home=(42.0, 13.0), "
            "url=https://webservices.ingv.it/fdsnws/event/1/query?minmag=3.0, "
            "radius=None, magnitude=3.0)>"
        )


@pytest.mark.asyncio
async def test_update_ok_with_radius_and_minimum_magnitude_filter(
    aresponses, event_loop
):
    """Test updating feed is ok with radius and minimum magnitude filter."""
    home_coordinates = (42.0, 13.0)
    async with aiohttp.ClientSession(loop=event_loop) as websession:

        feed = IngvCentroNazionaleTerremotiQuakeMLFeed(
            websession,
            home_coordinates,
            filter_radius=100.0,
            filter_minimum_magnitude=3.0,
        )
        assert (
            repr(feed) == "<IngvCentroNazionaleTerremotiQuakeMLFeed(home=(42.0, 13.0), "
            "url=https://webservices.ingv.it/fdsnws/event/1/query?lat=42.0&lon=13.0&maxradiuskm=100.0&minmag=3.0, "
            "radius=100.0, magnitude=3.0)>"
        )


@pytest.mark.asyncio
async def test_empty_feed(aresponses, event_loop):
    """Test updating feed is ok when feed does not contain entries with coordinates."""
    home_coordinates = (42.0, 13.0)
    aresponses.add(
        "webservices.ingv.it",
        "/fdsnws/event/1/query",
        "get",
        aresponses.Response(text=load_fixture("ingv-terremoti-2.xml"), status=200),
        match_querystring=True,
    )

    async with aiohttp.ClientSession(loop=event_loop) as websession:

        feed = IngvCentroNazionaleTerremotiQuakeMLFeed(websession, home_coordinates)
        assert (
            repr(feed) == "<IngvCentroNazionaleTerremotiQuakeMLFeed(home=(42.0, 13.0), "
            "url=https://webservices.ingv.it/fdsnws/event/1/query, "
            "radius=None, magnitude=None)>"
        )
        status, entries = await feed.update()
        assert status == UPDATE_OK
        assert entries is not None
        assert len(entries) == 0
        assert feed.last_timestamp is None


@pytest.mark.asyncio
async def test_update_not_xml(aresponses, event_loop):
    """Test updating feed where returned payload is not XML."""
    home_coordinates = (42.0, 13.0)
    not_xml = "\x00\x00\x00"
    aresponses.add(
        "webservices.ingv.it",
        "/fdsnws/event/1/query",
        "get",
        aresponses.Response(text=not_xml, status=200),
    )

    async with aiohttp.ClientSession(loop=event_loop) as websession:
        feed = IngvCentroNazionaleTerremotiQuakeMLFeed(websession, home_coordinates)
        assert (
            repr(feed) == "<IngvCentroNazionaleTerremotiQuakeMLFeed(home=(42.0, 13.0), "
            "url=https://webservices.ingv.it/fdsnws/event/1/query, "
            "radius=None, magnitude=None)>"
        )
        status, entries = await feed.update()
        assert status == UPDATE_OK_NO_DATA
        assert entries is None
