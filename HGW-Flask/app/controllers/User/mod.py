from flask import Blueprint, jsonify, render_template

mod_bp = Blueprint('mod', __name__)

@mod_bp.route("/api/moderador", methods=["GET"])
def dashboard():
    return "Moderador"

@mod_bp.route("/", methods=["GET"])
def index():

    return render_template("index.html")