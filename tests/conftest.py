"""Configuration for tests."""
import pytest
from aioresponses import aioresponses


@pytest.fixture
def mock_aioresponse():
    """Return aioresponse fixture."""
    with aioresponses() as m:
        yield m
