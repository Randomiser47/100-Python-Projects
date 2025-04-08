import requests
import os
import tkinter as tk
from tkinter import simpledialog
from datetime import datetime

# ---------------------------- NLP-POWERED WORKOUT TRACKER ------------------------------- #
def get_exercise_description():
    root = tk.Tk()
    root.withdraw()  # Hide main window
    
    # Create custom dialog with better prompting
    user_input = simpledialog.askstring(
        "Workout Tracker 🤖",
        "What did you do today?\nExamples:\n- 'Ran 5k in 30 minutes'\n- 'Swam 20 laps'\n- '45 minute weight training session'",
        parent=root
    )
    root.destroy()
    return user_input

# ---------------------------- API CONFIGURATION ------------------------------- #
# Environment variables for security
NUTRITIONIX_APP_ID = os.environ.get("x_app_id")
NUTRITIONIX_API_KEY = os.environ.get("x_app_key")
NUTRITIONIX_ENDPOINT = os.environ.get("nuti_url")
SHEETY_ENDPOINT = os.environ.get("Sheety_url")

headers = {
    'x-app-id': NUTRITIONIX_APP_ID,
    'x-app-key': NUTRITIONIX_API_KEY,
}

# ---------------------------- NLP PROCESSING ------------------------------- #
# Get natural language input through GUI
exercise_query = get_exercise_description()

if exercise_query:  # Only proceed if user provided input
    # Nutritionix's NLP parses natural language into structured data
    nutritionix_params = {
        'gender': 'male',
        'weight_kg': 85,
        'height_cm': 180.33,
        'age': 25,
        'query': exercise_query
    }

    # Get exercise data from Nutritionix API
    response = requests.post(
        url=NUTRITIONIX_ENDPOINT,
        json=nutritionix_params,
        headers=headers
    )
    exercise_data = response.json()

    # ---------------------------- DATA LOGGING ------------------------------- #
    # Prepare timestamp
    today = datetime.now()
    
    # Log to Google Sheets via Sheety
    for exercise in exercise_data['exercises']:
        log_entry = {
            "sheet1": {
                "date": today.strftime("%Y/%m/%d"),
                "time": today.strftime("%H:%M:%S"),
                "exercise": exercise['name'],
                "duration": exercise['duration_min'],
                "calories": exercise['nf_calories']
            }
        }
        
        response = requests.post(
            url=SHEETY_ENDPOINT,
            json=log_entry,
            headers={'Content-Type': 'application/json'},
            auth=('iron_man', 'ironman422')
        )