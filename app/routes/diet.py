from flask import Blueprint, render_template

bp = Blueprint("diet", __name__, url_prefix="/diet")

@bp.route("/")
def diet_page():
    return "<h1>Diet Page (coming soon)</h1>"