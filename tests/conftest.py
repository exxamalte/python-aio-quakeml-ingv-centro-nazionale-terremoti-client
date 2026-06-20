"""Configuration for tests."""

from aiointercept import aiointercept
import pytest_asyncio


@pytest_asyncio.fixture
async def mock_aiointercept():
    """Return aiointercept fixture."""
    async with aiointercept(mock_external_urls=True) as m:
        yield m
