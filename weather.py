import requests
from datetime import datetime
import pytz

# API settings
api_key = "075daacb9c3ab96d1800952d3388e9cd"
current_weather_url = "https://api.openweathermap.org/data/2.5/weather"
forecast_url = "https://api.openweathermap.org/data/2.5/forecast"

def get_weather(city_name):
    # API request (current weather)
    current_url = f"{current_weather_url}?q={city_name}&appid={api_key}&units=metric"
    current_response = requests.get(current_url)
    current_weather = current_response.json()

    # API request (forecast)
    forecast_response = requests.get(f"{forecast_url}?q={city_name}&appid={api_key}&units=metric")
    forecast_data = forecast_response.json()

    # Current date and time
    today_date = datetime.now()
    tz = pytz.timezone('Asia/Tashkent')

    # Current weather data
    current_temp = current_weather['main']['temp']
    humidity = current_weather['main']['humidity']
    pressure = current_weather['main']['pressure'] * 0.75006  # hPa to mm Hg
    wind_speed = current_weather['wind']['speed']
    wind_dir = current_weather['wind']['deg']

    # Sunrise and sunset times
    sunrise_utc = datetime.utcfromtimestamp(current_weather['sys']['sunrise'])
    sunset_utc = datetime.utcfromtimestamp(current_weather['sys']['sunset'])
    sunrise = sunrise_utc.replace(tzinfo=pytz.utc).astimezone(tz).strftime('%H:%M')
    sunset = sunset_utc.replace(tzinfo=pytz.utc).astimezone(tz).strftime('%H:%M')

    # Wind direction
    def get_wind_direction(degree):
        directions = ['Shimoliy', 'Shimoliy-Sharqiy', 'Sharqiy', 'Janubiy-Sharqiy', 'Janubiy', 'Janubiy-G’arbi', 'G’arbiy', 'Shimoliy-G’arbi']
        idx = round(degree / 45) % 8
        return directions[idx]

    wind_direction = get_wind_direction(wind_dir)

    # Daily forecast
    day_forecast = {"Tong": None, "Kun": None, "Oqshom": None}

    for forecast in forecast_data['list']:
        forecast_time = datetime.utcfromtimestamp(forecast['dt']).replace(tzinfo=pytz.utc).astimezone(tz)
        forecast_date = forecast_time.strftime('%Y-%m-%d')

        if forecast_date == today_date.strftime('%Y-%m-%d'):
            hour = forecast_time.hour
            temp = forecast['main']['temp']
            
            if 6 <= hour < 12:
                day_forecast["Tong"] = f"☀️ +{int(temp)}°"
            elif 12 <= hour < 18:
                day_forecast["Kun"] = f"☀️ +{int(temp)}°"
            elif 18 <= hour < 24:
                day_forecast["Oqshom"] = f"☁️ +{int(temp)}°"

    # If no forecast found, use current temperature
    if not day_forecast["Tong"]:
        day_forecast["Tong"] = f"☀️ +{int(current_temp)}°"
    if not day_forecast["Kun"]:
        day_forecast["Kun"] = f"☀️ +{int(current_temp)}°"
    if not day_forecast["Oqshom"]:
        day_forecast["Oqshom"] = f"☁️ +{int(current_temp)}°"

    # Moon phase (placeholder)
    def get_moon_phase(date):
        return "Yosh oy"

    moon_phase = get_moon_phase(today_date)

    return {
        "date": today_date.strftime("%d Avgust"),
        "current_temp": int(current_temp),
        "humidity": humidity,
        "pressure": int(pressure),
        "wind_speed": wind_speed,
        "wind_direction": wind_direction,
        "sunrise": sunrise,
        "sunset": sunset,
        "moon_phase": moon_phase,
        "day_forecast": day_forecast
}