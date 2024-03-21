import requests

def get_current_weather(latitude, longitude):
    url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m,wind_direction_10m"
    response = requests.get(url)
    data = response.json()
    return data

def print_current_temperature_and_wind_direction(data):
    temperature = data['current']['temperature_2m']
    wind_direction = data['current']['wind_direction_10m']
    print(f"Current Temperature: {temperature}°C")
    print(f"Current Wind Direction: {wind_direction}°")

def main():
    # Replace latitude and longitude with your desired location
    latitude = 53.82
    longitude = -9.5
    weather_data = get_current_weather(latitude, longitude)
    print_current_temperature_and_wind_direction(weather_data)

if __name__ == "__main__":
    main()
