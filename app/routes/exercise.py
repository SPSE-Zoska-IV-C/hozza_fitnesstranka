from flask import Blueprint, render_template

bp = Blueprint("exercise", __name__, url_prefix="/exercise")

@bp.route("/")
def exercise_page():
    return "<h1>Exercise Page (coming soon)</h1>"