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
    }
]


@app.route('/rides', methods=['GET'])
def get_all_rides():
    if RIDES is None:
        return jsonify(
            {
                'code': 404,
                'success': False,
                'message': 'Error. Failed to retrieve rides.'
            }
        )
    else:
        return jsonify(
            {
                'code': 200,
                'status': True,
                'data': RIDES
            }
        )


if __name__ == '__main__':
    app.run()