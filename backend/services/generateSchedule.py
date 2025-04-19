import datetime
import os
from dotenv import load_dotenv
from supabase import create_client, Client

# Keyword maps for care suggestions
light_keywords = {
    "full sun": "6-8 hrs direct sunlight",
    "partial shade": "3-6 hrs indirect sunlight",
    "indirect light": "bright but indirect light",
    "low light": "minimal natural light"
}

soil_keywords = {
    "well-draining": "Use potting mix with perlite or sand",
    "loamy": "Use loamy soil (mix of sand, silt, and clay)",
    "acidic": "Check pH, aim for 5.5–6.5",
    "moist but not soggy": "Ensure good drainage, water moderately"
}

watering_keywords = {
    "keep soil moist": "Water every 2-3 days",
    "allow soil to dry": "Water once a week or when topsoil is dry",
    "frequent watering": "Water daily or when dry",
    "low water needs": "Water sparingly, once every 10 days"
}

def match_keywords(text, keyword_map):
    if not text:
        return None
    text = text.lower()
    for key_phrase, suggestion in keyword_map.items():
        if key_phrase in text:
            return suggestion
    return None


def generate_smart_care_schedule(plant_data, disease_data, weather_data, growth_metrics):
    priorities = {
        "disease": 0.4,
        "growth": 0.3,
        "weather": 0.2,
        "soil_light": 0.1
    }

    today = datetime.date.today()
    schedule = []

    # Disease Treatment
    disease_suggestions = disease_data.get("disease", [])
    high_confidence_diseases = [
        {
            "task": f"Treat disease: {d['name']}",
            "reason": f"High probability ({d['probability']:.0%}), apply {d['treatment']}.",
            "notification_time": "08:00 AM"
        }
        for d in disease_suggestions if d["probability"] > 0.8
    ]

    # Growth Metrics Suggestions
    growth_score = growth_metrics.get("score", 1.0)
    previous_score = growth_metrics.get("previous_score", growth_score)
    delta = growth_score - previous_score
    growth_suggestions = []

    if delta < -0.1:
        growth_suggestions.append({
            "task": "Check for stress",
            "reason": "Growth score dropped. Consider repotting or adjusting care.",
            "notification_time": "09:00 AM"
        })
    elif growth_score < 0.5:
        growth_suggestions.append({
            "task": "Increase watering/fertilizer",
            "reason": "Growth is slow.",
            "notification_time": "09:00 AM"
        })
    elif growth_score > 0.8:
        growth_suggestions.append({
            "task": "Monitor watering",
            "reason": "Excellent growth. Ensure not overwatering.",
            "notification_time": "09:00 AM"
        })

    # Keyword-based Soil/Light/Watering Suggestions
    light_suggestion = match_keywords(plant_data.get("best_light_condition", ""), light_keywords)
    soil_suggestion = match_keywords(plant_data.get("best_soil_type", ""), soil_keywords)
    watering_suggestion = match_keywords(plant_data.get("best_watering", ""), watering_keywords)

    soil_light_suggestions = []
    if light_suggestion:
        soil_light_suggestions.append({
            "task": "Adjust lighting",
            "reason": light_suggestion,
            "notification_time": "10:00 AM"
        })
    if soil_suggestion:
        soil_light_suggestions.append({
            "task": "Check soil",
            "reason": soil_suggestion,
            "notification_time": "10:00 AM"
        })
    if watering_suggestion:
        soil_light_suggestions.append({
            "task": "Watering advice",
            "reason": watering_suggestion,
            "notification_time": "10:00 AM"
        })

    # Process 7-day weather data
    weather_suggestions = []
    for day in weather_data:
        temp = day.get("temp", {}).get("day", 25)  # Use daytime temperature
        if temp > 30:
            weather_suggestions.append({
                "task": "Increase watering",
                "reason": "High temperature forecasted.",
                "notification_time": "08:00 AM"
            })
        elif temp < 10:
            weather_suggestions.append({
                "task": "Protect from cold",
                "reason": "Low temperature forecasted.",
                "notification_time": "08:00 AM"
            })

    # Build 7-day schedule
    for i in range(7):
        date_obj = today + datetime.timedelta(days=i)
        date_key = str(date_obj)
        day_name = date_obj.strftime("%A")

        day_tasks = []

        # Disease on Day 1
        if high_confidence_diseases and i == 0:
            for task in high_confidence_diseases:
                task.update({"date": date_key, "day": day_name})
                day_tasks.append(task)

        # Weather suggestions for the day
        if i < len(weather_suggestions):
            weather_task = weather_suggestions[i]
            weather_task.update({"date": date_key, "day": day_name})
            day_tasks.append(weather_task)

        # Growth suggestions on Day 2
        if i == 1:
            for task in growth_suggestions:
                task.update({"date": date_key, "day": day_name})
                day_tasks.append(task)

        # Soil/light suggestions on Day 6
        if i == 5:
            for task in soil_light_suggestions:
                task.update({"date": date_key, "day": day_name})
                day_tasks.append(task)

        # Placeholder if no task
        if not day_tasks:
            schedule.append({
                "date": date_key,
                "day": day_name,
                "task": "",
                "reason": "",
                "notification_time": ""
            })
        else:
            schedule.extend(day_tasks)

    return schedule

def auto_generate_if_inactive():
    
    load_dotenv()
    url = os.getenv("SUPABASE_URL")
    key = os.getenv("SUPABASE_KEY")
    supabase: Client = create_client(url, key)

    today = datetime.date.today()
    plants = supabase.table("user_plants").select("*").execute().data
    plants = supabase.table("user_plants").select("*").execute().data

    for plant in plants:
        last_analysis = supabase.table("growth_analysis").select("analyzed_at").eq("plant_id", plant["id"]).order("analyzed_at", desc=True).limit(1).execute().data

        if last_analysis:
            last_date = datetime.fromisoformat(last_analysis[0]["analyzed_at"])
            if (today - last_date).days > 7:
                generate_smart_care_schedule(plant["user_id"], plant["id"], {}, {}, None)