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


@pytest.mark.parametrize("ride_id", [
    'ride',
    None,
    True,
    False,
])
def test_get_ride_failed(client, ride_id):
    assert type(ride_id) is not int
    response = client.get("/rides/" + str(ride_id))
    assert response.status_code == 404


@pytest.mark.parametrize("ride_id", [
    -54,
    0,
    2456,
    345678,
])
def test_get_ride_not_found(client, ride_id):
    assert type(ride_id) is int
    response = client.get("/rides/" + str(ride_id))
    assert response.status_code == 404
    if ride_id > 0:
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


@pytest.mark.parametrize("duration, expected_readable_duration", [
    (9000, "02:30:00"),
    (7000, "01:56:40"),
    (6000, "01:40:00"),
    (4500, "01:15:00"),
    (3000, "00:50:00"),
    (2500, "00:41:40"),
    (1000, "00:16:40"),
    (230, "00:03:50"),
])
def test_get_human_readable_ride_duration(client, duration, expected_readable_duration):
    distance   = 2
    start_time = "2020-06-19T13:41:17.031Z"
    new_ride = Ride(distance, start_time, duration)
    assert new_ride.get_human_readable_duration() == expected_readable_duration


@pytest.mark.parametrize("duration, expected_end_time", [
    (9000, "2020-06-19T16:11:17.031Z"),
    (7000, "2020-06-19T15:37:57.031Z"),
    (6000, "2020-06-19T15:21:17.031Z"),
    (4500, "2020-06-19T14:56:17.031Z"),
    (3000, "2020-06-19T14:31:17.031Z"),
    (2500, "2020-06-19T14:22:57.031Z"),
    (1000, "2020-06-19T13:57:57.031Z"),
    (230, "2020-06-19T13:45:07.031Z"),
])
def test_get_end_time_ride(client, duration, expected_end_time):
    distance   = 2
    start_time = "2020-06-19T13:41:17.031Z"
    new_ride = Ride(distance, start_time, duration)
    assert new_ride.get_end_time() == expected_end_time
