from flask import session, render_template, request, redirect, url_for, flash
from flask_login import login_user
from ...models.VolunteersModel import VolunteersModel
from ...utils.rbac_helpers import set_user_roles_in_session
from . import auth_bp


@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form["password"]
        volunteer = VolunteersModel.find_by_email(email)
        if volunteer and VolunteersModel.check_hash(volunteer["password_hash"], password):
            login_user(volunteer)
            set_user_roles_in_session(volunteer["id"])
            session["name"] = volunteer["name"]
            session["id"] = volunteer["id"]
            flash("Logged in successfully!", "success")
            return redirect(url_for("dashboard"))
        flash("Invalid email or password.", "danger")
    return render_template("login.html")