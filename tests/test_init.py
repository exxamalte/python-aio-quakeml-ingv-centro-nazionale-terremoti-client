"""Tests for the INGV Centro Nazionale Terremoti (Earthquakes) QuakeML feed general setup."""

from aio_quakeml_ingv_centro_nazionale_terremoti_client import __version__


def test_version():
    """Test for version tag."""
    assert __version__ is not None
