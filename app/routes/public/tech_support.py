from flask import render_template
from . import public_bp


@public_bp.route("/tech-support")
def tech_support():
    return render_template("public/tech_support.html")