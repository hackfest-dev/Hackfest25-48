import uuid
from datetime import datetime
from supabase import create_client
import os
from dotenv import load_dotenv

load_dotenv()
url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")
supabase = create_client(url, key)

def log_health_issues(data):
    user_id = data.get("user_id")
    plant_id = data.get("plant_id")
    analysis = data.get("result", {}).get("disease", {}).get("suggestions", [])

    if not user_id or not plant_id or not analysis:
        raise ValueError("Missing required fields: user_id, plant_id or disease suggestions")

    logs_to_insert = []

    for issue in analysis:
        log_entry = {
            "id": str(uuid.uuid4()),
            "plant_id": plant_id,
            "user_id": user_id,
            "disease_name": issue.get("name"),
            "description": issue.get("details", {}).get("description"),
            "treatment_info": issue.get("details", {}).get("treatment"),
            "detected_at": datetime.utcnow().isoformat(),
            "disease_data": issue  # raw data if needed for deep analysis
        }
        logs_to_insert.append(log_entry)

    response = supabase.table("health_log").insert(logs_to_insert).execute()

    if response.get("error"):
        raise Exception(response["error"]["message"])
    return f"{len(logs_to_insert)} health issues logged."