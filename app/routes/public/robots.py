from flask import current_app, send_from_directory
from . import public_bp


@public_bp.route("/robots.txt", methods=["GET"])
def robots():
    return send_from_directory(current_app.static_folder + "/site", "robots.txt")