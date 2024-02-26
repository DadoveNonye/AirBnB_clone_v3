#!/usr/bin/python3
""" flask app"""

from api.v1.views import app_views
from flask import jsonify


@app_views.route("/status", methods=['GET'], strict_slashes=False)
def status():
    """checks status and returns json"""
    return jsonify({"status": "OK"})
