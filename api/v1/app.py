#!/usr/bin/python3
"""creates the app.py"""
from flask import Flask, jsonify
from flask_cors import CORS
from models import storage
from api.v1.views import app_views
import os

app = Flask(__name__)

# enable CORS and allow for origins:
CORS(app, resources={r'/api/v1/*': {'origins': '0.0.0.0'}})

app.register_blueprint(app_views)
app.url_map.strict_slashes = False


# Register blueprint for API routes
app.register_blueprint(app_views)

@app.teardown_appcontext
def teardown(error):
    """Closes the SQL session when the application context is destroyed."""
    storage.close()

# Define a handler for 404 errors
@app.errorhandler(404)
def not_found_error(error):
    return jsonify({"error": "Not found"}), 404

if __name__ == "__main__":
     # Get host and port from environment variables or use defaults
    host = os.getenv('HBNB_API_HOST', '0.0.0.0')
    port = int(os.getenv('HBNB_API_PORT', 5000))

    # Run the Flask application
    app.run(host=host, port=port, threaded=True)
