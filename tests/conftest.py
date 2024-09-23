"""Configuration for tests."""

from aioresponses import aioresponses
import pytest


@pytest.fixture
def mock_aioresponse():
    """Return aioresponse fixture."""
    with aioresponses() as m:
        yield m
