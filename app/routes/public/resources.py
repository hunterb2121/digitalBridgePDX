from flask import render_template
from . import public_bp


@public_bp.route("/resources")
def resources():
    return render_template("public/resources.html")