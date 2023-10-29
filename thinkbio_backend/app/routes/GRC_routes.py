# GRC_Route.py
from flask import Blueprint, jsonify

GRC_bp = Blueprint('GRC', __name__)

@GRC_bp.route("/GRC")
def GRC_test():
    return jsonify({"message": "GRC route is OK"})

@GRC_bp.route("/GRC/test")
def GRC_test_route():
    return jsonify({"message": "GRC test route is OK"})

