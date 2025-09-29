from flask import Blueprint, render_template

bp = Blueprint("auth", __name__, url_prefix="/auth")

@bp.route("/login")
def login():
    return "<h1>Login Page (coming soon)</h1>"

@bp.route("/register")
def register():
    return "<h1>Register Page (coming soon)</h1>"
