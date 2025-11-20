from flask import Flask, request
import requests
import os  # to load environment variables
from dotenv import load_dotenv

# Load variables from .env file
load_dotenv()

app = Flask(__name__)

# Get your Ultramsg credentials from environment variables
ULTRAMSG_INSTANCE = os.getenv("ULTRAMSG_INSTANCE")
ULTRAMSG_TOKEN = os.getenv("ULTRAMSG_TOKEN")

@app.route('/', methods=['POST'])
def webhook():
    message = request.json
    print("Message received:", message)

    # Extract sender and message text
    sender = message['data']['from']
    text = message['data']['body']

    # Prepare reply text
    reply_text = f"Hello! I received your message: {text}"

    # Ultramsg API URL
    url = f"https://api.ultramsg.com/{ULTRAMSG_INSTANCE}/messages/chat"

    # Payload formatted like Ultramsg docs
    payload = f"token={ULTRAMSG_TOKEN}&to={sender}&body={reply_text}"
    payload = payload.encode('utf8').decode('iso-8859-1')

    headers = {'content-type': 'application/x-www-form-urlencoded'}

    # Send reply
    response = requests.post(url, data=payload, headers=headers)
    print("Reply sent:", response.text)

    return "OK", 200

if __name__ == '__main__':
    app.run(port=3000)
