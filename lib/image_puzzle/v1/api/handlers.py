"""
    handlers file contains all the methods for the app views
"""
import os
import sys
sys.path.insert(0, os.path.dirname(__file__) + '/../../../')

from image_puzzle.v1.lib.images import Images
from flask import jsonify, request

images = Images()

def get_images():
    """ get_image """
    try:
        image_url = images.read()
    except Exception, error:
        message = '%s: %s' % (error.__class__.__name__, error)
        return jsonify(message=message, success=False), 500
    return jsonify(image_url) 
