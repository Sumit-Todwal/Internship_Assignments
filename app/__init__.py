from flask import Flask
import os

def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_pyfile('config.py')

    from app.routes.dashboard import dashboard_bp
    from app.routes.device import device_bp
    from app.routes.auth import auth_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(dashboard_bp, url_prefix='/dashboard')
    app.register_blueprint(device_bp, url_prefix='/device')

    return app
