from flask import Flask
from flask_cors import CORS

DEBUG = True

app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})


@app.route('/', methods=['GET'])
def hello():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()