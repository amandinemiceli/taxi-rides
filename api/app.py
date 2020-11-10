from flask import Flask, jsonify
from flask_cors import CORS

import settings as app_settings
from models.ride import Ride

app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})


@app.route('/')
def index():
    return jsonify({'hello': 'world'}), 200


@app.route('/rides', methods=['GET'])
def get_all_rides():
    try:
        rides = app_settings.RIDES
    except AttributeError:
        return jsonify(
            {
                'status_code': 404,
                'success': False,
                'message': 'Error. Failed to retrieve rides.'
            }
        ), 404

    all_rides = []
    for ride in rides:
        current_ride = Ride(ride['distance'], ride['startTime'], ride['duration'])
        ride['cost'] = current_ride.calculate_ride_cost()
        all_rides.append(ride)

    return jsonify(
        {
            'status_code': 200,
            'success': True,
            'data': all_rides
        }
    ), 200


@app.route('/rides/<int:ride_id>', methods=['GET'])
def get_ride(ride_id):
    if isinstance(ride_id, int):
        try:
            rides = app_settings.RIDES
        except AttributeError:
            return jsonify(
                {
                    'status_code': 404,
                    'success': False,
                    'message': 'Error. Failed to retrieve rides.'
                }
            ), 404

        for ride in rides:
            for key in ride:
                if key == 'id' and ride['id'] == ride_id:
                    new_ride = Ride(ride['distance'], ride['startTime'], ride['duration'])
                    current_ride = dict()
                    current_ride['readableDuration'] = new_ride.get_human_readable_duration()
                    current_ride['endTime'] = new_ride.get_end_time()

                    return jsonify(
                        {
                            'status_code': 200,
                            'success': True,
                            'data': current_ride
                        }
                    ), 200

    return jsonify(
        {
            'status_code': 404,
            'success': False,
            'message': 'This ride does not exist.'
        }
    ), 404


if __name__ == '__main__':
    app.run(debug=True)
