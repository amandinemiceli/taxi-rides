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


@pytest.mark.parametrize("start_time, duration, expected_end_time", [
    ("2020-11-06T13:41:17.031Z", 9000, "2020-11-06T16:11:17.031Z"),
    ("2020-11-06T13:41:17.031Z", 7000, "2020-11-06T15:37:57.031Z"),
    ("2020-11-06T13:41:17.031Z", 6000, "2020-11-06T15:21:17.031Z"),
    ("2020-11-06T13:41:17.031Z", 4500, "2020-11-06T14:56:17.031Z"),
    ("2020-11-06T13:41:17.031Z", 3000, "2020-11-06T14:31:17.031Z"),
    ("2020-11-06T13:41:17.031Z", 2500, "2020-11-06T14:22:57.031Z"),
    ("2020-11-06T13:41:17.031Z", 1000, "2020-11-06T13:57:57.031Z"),
    ("2020-11-06T13:41:17.031Z", 230, "2020-11-06T13:45:07.031Z"),
    ("2020-11-06T23:41:17.031Z", 9000, "2020-11-07T02:11:17.031Z"),
    ("2020-11-06T23:59:59.031Z", 2100, "2020-11-07T00:34:59.031Z"),
])
def test_get_end_time_ride(client, start_time, duration, expected_end_time):
    new_ride = Ride(2, start_time, duration)
    assert new_ride.get_end_time() == expected_end_time


@pytest.mark.parametrize("start_time, expected_result", {
    ("2020-11-06T11:28:05.031Z", False),
    ("2020-11-06T15:03:45.031Z", False),
    ("2020-11-06T15:59:59.031Z", False),
    ("2020-11-06T16:00:00.031Z", True),
    ("2020-11-06T18:59:59.031Z", True),
    ("2020-11-06T19:00:00.031Z", False),
    ("2020-11-06T01:57:57.031Z", False),
    ("2020-11-06T05:22:35.031Z", False),
})
def test_is_busy_hour(client, start_time, expected_result):
    new_ride = Ride(1, start_time, 3000)
    assert new_ride.is_busy_hour() == expected_result


@pytest.mark.parametrize("start_time, expected_result", {
    ("2020-11-06T11:28:05.031Z", False),
    ("2020-11-06T15:03:45.031Z", False),
    ("2020-11-06T18:44:23.031Z", False),
    ("2020-11-06T19:59:59.031Z", False),
    ("2020-11-06T20:00:00.031Z", True),
    ("2020-11-06T01:39:12.031Z", True),
    ("2020-11-06T03:22:35.031Z", True),
    ("2020-11-06T05:59:59.031Z", True),
    ("2020-11-06T06:00:00.031Z", False),
    ("2020-11-06T12:23:51.031Z", False),

})
def test_is_night_hour(client, start_time, expected_result):
    new_ride = Ride(1, start_time, 3000)
    assert new_ride.is_night_hour() == expected_result


@pytest.fixture
def ride_cost_per_mile():
    ride_cost = app_settings.COST_PER_MILE
    return ride_cost


@pytest.mark.parametrize("distance, expected_cost", [
    (0, 0),
    (1, 2.5),
    (3, 7.5),
    (5, 12.5),
    (7, 17.5),
])
def test_ride_cost_distance_only(client, ride_cost_per_mile, distance, expected_cost):
    ride_cost = ride_cost_per_mile * distance
    assert ride_cost == expected_cost


@pytest.mark.parametrize("distance, expected_cost", [
    (0, 1),
    (5, 13.5),
    (7, 18.5),
    (1, 3.5),
    (2, 6),
    (10, 26),
    (7, 18.5),
    (3, 8.5),
    (8, 21),
    (25, 63.5),
    (5, 13.5),
    (4, 11),
    (161, 403.5),
    (13, 33.5),
    (6, 16),
    (44, 111),
    (250, 626),
    (33, 83.5),
    (806, 2016),
])
def test_ride_cost_without_extra(client, ride_cost_per_mile, distance, expected_cost):
    ride_cost = app_settings.INITIAL_CHARGE
    ride_cost += ride_cost_per_mile * distance
    assert ride_cost == expected_cost


@pytest.mark.parametrize("distance, start_time, duration, expected_cost", [
    (0, "2020-11-06T11:28:05.031Z", 0, 1),
    (2, "2020-11-06T15:03:45.031Z", 500, 6),
    (10, "2020-11-06T15:59:59.031Z", 1000, 26),
    (5, "2020-11-06T16:00:00.031Z", 2500, 14.5),
    (7, "2020-11-06T18:59:59.031Z", 7000, 19.5),
    (3, "2020-11-06T19:00:00.031Z", 6300, 8.5),
    (8, "2020-11-06T01:57:57.031Z", 150, 21.5),
    (25, "2020-11-06T05:22:35.031Z", 390, 64),
    (5, "2020-11-06T11:28:05.031Z", 2150, 13.5),
    (4, "2020-11-06T15:03:45.031Z", 999, 11),
    (161, "2020-11-06T18:44:23.031Z", 5600, 404.5),
    (1, "2020-11-06T19:59:59.031Z", 1760, 3.5),
    (13, "2020-11-06T20:00:00.031Z", 3450, 34),
    (6, "2020-11-06T01:39:12.031Z", 620, 16.5),
    (44, "2020-11-06T03:22:35.031Z", 2050, 111.5),
    (250, "2020-11-06T05:59:59.031Z", 8000, 626.5),
    (33, "2020-11-06T06:00:00.031Z", 7100, 83.5),
    (806, "2020-11-06T12:23:51.031Z", 9000, 2016),
])
def test_calculate_ride_cost(client, ride_cost_per_mile, distance, start_time, duration, expected_cost):
    new_ride = Ride(distance, start_time, duration)
    assert new_ride.calculate_ride_cost() == expected_cost
