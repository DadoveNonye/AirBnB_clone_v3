#!/usr/bin/python3
"""index that imports app_views"""
from api.v1.views import app_views
from flask import jsonify

@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status():
    """Returns a JSON response with status OK"""
    return jsonify({"status": "OK"})

