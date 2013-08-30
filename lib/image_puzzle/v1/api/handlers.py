"""
    handlers file contains all the methods for the app views
"""
#import sys
#import os
#sys.path.insert(0, os.path.dirname(__file__) + '/../')

from flask import jsonify, request

client = None

def get_videos():
    """ get_videos """
    try:
        videos = [{}]
    except Exception, error:
        #message = '%s: %s' % ('NotFoundError', error)
        message = "video '%s' does not exist." % error
        code = 404
        return jsonify(error=code, message=message, success=False), code
    return jsonify(data={ 'videos': videos }, success=True), 200


def get_video(video_id):
    """ get_video """
    try:
        video = {}
        #video = filter(lambda t: t['id'] == video_id, videos)
    except Exception, error:
        #message = '%s: %s' % ('NotFoundError', error)
        message = "video '%s' does not exist." % video_id
        code = 404
        return jsonify(error=code, message=message, success=False), code
    return jsonify(data={ video_id: video }, success=True), 200


def get_add_numbers():
    """ test method to return addition of two numbers """
    a = request.args.get('a', 0, type=int)
    b = request.args.get('b', 0, type=int)
    return jsonify(result=a + b)

