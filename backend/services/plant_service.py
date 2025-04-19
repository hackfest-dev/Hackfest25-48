from supabase import create_client
import os
from dotenv import load_dotenv

load_dotenv()
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")
supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

def get_all_plants(user_id):
    """
    Fetch all plants for a specific user and return only the plant name and image URL.
    """
    response = supabase.table("user_plants") \
        .select("plant_name, image_url") \
        .eq("user_id", user_id) \
        .execute()

    if response.error:
        raise Exception(response.error.message)

    return response.data
