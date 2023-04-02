import os
import requests
import twilio_api as t


api_endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = os.getenv("API_KEY")

params = {
    "lat": -22.54889467287643,
    "lon": -44.126534016179875,
    "appid": api_key,
    "units": "metric",
    "cnt": 5,
    "lang": "pt-br"
}
response = requests.get(api_endpoint, params=params)
response.raise_for_status()

weather_data = response.json()["list"]
print(weather_data)

for weather in weather_data:
    weather_code = int(weather["weather"][0]["id"])
    print(weather_code)
    if 500 <= weather_code < 600:
        t.send_sms()
        break
