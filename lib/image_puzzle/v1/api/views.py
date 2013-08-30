"""
    views file contains all the routes for the app and maps them to a
    specific hanlders function.
"""
from flask import Blueprint, jsonify
from image_puzzle.v1.helpers.lazy_view import LazyView

api_v1 = Blueprint('api_v1', __name__)

@api_v1.app_errorhandler(400)
@api_v1.app_errorhandler(404)
@api_v1.app_errorhandler(405)
@api_v1.app_errorhandler(500)
def default_error_handle(error=None):
    """ handle all errors with json output """
    return jsonify(error=error.code, message=error.message, success=False), \
        error.code

api_v1.add_url_rule('/videos', methods=['GET'], 
    view_func=LazyView('image_puzzle.v1.api.handlers.get_videos'))
api_v1.add_url_rule('/videos/<string:video_id>', methods=['GET'], 
    view_func=LazyView('image_puzzle.v1.api.handlers.get_video'))
