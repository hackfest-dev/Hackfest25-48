from flask import Blueprint, request, jsonify
from backend.services.plant_service import get_all_plants

plant_bp = Blueprint('plant', __name__)

@plant_bp.route('/get_plants', methods=['GET'])
def get_plants():
    """
    Fetch all plants for a specific user and return their names and image URLs.
    """
    user_id = request.args.get('user_id')

    if not user_id:
        return jsonify({"error": "user_id is required."}), 400

    try:
        plants = get_all_plants(user_id)
        return jsonify({
            "message": "Plants fetched successfully.",
            "plants": plants
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500
