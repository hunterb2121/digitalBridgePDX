from functools import wraps
from flask import session, redirect, url_for, flash
from flask_login import current_user
from ..models.Volunteers import Volunteers
from ..models.UserRoles import UserRoles
from ..models.SiteRoles import SiteRoles


def get_user_roles(volunteer_id):
    user_roles = UserRoles.find_by_volunteer_id(volunteer_id)
    roles = []
    for role in user_roles:
        user_role = SiteRoles.find_by_id(role["role_id"])
        roles.append(user_role["title"])
    return roles


def set_user_roles_in_session(volunteer_id):
    session["roles"] = get_user_roles(volunteer_id)


def role_required(required_roles):
    def decorator(f):
        @wraps(f)
        def wrapped(*args, **kwargs):
            if not current_user.is_authenticated:
                flash("Please log in to access this page.", "warning")
                return redirect(url_for("login"))
            user_roles = session.get("roles", [])
            if not any(role in user_roles for role in required_roles):
                flash("You do not have permission to access this page.", "danger")
                return redirect(url_for("index"))
            return f(*args, **kwargs)
        return wrapped
    return decorator