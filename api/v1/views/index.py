#!/usr/bin/python3
""" flask app"""

from api.v1.views import app_views
from flask import Blueprint, jsonify
from models import storage

app_views = Blueprint('app_views', __name__)


@app_views.route("/status", methods=['GET'])
def status():
    """checks status and returns json"""
    return jsonify({"status": "OK"})


@app_views.route('/stats', methods=['GET'])
def object_stats():
    """Retrieves the no of each object by type"""
    objects = {
            "amenities": storage.count('Amenity'),
            "cities": storage.count('City'),
            "places": storage.count('Place'),
            "reviews": storage.count('Review'),
            "states": storage.count('State'),
            "users": storage.count('User'),
            }
    return jsonify(objects)

