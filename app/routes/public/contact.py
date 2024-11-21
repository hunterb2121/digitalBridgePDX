from flask import render_template
from . import public_bp


@public_bp.route("/contact")
def contact():
    return render_template("public/contact.html")