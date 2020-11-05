from flask import Flask, jsonify
from flask_cors import CORS

DEBUG = True

app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

RIDES = [
    {
        "id": 1,
        "distance": 2,
        "startTime": "2020-06-19T13:01:17.031Z",
        "duration": 9000
    },
    {
        "id": 2,
        "distance": 1,
        "startTime": "2020-06-19T12:01:17.031Z",
        "duration": 6000
    },
    {
        "id": 3,
        "distance": 5,
        "startTime": "2020-06-19T14:01:17.031Z",
        "duration": 7000
    },
    {
        "id": 4,
        "distance": 4,
        "startTime": "2020-06-19T08:32:45.031Z",
        "duration": 6500
    },
    {
        "id": 5,
        "distance": 2,
        "startTime": "2020-10-24T23:06:27.031Z",
        "duration": 3000
    },
        {
        "id": 6,
        "distance": 1,
        "startTime": "2020-10-29T18:35:22.391Z",
        "duration": 9000
    },
    {
        "id": 7,
        "distance": 3,
        "startTime": "2020-11-01T11:28:05.031Z",
        "duration": 5000
    },
    {
        "id": 8,
        "distance": 1,
        "startTime": "2020-11-06T03:55:07.031Z",
        "duration": 7000
    }
]


@app.route('/rides', methods=['GET'])
def get_all_rides():
    if RIDES is None:
        return jsonify(
            {
                'status_code': 404,
                'success': False,
                'message': 'Error. Failed to retrieve rides.'
            }
        )
    else:
        return jsonify(
            {
                'status_code': 200,
                'status': True,
                'data': RIDES
            }
        )


if __name__ == '__main__':
    app.run()