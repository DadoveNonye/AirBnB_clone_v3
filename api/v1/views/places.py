#!/usr/bin/python
"""Place objects that handles all default RESTFul API actions"""

from flask import jsonify, abort, request
from api.v1.views import app_views
from models import storage
from models.place import Place

@app_views.route('/places', methods=['GET'])
def get_places():
    places = storage.all(Place)
    return jsonify([place.to_dict() for place in places.values()])