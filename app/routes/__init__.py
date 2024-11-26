from flask import Blueprint
from .public import public_bp
from .volunteer import volunteer_bp


def register_blueprints(app):
    app.register_blueprint(public_bp)
    app.register_blueprint(volunteer_bp)