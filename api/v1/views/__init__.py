#!/usr/bin/python3
"""Creating a flask blueprint"""

from flask import Blueprint


app_views = Blueprint("app_views", __name__, url_defaults="/api/v1")

from api.v1.views.index import *
from api.v1.views.cities import *
from api.v1.views.amenities import *
from api.v1.views.users import *
from api.v1.views.places import *
