from flask import Flask, jsonify
from flask_cors import CORS

import api.settings as app_settings

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

    return jsonify(
        {
            'status_code': 200,
            'success': True,
            'data': rides
        }
    ), 200


@app.route('/rides/<int:ride_id>', methods=['GET'])
def get_ride(ride_id):
    for ride in app_settings.RIDES:
        for key in ride:
            if key == 'id' and ride['id'] == ride_id:
                return jsonify(
                    {
                        'status_code': 200,
                        'success': True,
                        'data': ride
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
