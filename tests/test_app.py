import pytest, json

from api.models.ride import Ride
import api.settings as app_settings

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


def test_ride_class(client):
    distance   = 2
    start_time = "2020-06-19T13:01:17.031Z"
    duration   = 9000
    new_ride = Ride(distance, start_time, duration)
    assert new_ride.distance == distance
    assert new_ride.start_time == start_time
    assert new_ride.duration == duration
