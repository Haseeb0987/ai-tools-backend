from flask import Blueprint, request, jsonify
from app.helpers.ai_utils import summarize_code, explain_code

ai_bp = Blueprint('ai_routes', __name__)

@ai_bp.route("/summarize", methods=["POST"])
def summarize():
    code = request.json.get("code", "")
    summary = summarize_code(code)
    return jsonify({"summary": summary})

@ai_bp.route("/explain", methods=["POST"])
def explain():
    code = request.json.get("code", "")
    explanation = explain_code(code)
    return jsonify({"explanation": explanation})

@ai_bp.route("/test", methods=["GET"])
def test():
    return jsonify({"message": "AI routes are working!"})
