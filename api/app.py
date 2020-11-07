from flask import Flask, jsonify
from flask_cors import CORS

import api.settings as app_settings

app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})


@app.route('/')
def index():
    return jsonify({'hello': 'world'})


@app.route('/rides', methods=['GET'])
def get_all_rides():
    if app_settings.RIDES is None:
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
                'success': True,
                'data': app_settings.RIDES
            }
        )


if __name__ == '__main__':
    app.run(debug=True)