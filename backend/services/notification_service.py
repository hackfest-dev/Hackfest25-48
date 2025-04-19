from supabase import create_client
import os
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")
supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

def get_notifications_for_today(user_id):
    """
    Fetch all notifications for the current day for a specific user by matching with care_schedule.
    """
    today = datetime.now(datetime.timezone.utc).date()

    # Fetch care schedule entries for today
    care_schedule_response = supabase.table("care_schedule") \
        .select("notification_id, task, reason") \
        .eq("user_id", user_id) \
        .eq("date", today.isoformat()) \
        .execute()

    if care_schedule_response.error:
        raise Exception(care_schedule_response.error.message)

    care_schedule_data = care_schedule_response.data

    # Extract notification IDs from care schedule
    notification_ids = [entry["notification_id"] for entry in care_schedule_data if entry["notification_id"]]

    if not notification_ids:
        return []

    # Fetch notifications matching the IDs
    notification_response = supabase.table("notification") \
        .select("id, time, notification_text") \
        .in_("id", notification_ids) \
        .execute()

    if notification_response.error:
        raise Exception(notification_response.error.message)

    notifications = notification_response.data

    # Combine notifications with care schedule tasks
    for notification in notifications:
        matching_schedule = next((entry for entry in care_schedule_data if entry["notification_id"] == notification["id"]), {})
        notification["task"] = matching_schedule.get("task")
        notification["reason"] = matching_schedule.get("reason")

    return notifications

def get_user_details(user_id):
    """
    Fetch user details (name and email) from the database.
    """
    response = supabase.table("auth.users") \
        .select("name, email") \
        .eq("id", user_id) \
        .execute()

    if response.error:
        raise Exception(response.error.message)

    if not response.data:
        raise Exception("User not found.")

    return response.data[0]
