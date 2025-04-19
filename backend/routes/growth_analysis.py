from flask import Blueprint, request, jsonify
from backend.core.growth_tracking import compare_and_score_growth
from supabase import create_client
import os
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")
supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

# Create a Blueprint for growth analysis routes
growth_analysis_bp = Blueprint('growth_analysis', __name__)

@growth_analysis_bp.route('/analyze_growth', methods=['POST'])
def analyze_growth():
    """
    Analyze growth metrics for a plant based on the latest two images.
    """
    data = request.json
    user_id = data.get('user_id')
    plant_id = data.get('plant_id')

    if not user_id or not plant_id:
        return jsonify({"error": "user_id and plant_id are required."}), 400

    try:
        # Fetch latest 2 image entries for this plant
        response = supabase.table("plant_images") \
            .select("image_url, timestamp") \
            .eq("user_id", user_id) \
            .eq("plant_id", plant_id) \
            .order("timestamp", desc=True) \
            .limit(2) \
            .execute()

        image_data = response.data

        if len(image_data) < 2:
            return jsonify({"error": "Not enough images to compare."}), 400

        url1 = image_data[1]["image_url"]  # older
        url2 = image_data[0]["image_url"]  # latest

        timestamp1 = datetime.fromisoformat(image_data[1]["timestamp"])
        timestamp2 = datetime.fromisoformat(image_data[0]["timestamp"])
        time_diff_days = (timestamp2 - timestamp1).days

        # Compare growth metrics
        growth_score, delta_metrics = compare_and_score_growth(url2, url1, species=data.get("species", "generic"))

        # Prepare data to insert into Supabase
        result_payload = {
            "user_id": user_id,
            "plant_id": plant_id,
            "growth_score": growth_score,
            "delta_metrics": delta_metrics,
            "time_difference_days": time_diff_days,
            "analyzed_at": datetime.utcnow().isoformat()
        }

        # Insert result into a 'growth_analysis' table
        supabase.table("growth_analysis").insert(result_payload).execute()

        return jsonify({
            "message": "Growth analysis completed and stored successfully.",
            **result_payload
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500

@growth_analysis_bp.route('/get_growth_history', methods=['GET'])
def get_growth_history():
    """
    Fetch growth history for a specific plant to plot a line chart and display past images.
    """
    user_id = request.args.get('user_id')
    plant_id = request.args.get('plant_id')

    if not user_id or not plant_id:
        return jsonify({"error": "user_id and plant_id are required."}), 400

    try:
        # Fetch growth history from the 'growth_analysis' table
        response = supabase.table("growth_analysis") \
            .select("growth_score, time_difference_days, analyzed_at, plant_id") \
            .eq("user_id", user_id) \
            .eq("plant_id", plant_id) \
            .order("analyzed_at", asc=True) \
            .execute()

        growth_history = response.data

        if not growth_history:
            return jsonify({"error": "No growth history found for the specified plant."}), 404

        # Fetch image URLs from the 'plant_images' table
        image_response = supabase.table("plant_images") \
            .select("image_url, timestamp") \
            .eq("user_id", user_id) \
            .eq("plant_id", plant_id) \
            .order("timestamp", asc=True) \
            .execute()

        image_data = image_response.data

        # Combine growth history with image URLs
        for record in growth_history:
            matching_image = next((img for img in image_data if img["timestamp"] == record["analyzed_at"]), None)
            record["image_url"] = matching_image["image_url"] if matching_image else None

        return jsonify({
            "message": "Growth history fetched successfully.",
            "growth_history": growth_history
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500