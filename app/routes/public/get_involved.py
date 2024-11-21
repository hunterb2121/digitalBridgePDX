from flask import render_template
from . import public_bp


@public_bp.route("/get-involved")
def get_involved():
    return render_template("public/get_involved.html")