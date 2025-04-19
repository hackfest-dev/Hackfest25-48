from flask import Blueprint, request, jsonify
from backend.services.notification_service import get_notifications_for_today, get_user_details

notification_bp = Blueprint('notification', __name__)

@notification_bp.route('/get_notifications', methods=['GET'])
def get_notifications():
    """
    Fetch all notifications for the current day for a specific user by matching with care_schedule.
    """
    user_id = request.args.get('user_id')

    if not user_id:
        return jsonify({"error": "user_id is required."}), 400

    try:
        notifications = get_notifications_for_today(user_id)
        return jsonify({
            "message": "Notifications fetched successfully.",
            "notifications": notifications
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@notification_bp.route('/get_user_details', methods=['GET'])
def get_user_details_route():
    """
    Fetch user details (name and email) for a specific user.
    """
    user_id = request.args.get('user_id')

    if not user_id:
        return jsonify({"error": "user_id is required."}), 400

    try:
        user_details = get_user_details(user_id)
        return jsonify({
            "message": "User details fetched successfully.",
            "user_details": user_details
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500
