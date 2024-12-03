from flask import Blueprint

public_bp = Blueprint("public", __name__, template_folder="../../templates/public")
sitemap_bp = Blueprint("sitemap", __name__)

from . import about, aid_fund_donations, classes, contact, get_involved, index, resources, tech_support, sitemap, robots