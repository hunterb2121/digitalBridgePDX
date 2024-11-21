from flask import render_template
from . import public_bp


@public_bp.route("/about")
def about():
    return render_template("public/about.html")