from datetime import datetime
from supabase import create_client
import os
from dotenv import load_dotenv
from backend.core.growth_tracking import compare_and_score_growth

load_dotenv()
url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")
supabase = create_client(url, key)


def analyze_growth_for_plant(plant_id, user_id, new_img_url, species):
    """
    Step-by-step:
    1. Insert the new image entry into growth_analysis with timestamp only.
    2. Fetch last 2 images for the plant (ordered by timestamp).
    3. Compare metrics and compute growth score.
    4. Update the latest row with score, deltas, time_diff.
    5. Return score and metrics.
    """
    # Step 1: Insert new entry (score & metrics will be added later)
    insert_response = supabase.table("growth_analysis").insert({
        "plant_id": plant_id,
        "user_id": user_id,
        "analyzed_at": datetime.now()
    }).execute()
    new_entry_id = insert_response.data[0]["id"]

    # Step 2: Fetch last 2 image entries (most recent first)
    entries = supabase.table("growth_analysis") \
        .select("id, analyzed_at") \
        .eq("plant_id", plant_id) \
        .order("analyzed_at", desc=True) \
        .limit(2) \
        .execute().data

    if len(entries) < 2:
        print("Need at least two images to compare growth.")
        return None

    current_id, previous_id = entries[0]["id"], entries[1]["id"]
    analyzed_at_current = datetime.fromisoformat(entries[0]["analyzed_at"])
    analyzed_at_previous = datetime.fromisoformat(entries[1]["analyzed_at"])
    time_diff_days = (analyzed_at_current - analyzed_at_previous).days

    # Step 3: Fetch previous image URL from `user_plants`
    previous_image_url = supabase.table("user_plants") \
        .select("image_url") \
        .eq("id", plant_id) \
        .execute().data[0]["image_url"]

    # Step 4: Compute score and deltas
    score, deltas = compare_and_score_growth(
        current_img_url=new_img_url,
        previous_img_url=previous_image_url,
        species=species
    )

    # Step 5: Update current row with calculated metrics
    supabase.table("growth_analysis").update({
        "growth_score": score,
        "delta_metrics": deltas,
        "time_difference_days": time_diff_days
    }).eq("id", current_id).execute()


def get_growth_history(plant_id):
    """
    Get all growth scores and timestamps for the plant to plot line chart.
    """
    response = supabase.table("growth_analysis") \
        .select("growth_score, analyzed_at") \
        .eq("plant_id", plant_id) \
        .order("analyzed_at", desc=True) \
        .execute()

    history = [{
        "timestamp": row["analyzed_at"],
        "growth_score": row["growth_score"]
    } for row in response.data if row["growth_score"] is not None]

    return history
