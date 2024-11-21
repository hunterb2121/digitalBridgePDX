from flask import Blueprint
from .auth import auth_bp
from .public import public_bp


def register_blueprints(app):
    app.register_blueprint(auth_bp)
    app.register_blueprint(public_bp)