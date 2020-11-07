import json

from tests.conftest import app, client


def test_index(client):
    """initial test. ensure that the root route is available."""
    response = client.get("/")
    assert response.status_code == 200
    expected = {'hello': 'world'}
    assert expected == json.loads(response.get_data(as_text=True))
