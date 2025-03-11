# Weather Alert Bot

## Overview

This script fetches weather data from an API and sends an alert via Telegram if it detects rain.

## Features

- Uses OpenWeather API to fetch weather data.
- Checks for rain conditions based on weather codes.
- Sends a Telegram message when rain is detected.

## Requirements

- Python 3
- `requests` library
- Telegram bot and chat ID
- OpenWeather API key

## Setup

1. **Install dependencies**

   ```bash
   pip install requests
   ```

2. **Obtain API keys**

   - Get an OpenWeather API key from [OpenWeather](https://openweathermap.org/api)
   - Create a Telegram bot and get the bot token from [BotFather](https://t.me/BotFather)
   - Get your chat ID using the Telegram bot API

3. **Configure the script**
   Replace placeholders in the script with your own:

   ```python
   open_weather_url = 'Your OpenWeather API endpoint'
   bot_token = 'Your Telegram bot token'
   chat_id = 'Your Telegram chat ID'
   open_weather_api = 'Your OpenWeather API key'
   ```

4. **Run the script**

   ```bash
   python main.py
   ```

## How It Works

- The script sends a request to OpenWeather API with location and API key.
- It parses the JSON response and checks if any of the next few hours have weather conditions indicating rain (`id < 700`).
- If rain is detected, it sends a message via Telegram: **"Bring an umbrella"**.
- Otherwise, it sends **"I don't think an umbrella is necessary today."**

## Notes

- Ensure that your Telegram bot has permission to send messages to your chat ID.
- Modify the `cnt` parameter in API request to change the number of forecast hours checked.
- Use PythonAnywhere to schedule and run this on a specific time.&#x20;
