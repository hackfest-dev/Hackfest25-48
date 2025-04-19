from backend.models.supabase_models import insert_user_plant

def extract_plant_data(response_data):
    """Extract relevant fields from the Plant ID API response."""
    try:
        suggestions = response_data["result"]["classification"]["suggestions"]
        if not suggestions:
            raise ValueError("No plant suggestions found.")
        
        best = suggestions[0]
        details = best.get("details", {})

        #Use common name if available, else fallback to scientific name
        common_name = details.get("common_names", [None])[0] or best.get("name")

        #Get original uploaded image URL
        input_image_url = response_data.get("input", {}).get("images", [None])[0] or ""

        #Get other plant info
        best_light = details.get("best_light_condition", "Unknown")
        best_soil = details.get("best_soil_type", "Unknown")
        best_watering = details.get("best_watering", "Moderate")

        return {
            "plant_name": common_name,
            "image_url": input_image_url,
            "light": best_light,
            "soil": best_soil,
            "water": best_watering
        }

    except Exception as e:
        raise ValueError(f"Error parsing Plant ID response: {str(e)}")


def process_and_store_plant_data(user_id, response_data):
    plant_data = extract_plant_data(response_data)
    return insert_user_plant(user_id, plant_data)