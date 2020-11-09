import pytest
import json
import api.settings as app_settings
import api.app as api

from tests.conftest import app, client


def test_index(client):
    """initial test. ensure that the root route is available."""
    response = client.get("/")
    assert response.status_code == 200
    expected = {'hello': 'world'}
    assert expected == json.loads(response.get_data(as_text=True))


def test_get_all_rides(client):
    response = client.get("/rides")
    assert response.status_code == 200
    response_data = json.loads(response.get_data(as_text=True))
    assert 'data' in response_data
    assert isinstance(response_data['data'], list)


def test_get_ride(client):
    rideId: int = 6
    response = client.get("/rides/" + str(rideId))
    assert response.status_code == 200
    response_data = json.loads(response.get_data(as_text=True))
    assert 'data' in response_data
    assert isinstance(response_data['data'], dict)


def test_get_ride_none(client):
    rideId: int = 0
    response = client.get("/rides/" + str(rideId))
    assert response.status_code == 404
    response_data = json.loads(response.get_data(as_text=True))
    assert 'message' in response_data
    assert isinstance(response_data['message'], str)
