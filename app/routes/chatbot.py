from flask import Blueprint, render_template

bp = Blueprint("chatbot", __name__, url_prefix="/chatbot")

@bp.route("/")
def chatbot_page():
    return "<h1>Chatbot Page (coming soon)</h1>"
