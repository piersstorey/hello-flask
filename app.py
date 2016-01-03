#!flask/bin/python
"""Flask app for use in Jenkins testing"""
from flask import Flask, jsonify

APP = Flask(__name__)


@APP.route('/')
def favicon():
    """Return message for default route."""
    return jsonify({'message': 'Hello pythonistic world'})

if __name__ == '__main__':
    APP.run(threaded=True)
