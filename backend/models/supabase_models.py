from supabase import create_client
import os
from dotenv import load_dotenv

load_dotenv()
url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")
supabase = create_client(url, key)

def insert_user_plant(user_id, plant_data):
    payload = {
        "user_id": user_id,
        "plant_name": plant_data["plant_name"],
        "probability": plant_data["probability"],
        "image_url": plant_data["image_url"],
        "best_light": plant_data["best_light"],
        "best_soil": plant_data["best_soil"],
        "best_watering": plant_data["best_watering"]
    }

    response = supabase.table("user_plants").insert(payload).execute()
    return response.data
