from flask import Flask
from flask_cors import CORS # type: ignore

def create_app():
    app = Flask(__name__)
    CORS(app)  # Allow Angular to access APIs

    # Register Blueprints
    from .routes.ai_routes import ai_bp
    app.register_blueprint(ai_bp, url_prefix="/api")

    return app
