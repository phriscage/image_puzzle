#!/usr/bin/python
"""
API bootstrap file
"""

from flask import Flask, jsonify
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.realpath(__file__)) + '/../../lib')

app = Flask(__name__)

#@app.errorhandler(404)
#def default_error_handle(error=None):
    #return "test"

from image_puzzle.v1.api.views import api_v1
app.register_blueprint(api_v1, url_prefix="/api/v1")

def bootstrap():
    """bootstraps the application. can handle setup here"""
    app.debug = True
    app.run(host='0.0.0.0', port=8000)

if __name__ == "__main__":
    bootstrap()
