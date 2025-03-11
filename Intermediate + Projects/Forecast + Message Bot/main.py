import requests
import json

# TELEGRAM
open_weather_url = 'User your own'
bot_token = 'User your own'
chat_id = 'User your own'
open_weather_api= 'User your own'

parameters = {
    'lat': 'User your own',
    'lon':'User your own',
    'appid':open_weather_api,
    'cnt':4
}

response = requests.get(url= open_weather_url,params=parameters)
response.raise_for_status()
data = response.json()

will_rain = False
weather_id = []
for hour_data in data['list']:
   condition_code =hour_data['weather'][0]['id']
   if condition_code < 700:
      will_rain  = True

if will_rain == True:
    text =  'bring umbrella'
else:
    text = "I don't think an umbrella is necessary today"

send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + chat_id + '&parse_mode=Markdown&text=' + text
telegram_response = requests.get(url=send_text)

