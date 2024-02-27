#!/usr/bin/python3
""" flask app"""

from api.v1.views import app_views
from flask import Flask, jsonify
from models import storage

app = Flask(__name__)

app.register_blueprint(app_views)


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

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
