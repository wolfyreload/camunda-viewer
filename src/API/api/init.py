import flask
from flask import Flask
from flask_compress import Compress
from flask_cors import CORS

from api.api_definition import api_definition_bp
from api.api_environment import api_environment_bp
from api.api_task import api_task_bp
from api.api_task_history import api_task_history_bp
from api.spa import spa_bp


def create_app():
    app = Flask(__name__)
    CORS(app)
    Compress(app)
    flask.json.provider.DefaultJSONProvider.sort_keys = False

    # Register the blueprints
    app.register_blueprint(api_definition_bp)
    app.register_blueprint(api_task_bp)
    app.register_blueprint(api_task_history_bp)
    app.register_blueprint(api_environment_bp)
    app.register_blueprint(spa_bp)

    return app
