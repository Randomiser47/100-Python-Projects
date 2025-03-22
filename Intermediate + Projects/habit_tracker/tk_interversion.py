import requests
from datetime import datetime
import tkinter as tk
import os

# Load USERNAME and TOKEN from environment variables (you can set them in your environment or .env file)
USERNAME = os.getenv("PIXELA_USERNAME", "your_username")
TOKEN = os.getenv("PIXELA_TOKEN", "your_token")
GRAPH_ID = "graph1"
PIXELA_ENDPOINT = f"https://pixe.la/v1/users/{USERNAME}/graphs/{GRAPH_ID}"

HEADERS = {
    "X-USER-TOKEN": TOKEN,
}

def update_hours():
    hours = entry.get()
    today = datetime.now().strftime('%Y%m%d')
    value_parameters = {
        'date': today,
        'quantity': hours,
    }
    response = requests.post(url=PIXELA_ENDPOINT, json=value_parameters, headers=HEADERS)
    if response.status_code == 200:
        status_label.config(text="Updated successfully!", fg="green")
    else:
        status_label.config(text="Failed to update!", fg="red")

# Tkinter GUI
root = tk.Tk()
root.title("Python Progress Tracker")
root.geometry("300x150")

tk.Label(root, text="Enter Hours:").pack(pady=10)
entry = tk.Entry(root)
entry.pack(pady=5)

submit_btn = tk.Button(root, text="Submit", command=update_hours)
submit_btn.pack(pady=5)

status_label = tk.Label(root, text="")
status_label.pack(pady=5)

root.mainloop()
