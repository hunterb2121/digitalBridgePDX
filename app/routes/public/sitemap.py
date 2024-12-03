from flask import Response, url_for
from . import sitemap_bp


@sitemap_bp.route("/sitemap.xml", methods=["GET"])
def sitemap():
    urls = [
        {"loc": url_for("public.index", _external=True), "lastmod": "2024-12-01"},
        {"loc": url_for("public.about", _external=True), "lastmod": "2024-12-01"},
        {"loc": url_for("public.contact", _external=True), "lastmod": "2024-12-01"},
        {"loc": url_for("public.classes", _external=True), "lastmod": "2024-12-01"},
        {"loc": url_for("public.resources", _external=True), "lastmod": "2024-12-01"},
        {"loc": url_for("public.tech_support", _external=True), "lastmod": "2024-12-01"},
        {"loc": url_for("public.get_involved", _external=True), "lastmod": "2024-12-01"},
        {"loc": url_for("public.aid_fund_donations", _external=True), "lastmod": "2024-12-01"}
    ]

    xml = '<?xml version="1.0" encoding="UTF-8"?>\n'
    xml += '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'

    for url in urls:
        xml += "    <url>\n"
        xml += f"       <loc>{url['loc']}</loc>\n"
        xml += f"       <lastmod>{url['lastmod']}</lastmod>\n"
        xml += "    </url>\n"

    xml += "</urlset>\n"

    return Response(xml, mimetype="application/xml")