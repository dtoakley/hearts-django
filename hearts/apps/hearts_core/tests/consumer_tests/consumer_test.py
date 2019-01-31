import pytest
from channels.testing import HttpCommunicator

from hearts_core.consumers import HeartsConsumer




@pytest.mark.asyncio
async def test_my_consumer():
    communicator = HttpCommunicator(MyConsumer, "GET", "/test/")
    response = await communicator.get_response()
    assert response["body"] == b"test response"
    assert response["status"] == 200


