import requests
from datetime import datetime
import pytz

# API sozlamalari
api_key = "075daacb9c3ab96d1800952d3388e9cd"
base_url = "https://api.openweathermap.org/data/2.5/forecast"

# Toshkent vaqti (UTC+5)
tz = pytz.timezone('Asia/Tashkent')

# Kunlar nomini olish uchun dictionary
days_map = {
    0: "Dushanba",
    1: "Seshanba",
    2: "Chorshanba",
    3: "Payshanba",
    4: "Juma",
    5: "Shanba",
    6: "Yakshanba",
}

# Ma'lumotlarni qaytarish uchun funksiya
def get_weather_forecast(city_name):
    # API so'rovi (6 kunlik prognoz uchun)
    forecast_url = f"{base_url}?q={city_name}&appid={api_key}&units=metric"
    forecast_response = requests.get(forecast_url)
    forecast_data = forecast_response.json()

    # Ob-havo ma'lumotlarini yig'ish
    weather_forecast = {}

    for forecast in forecast_data['list']:
        forecast_time = datetime.utcfromtimestamp(forecast['dt']).replace(tzinfo=pytz.utc).astimezone(tz)
        day = forecast_time.strftime("%Y-%m-%d")
        day_name = days_map[forecast_time.weekday()]

        if day not in weather_forecast:
            weather_forecast[day] = {
                "day_name": day_name,
                "date": forecast_time.strftime("%d %B"),
                "temp_min": forecast['main']['temp_min'],
                "temp_max": forecast['main']['temp_max'],
                "description": forecast['weather'][0]['description'],
                "rain_probability": forecast.get('pop', 0) * 100
            }
        else:
            weather_forecast[day]['temp_min'] = min(weather_forecast[day]['temp_min'], forecast['main']['temp_min'])
            weather_forecast[day]['temp_max'] = max(weather_forecast[day]['temp_max'], forecast['main']['temp_max'])

    # Natijani formatlash
    forecast_output = ""
    for i, (day, data) in enumerate(weather_forecast.items()):
        if i == 0:
            forecast_output += f"Bugun, {data['date']}\n"
        else:
            forecast_output += f"{data['day_name']}, {data['date']}\n"
        forecast_output += f"☀️ +{int(data['temp_max'])}°...+{int(data['temp_min'])}°, {data['description'].capitalize()}\n"
        forecast_output += f"Yog‘ingarchilik ehtimoli: {int(data['rain_probability'])}%\n\n"
    return forecast_output
