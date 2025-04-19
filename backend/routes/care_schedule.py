from flask import Blueprint, request, jsonify
from supabase import create_client
import os
from backend.services.generateSchedule import generate_smart_care_schedule
from datetime import datetime

# Load Supabase credentials
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")
supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

# Create a Blueprint for care schedule routes
care_schedule_bp = Blueprint('care_schedule', __name__)

@care_schedule_bp.route('/generate_schedule', methods=['POST'])
def generate_schedule():
    """
    Generate a care schedule for a specific plant.
    """
    data = request.json
    user_id = data.get('user_id')
    plant_id = data.get('plant_id')
    weather_api_response = data.get('weather_api_response')  # Accept raw weather API response

    if not user_id or not plant_id or not weather_api_response:
        return jsonify({"error": "user_id, plant_id, and weather_api_response are required."}), 400

    try:
        # Parse weather data and convert temperatures from Kelvin to Celsius
        weather_data = []
        for day in weather_api_response.get('daily', []):
            day_temp_kelvin = day.get('temp', {}).get('day')
            if day_temp_kelvin is not None:
                day_temp_celsius = day_temp_kelvin - 273.15  # Convert Kelvin to Celsius
                weather_data.append({
                    "date": datetime.fromtimestamp(datetime.timezone.utc)(day.get('dt')).strftime('%Y-%m-%d'),
                    "temp": round(day_temp_celsius, 2)  # Round to 2 decimal places
                })

        if not weather_data:
            return jsonify({"error": "Invalid weather data."}), 400

        # Fetch plant data
        plant_response = supabase.table("user_plants") \
            .select("best_light, best_soil, best_watering") \
            .eq("user_id", user_id) \
            .eq("id", plant_id) \
            .execute()
        plant_data = plant_response.data[0] if plant_response.data else None

        if not plant_data:
            return jsonify({"error": "Plant data not found."}), 404

        # Fetch disease data
        disease_response = supabase.table("health_log") \
            .select("disease_name, treatment_info") \
            .eq("user_id", user_id) \
            .eq("plant_id", plant_id) \
            .order("detected_at", desc=True) \
            .limit(1) \
            .execute()
        disease_data = {"disease": disease_response.data} if disease_response.data else {}

        # Fetch growth metrics
        growth_response = supabase.table("growth_analysis") \
            .select("growth_score, delta_metrics") \
            .eq("user_id", user_id) \
            .eq("plant_id", plant_id) \
            .order("analyzed_at", desc=True) \
            .limit(1) \
            .execute()
        growth_metrics = growth_response.data[0] if growth_response.data else {}

        # Generate the care schedule
        schedule = generate_smart_care_schedule(plant_data, disease_data, weather_data, growth_metrics)

        return jsonify({
            "message": "Care schedule generated successfully.",
            "schedule": schedule
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500
