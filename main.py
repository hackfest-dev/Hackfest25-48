from flask import Flask, request, jsonify
from supabase import create_client, Client
from backend.routes.growth_analysis import growth_analysis_bp
from backend.routes.plant_id import plant_id_bp
from backend.routes.healthLogs import health_log_bp
from backend.routes.care_schedule import care_schedule_bp
from backend.routes.notification import notification_bp
from backend.routes.plant import plant_bp  # Import the new plant blueprint
import os
from datetime import datetime
from dotenv import load_dotenv

app = Flask(__name__)

load_dotenv()
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

app.register_blueprint(growth_analysis_bp, url_prefix='/api')
app.register_blueprint(plant_id_bp, url_prefix='/api')
app.register_blueprint(health_log_bp, url_prefix='/api')
app.register_blueprint(care_schedule_bp, url_prefix='/api')
app.register_blueprint(notification_bp, url_prefix='/api')
app.register_blueprint(plant_bp, url_prefix='/api')

if __name__ == '__main__':
    app.run(debug=True)