from flask import Blueprint, request, jsonify
from backend.services.plant_id_service import process_and_store_plant_data

plant_id_bp = Blueprint('plant_id', __name__)

@plant_id_bp.route('/plant_id_callback', methods=['POST'])
def plant_id_callback():
    data = request.get_json()
    user_id = data.get("user_id")  # You must send this from FlutterFlow
    response_data = data.get("api_response")

    if not user_id or not response_data:
        return jsonify({"error": "user_id and api_response are required"}), 400

    try:
        plant_record = process_and_store_plant_data(user_id, response_data)
        return jsonify({"message": "Plant data stored successfully", "plant": plant_record})
    except Exception as e:
        return jsonify({"error": str(e)}), 500