from flask import Flask, Blueprint
from models import storage
from api.v1 import views as app_views


app = Flask(__name__)
"""import app views"""
from api.v1.views import app_views

"""Create a blueprint"""
app_blueprint = Blueprint('app', __name__, url_prefix='/api/v1')

"""Register the views with the blueprint"""
app_blueprint.register_blueprint(app_views)

"""Register the blueprint with your Flask app"""
app.register_blueprint(app_blueprint)

app.teardown_appcontext(storage.close())
def tear_down(exceptions=None):
    pass


if __name__ == "__main__":
    """Define host and port based on environment variables or defaults"""
    host = os.getenv('HBNB_API_HOST', '0.0.0.0')
    port = int(os.getenv('HBNB_API_PORT', 5000))

    """Run the Flask server"""
    app.run(host=host, port=port, threaded=True)

