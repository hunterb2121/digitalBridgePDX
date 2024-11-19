from flask import redirect, url_for, flash, session
from flask_login import login_required, logout_user
from . import auth_bp


@auth_bp.route("/logout")
@login_required
def logout():
    logout_user()
    session.clear()
    flash("You have been logged out.", "success")
    return redirect(url_for("auth.login"))