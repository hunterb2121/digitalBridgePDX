from flask import render_template
from . import public_bp


@public_bp.route("/classes")
def classes():
    return render_template("public/classes.html")