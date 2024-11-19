from flask import Blueprint
from .auth import auth_bp


def register_blueprints(app):
    app.register_blueprint(auth.bp)