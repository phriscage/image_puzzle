#!/usr/bin/python
"""
API bootstrap file
"""

from flask import Flask, jsonify
import sys
import os
import argparse

sys.path.insert(0, os.path.dirname(os.path.realpath(__file__)) + '/../lib')

app = Flask(__name__)

#@app.errorhandler(404)
#def default_error_handle(error=None):
    #return "test"

from image_puzzle.v1.api.views import api_v1
app.register_blueprint(api_v1, url_prefix="/api/v1")

def bootstrap(**kwargs):
    """bootstraps the application. can handle setup here"""
    app.debug = True
    app.run(host=kwargs['host'], port=kwargs['port'])


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--host", help="Hostname or IP address",
        dest="host", type=str, default='0.0.0.0')
    parser.add_argument("--port", help="Port number",
        dest="port", type=int, default=8000)
    kwargs = parser.parse_args()
    bootstrap(**kwargs.__dict__)
