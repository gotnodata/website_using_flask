# Where we define the main blueprint routes.
from flask import Blueprint, render_template
from models import users

main_bp = Blueprint('main', __name__)

@main_bp.route("/")
def home():
    return render_template("index.html")

@main_bp.route("/view")
def view():
    return render_template("view.html", values=users.query.all())