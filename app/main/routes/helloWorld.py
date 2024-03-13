from flask import Blueprint, render_template

bp = Blueprint("static", __name__)

@bp.route("/")
def home():
    return render_template("home.html", title="Hello World", image_url="assets/quesito.jpeg")

"""
@bp.route("/about")
def about():
    return "Hello, About!"
"""
