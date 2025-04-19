from flask import Blueprint, request, jsonify
from backend.services.healthLog_service import log_health_issues

health_log_bp = Blueprint('health_log_bp', __name__)

@health_log_bp.route('/log_health', methods=['POST'])
def log_health():
    try:
        data = request.get_json()
        result = log_health_issues(data)
        return jsonify({"status": "success", "message": result}), 201
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500
