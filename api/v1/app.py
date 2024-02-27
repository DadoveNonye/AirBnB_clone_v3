#!/usr/bin/python3
""" 
    Flask application creation from blueprint
"""


# Import required modules
from flask import Flask, jsonify
from models import storage
from api.v1.views import app_views
import os
#from flask_cors import CORS


# creating flask instance
app = Flask(__name__)


# Blueprint registration for app_views
app.register_blueprint(app_views)


# Initialize CORS
#CORS(app, resources={r"/*": {"origins": "0.0.0.0"}})


# method to handle teardown. 
@app.teardown_appcontext
def teardown(exception):
    """Closing the sql session"""
    storage.close()


@app.errorhandler(404)
def error_not_found(error):
    """handles 404 error"""
    return jsonify({"error": "Not found"}), 404


if __name__ == "__main__":
    host = os.getenv('HBNB_API_HOST', '0.0.0.0')
    port = int(os.getenv('HBNB_API_PORT', 5000))
    # getenv returns a string and port is an int
    # THREADED is set to true so it can serve multiple requests at once
    app.run(host=host, port=port, threaded=True)
